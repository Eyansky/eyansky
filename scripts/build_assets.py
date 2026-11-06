#!/usr/bin/env python3
"""Rebuild the profile's original SVG artwork. Python standard library only."""
from pathlib import Path
from html import escape
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
BG, SURFACE, BORDER = "#0D1117", "#161B22", "#30363D"
GREEN, TEAL, WHITE, MUTED = "#3DDC97", "#22D3A7", "#F0F6FC", "#B1BAC4"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', monospace"


def text(x, y, value, size=24, color=WHITE, weight=400, mono=False):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" '
            f'font-family="{SANS if not mono else MONO}" font-weight="{weight}">'
            f'{escape(value)}</text>')


def lines(x, y, values, size=24, leading=34, color=MUTED):
    return "".join(text(x, y+i*leading, v, size, color) for i, v in enumerate(values))


def svg(name, w, h, title, body, background=BG):
    content = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
               f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">'
               f'<title id="title">{escape(title)}</title>'
               f'<desc id="desc">{escape(title)}</desc>'
               f'<rect x="0.75" y="0.75" width="{w-1.5}" height="{h-1.5}" rx="18" '
               f'fill="{background}" stroke="{BORDER}" stroke-width="1.5"/>{body}</svg>\n')
    p = ASSETS / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)


def workspace():
    # Original vector illustration: monitor, coffee, books, plant, and desk.
    return f'''
    <defs>
      <radialGradient id="glow"><stop stop-color="{GREEN}" stop-opacity=".13"/>
      <stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></radialGradient>
      <linearGradient id="screen" x2="1" y2="1"><stop stop-color="#112D28"/>
      <stop offset="1" stop-color="#101820"/></linearGradient>
    </defs>
    <ellipse cx="180" cy="147" rx="216" ry="180" fill="url(#glow)"/>
    <path d="M12 253H354M28 262H334" stroke="{BORDER}" stroke-width="2"/>
    <rect x="47" y="22" width="273" height="179" rx="12" fill="#1D282F" stroke="#43514F" stroke-width="2"/>
    <rect x="57" y="32" width="253" height="157" rx="5" fill="url(#screen)"/>
    <path d="M71 49H112M71 57H91" stroke="#38715B" stroke-width="3" stroke-linecap="round"/>
    <path d="M145 92L119 113L145 134M220 92L246 113L220 134M197 84L170 143" fill="none" stroke="{GREEN}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M87 164H128M138 164H164M173 164H207" stroke="#2B5547" stroke-width="3" stroke-linecap="round"/>
    <path d="M166 202L160 228H207L201 202" fill="#253332" stroke="#43514F"/>
    <rect x="142" y="228" width="84" height="6" rx="3" fill="#53605A"/>
    <path d="M87 246L106 236H251L268 246Z" fill="#1E2C2D" stroke="#52625D"/>
    <path d="M113 240H245" stroke="#62736B" stroke-dasharray="4 3"/>
    <rect x="267" y="227" width="73" height="10" rx="2" fill="#263D37" stroke="#476355"/>
    <rect x="273" y="216" width="65" height="10" rx="2" fill="#364339" stroke="#6B7562"/>
    <rect x="267" y="204" width="70" height="11" rx="2" fill="#23332E" stroke="#476355"/>
    <path d="M280 208H319M280 220H322M278 231H323" stroke="#849688" stroke-width="1"/>
    <path d="M20 215H56L52 247H25Z" fill="#C8D0C4"/>
    <path d="M56 220H64C77 220 74 237 55 237" fill="none" stroke="#C8D0C4" stroke-width="5"/>
    <path d="M29 214C25 205 39 203 33 194M44 211C40 201 52 200 48 191" fill="none" stroke="#6A8274" stroke-width="2" stroke-linecap="round"/>
    <path d="M314 166H351L345 199H321Z" fill="#526B5B"/>
    <path d="M332 170V115" stroke="#5CA276" stroke-width="3"/>
    <path d="M333 153C308 153 305 135 310 132C327 133 333 142 333 153Z" fill="#357757"/>
    <path d="M333 140C355 139 363 122 356 120C339 122 333 132 333 140Z" fill="#438C62"/>
    <path d="M332 127C316 121 317 105 323 102C335 109 336 119 332 127Z" fill="#63AC7D"/>
    '''


