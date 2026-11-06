#!/usr/bin/env python3
"""Validate public profile content without third-party Python dependencies.

Run offline in CI; optionally use --check-links for a live public URL check.
"""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def require(condition, message):
    if not condition:
        ERRORS.append(message)


class ReadmeHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        require(tag in {'picture', 'source', 'img', 'a'}, f'Unsupported README HTML: {tag}')
        for key, value in attrs.items():
            require(key in {'media', 'srcset', 'src', 'width', 'alt', 'href'},
                    f'Unsupported README HTML attribute: {key}')
            require(not key.startswith('on'), f'Event handler found: {key}')
        if tag == 'img':
            require(bool(attrs.get('alt', '').strip()), 'Image needs descriptive alt text')
        self.refs.extend(attrs[k] for k in ('src', 'srcset', 'href') if k in attrs)


def slug(heading):
    return re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')


def validate():
    readme = (ROOT / 'README.md').read_text()
    parser = ReadmeHTML()
    parser.feed(readme)
    refs = parser.refs + re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', readme)
    anchors = {slug(s) for s in re.findall(r'^#{1,6}\s+(.+)$', readme, re.M)}
    for url in refs:
        parsed = urlsplit(url)
        require(parsed.scheme in ('', 'https', 'mailto'), f'Unsafe URL: {url}')
        if not parsed.scheme and not parsed.netloc:
            if parsed.path:
                path = (ROOT / unquote(parsed.path)).resolve()
                require(path.is_relative_to(ROOT), f'Reference escapes repo: {url}')
                require(path.is_file(), f'Missing local reference: {url}')
            elif parsed.fragment:
                require(parsed.fragment in anchors, f'Missing heading anchor: {url}')
    for alt, ref in re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', readme):
        require(bool(alt.strip()), f'Markdown image needs alt text: {ref}')
    require(not re.search(r'<(?:style|script|iframe|foreignObject)\b',readme,re.I),
            'README contains executable or unsupported markup')
    svgs = sorted((ROOT / 'assets').rglob('*.svg'))
    for path in svgs:
        raw = path.read_text()
        require(path.stat().st_size < 256_000, f'Oversized SVG: {path.name}')
        require('<!DOCTYPE' not in raw and '<!ENTITY' not in raw, f'Unsafe XML declaration: {path.name}')
        try:
            root = ET.fromstring(raw)
        except ET.ParseError as error:
            ERRORS.append(f'Invalid SVG {path.name}: {error}')
            continue
        require(root.tag == '{http://www.w3.org/2000/svg}svg', f'Missing SVG namespace: {path.name}')
        box = root.attrib.get('viewBox','').split()
        require(len(box) == 4 and all(float(x) > 0 for x in box[2:]), f'Invalid viewBox: {path.name}')
        ids = {e.attrib['id'] for e in root.iter() if 'id' in e.attrib}
        for e in root.iter():
            tag = e.tag.split('}')[-1]
            require(tag not in {'script','foreignObject','image','animate','animateTransform','set','a'},
                    f'Non-static or external SVG element in {path.name}: {tag}')
            for key, value in e.attrib.items():
                attr = key.split('}')[-1]
                require(not attr.startswith('on'), f'SVG event handler: {path.name}')
                if attr in {'href','src'}:
                    require(value.startswith('#'), f'External SVG reference: {path.name}')
                for target in re.findall(r'url\((.*?)\)', value):
                    require(target.startswith('#') and target[1:] in ids,
                            f'Broken SVG paint reference in {path.name}: {target}')
        if path.parent.name != 'icons':
            require(root.find('{http://www.w3.org/2000/svg}title') is not None,
                    f'SVG needs accessible title: {path.name}')
    secret_patterns = [r'gh[pousr]_[A-Za-z0-9]{30,}',r'github_pat_[A-Za-z0-9_]{30,}',
                       r'AKIA[A-Z0-9]{16}',r'-----BEGIN [A-Z ]*PRIVATE KEY-----']
    for path in ROOT.rglob('*'):
        if not path.is_file() or '.git' in path.parts:
            continue
        require(path.name != '.env' and not path.name.startswith('.env.'), f'Environment file: {path}')
        data = path.read_text(errors='ignore')
        require(not any(re.search(p,data) for p in secret_patterns), f'Potential secret: {path.relative_to(ROOT)}')
    return svgs, sorted({u for u in refs if u.startswith('https://')})


def check_links(urls):
    for url in urls:
        try:
            # GET validates the public destination; never submits product forms.
            with urlopen(Request(url, headers={'User-Agent':'profile-link-validator/1.0'}),timeout=25) as response:
                require(response.status == 200, f'Link returned {response.status}: {url}')
                print(f'  {response.status} {url}')
        except Exception as error:
            ERRORS.append(f'Link check failed {url}: {error}')


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--check-links',action='store_true')
    options = args.parse_args()
    svgs, urls = validate()
    if options.check_links:
        check_links(urls)
    if ERRORS:
        print('\n'.join(f'ERROR: {e}' for e in ERRORS), file=sys.stderr)
        sys.exit(1)
    print(f'PASS: {len(svgs)} valid static SVGs; README paths, anchors, alt text, supported HTML, and public-content checks.')