def hero(mobile=False):
    if mobile:
        body = text(32, 60, "Hi, I'm Ian.", 44, weight=650)
        body += lines(32, 112, ["I build software that works", "beautifully at scale."], 38, 49, WHITE)
        # The closing phrase alone owns the primary accent.
        body = body.replace('fill="#F0F6FC" font-size="38" font-family="'+SANS+'" font-weight="400">beautifully', 'fill="'+GREEN+'" font-size="38" font-family="'+SANS+'" font-weight="400">beautifully')
        body += lines(32, 217, ["Senior Software Engineer", "Backend, Full-Stack & AI Systems"], 24, 34, MUTED)
        body += lines(32, 303, ["10+ years turning ideas into reliable systems", "and products. Still excited by every great", "problem worth solving."], 23, 33)
        body += '<g transform="translate(122 400) scale(.96)">'+workspace()+'</g>'
        svg("hero-mobile.svg", 600, 680, "Hi, I'm Ian. I build software that works beautifully at scale.", body)
    else:
        body = text(44, 81, "Hi, I'm Ian.", 46, weight=650)
        body += text(44, 137, "I build software that works", 43, weight=600)
        body += text(44, 191, "beautifully at scale.", 46, GREEN, 600)
        body += text(44, 245, "Senior Software Engineer | Backend, Full-Stack & AI Systems", 22)
        body += lines(44, 292, ["10+ years of turning ideas into reliable systems and products.", "Still excited by every great problem worth solving."], 22, 33)
        body += '<g transform="translate(819 73) scale(.98)">'+workspace()+'</g>'
        svg("hero.svg", 1200, 380, "Hi, I'm Ian. I build software that works beautifully at scale.", body)


def terminal(mobile=False):
    w, h = (600, 398) if mobile else (1200, 290)
    body = ''.join(f'<circle cx="{32+i*20}" cy="27" r="5" fill="{c}"/>' for i,c in enumerate(["#66716E", "#84917D", "#3D8966"]))
    body += text(w-168, 34, "~/engineering", 18, MUTED, mono=True)
    body += f'<path d="M1 53H{w-1}" stroke="{BORDER}"/>'
    body += text(28, 97, "ian@eyansky:~$ whoami", 24, GREEN, mono=True)
    rows = (["> Senior Software Engineer,", "  builder & lifelong learner.", "> I turn complex problems into", "  reliable, scalable software.", "> 10+ years shipping products.", "  Still loving every line of code.", "> Building AI products & dev tools."] if mobile else ["> Senior Software Engineer, builder & lifelong learner.", "> I turn complex problems into reliable, scalable software.", "> 10+ years shipping products and still loving every line of code.", "> Currently building AI products and developer tools."])
    body += ''.join(text(28, 140+i*31, s, 23, MUTED, mono=True) for i,s in enumerate(rows))
    y = 371 if mobile else 256
    body += text(28, y, "$", 24, GREEN, mono=True)+f'<rect x="55" y="{y-19}" width="11" height="22" rx="1" fill="{GREEN}"/>'
    svg("terminal-mobile.svg" if mobile else "terminal.svg", w, h, "Ian's introduction in a static terminal window", body, SURFACE)


def about(mobile=False):
    w,h = (600, 1030) if mobile else (1200, 450)
    body = text(32, 53, "About me", 30, weight=600)
    if mobile:
        paras = [
            ["I'm a Senior Software Engineer with over a", "decade of experience building production", "software, scalable backends, and full-stack", "products."],
            ["I care about clean architecture, maintainability,", "performance, and the details that make", "software dependable."],
            ["From the first architecture discussion to the", "production deployment, I bring craftsmanship,", "curiosity, and a focus on creating real value."]]
        y=102
        for p in paras:
            body+=lines(32,y,p,24,34); y+=len(p)*34+25
        body += f'<path d="M32 525H568" stroke="{BORDER}"/>'
        x,y=32,582
        body+=text(x,y,"Current focus",30,weight=600)
        focus=[("AI products",["Building practical AI-enabled experiences."]), ("Backend architecture",["Designing dependable, maintainable services."]), ("Developer tools",["Automating workflows and improving", "engineering quality."]), ("Product engineering",["Taking ambitious ideas from concept", "to production."])]
        for name,desc in focus:
            y+=53
            body+=text(x,y,name,25,GREEN,600)
            body+=lines(x,y+34,desc,24,32)
            y+=len(desc)*32+9
    else:
        paras=[
            ["I'm a Senior Software Engineer with over a decade of", "experience building production software, scalable", "backends, and full-stack products."],
            ["I care about clean architecture, maintainability,", "performance, and the details that make software", "dependable."],
            ["From the first architecture discussion to production", "deployment, I bring craftsmanship, curiosity, and a", "focus on creating real value."]]
        y=101
        for p in paras:
            body+=lines(32,y,p,22,31);y+=len(p)*31+30
        body+=f'<path d="M624 32V418" stroke="{BORDER}"/>'
        body+=text(664,53,"Current focus",30,weight=600)
        focus=[("AI products",["Building practical AI-enabled experiences."]), ("Backend architecture",["Designing dependable, maintainable services."]), ("Developer tools",["Automating workflows; improving engineering quality."]), ("Product engineering",["Taking ideas from concept to production."])]
        y=106
        for name,desc in focus:
            body+=text(664,y,name,24,GREEN,600)
            body+=lines(664,y+33,desc,21,30);y+=92
    svg("about-mobile.svg" if mobile else "about.svg",w,h,"About Ian and his current engineering focus",body,SURFACE)


def project_art(kind):
    if kind=="glow":
        return f'<rect x="35" y="10" width="100" height="120" rx="9" fill="#162E27" stroke="#44745D"/><path d="M55 34H99M55 48H114M55 76H112M55 90H100M55 104H108" stroke="#81A896" stroke-width="4" stroke-linecap="round"/><path d="M130 39V9M115 24H145" stroke="{GREEN}" stroke-width="4" stroke-linecap="round"/>'
    if kind=="mwangi":
        return f'<rect x="8" y="18" width="156" height="103" rx="9" fill="#142A25" stroke="#44745D"/><path d="M8 43H164" stroke="#44745D"/><circle cx="23" cy="30" r="3" fill="{GREEN}"/><path d="M61 65L43 82L61 99M111 65L129 82L111 99M94 60L79 104" fill="none" stroke="{GREEN}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    return f'<path d="M85 10L143 30V68C143 100 116 118 85 132C54 118 27 100 27 68V30Z" fill="#152D25" stroke="#44745D" stroke-width="2"/><path d="M57 71L76 90L113 49" fill="none" stroke="{GREEN}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'


def projects():
    for slug,title,tag in [("glow","Glow Careers","AI · SaaS · Full-Stack · Product Engineering"),("mwangi","mwangi.dev","Consultancy · Full-Stack · Cloud · Automation"),("vibecheck","VibeCheck","Python · FastAPI · Developer Tools · Web Diagnostics")]:
        for mobile in [False,True]:
            w,h=(600,178) if mobile else (1200,170)
            body=text(32,68,title,40,GREEN,600)
            # Mobile tags remain native Markdown below each illustration.
            if not mobile: body+=text(32,115,tag,24,MUTED)
            else: body+=text(32,111,"by Ian Mwangi",24,MUTED)
            body+='<g transform="translate('+('430 17' if mobile else '983 15')+') scale('+('.9' if mobile else '1')+')">'+project_art(slug)+'</g>'
            svg(f'projects/{slug}'+('-mobile' if mobile else '')+'.svg',w,h,title,body,SURFACE)


def badges():
    for slug,label in [("python","Python"),("django","Django"),("fastapi","FastAPI"),("react","React"),("typescript","TypeScript"),("postgresql","PostgreSQL"),("docker","Docker"),("cloudflare","Cloudflare")]:
        icon=ET.parse(ASSETS/'icons'/f'{slug}.svg').getroot()
        paths=''.join(f'<path d="{e.attrib["d"]}" fill="{GREEN}"/>' for e in icon.iter() if e.tag.split('}')[-1]=='path')
        w=54+len(label)*8
        body=f'<g transform="translate(10 8) scale(.83)">{paths}</g>'+text(38,23,label,14,WHITE,500)
        svg(f'stack/{slug}.svg',w,36,label,body,SURFACE)


if __name__ == '__main__':
    for mobile in [False,True]:
        hero(mobile);terminal(mobile);about(mobile)
    projects();badges()
    print('Generated 20 SVG assets; original source logos retained in assets/icons/.')
