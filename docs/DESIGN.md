# Design specification

The profile is a GitHub-native README with original, repository-owned SVGs. No application framework, JavaScript, external image widgets, or runtime font downloads are required.

## Identity

| Role | Value |
| --- | --- |
| Background | `#0D1117` |
| Surface | `#161B22` |
| Main accent | `#3DDC97` |
| Secondary accent | `#22D3A7` |
| Border | `#30363D` |
| Primary text | `#F0F6FC` |
| Supporting text | `#B1BAC4` |

Native Markdown follows the visitor's GitHub theme. Artwork retains its own opaque dark background and contrasting text in both themes. Text uses system sans-serif fallbacks; terminal text uses system monospace fallbacks. Accent green is reserved for emphasis and artwork. Thin borders are decorative, not essential control boundaries.

## Hierarchy and responsive layout

The hero establishes name, engineering position, experience, and personality. A static terminal adds the voice of a working engineer. About and Current Focus share a two-column desktop graphic and become vertically stacked on mobile. Expertise precedes the live product showcase; experience, principles, public code, and contact complete the page.

The desktop hero is 1200 × 380. GitHub scales it to its content column. A `<picture>` source at 600px switches to a separately composed mobile asset rather than shrinking desktop copy. Terminal, About/Focus, and project mastheads also have mobile compositions. The project descriptions, features, tags, and destinations use native Markdown and wrap normally. No layout tables or unsupported CSS are used.

Trade-off: static SVG panels preserve the intended illustration and desktop/mobile composition, but text within those panels cannot be selected like native Markdown. Full text alternatives are supplied; long product and engineering descriptions remain native. GitHub controls page chrome, typography outside artwork, native repository cards, and the contribution graph.

## Artwork and provenance

- Workspace illustration, terminal, About/Focus panel, and project illustrations are original vector artwork built by `scripts/build_assets.py`.
- Technology logos are unmodified path geometry from [Simple Icons](https://github.com/simple-icons/simple-icons), downloaded from its public `icons/` directory on 2026-11-06. Badge builds recolor the paths and retain local source SVGs under `assets/icons/`.
- Simple Icons is distributed under [CC0](https://github.com/simple-icons/simple-icons/blob/develop/LICENSE.md); brand names and logos remain their respective owners' trademarks. Inclusion communicates technology familiarity, not endorsement.

## Content provenance

Name, title, 10+ years, Kenya, skills, company names, general experience, product ownership, and the VibeCheck Python/FastAPI attribution come from Ian's supplied brief. Company-specific dates, titles, metrics, and achievements are intentionally absent.

Live public product pages were checked on 2026-11-06:

- [Glow Careers](https://www.glow.careers): AI resumes, review, tailoring, cover letters, and job discovery.
- [mwangi.dev](https://www.mwangi.dev): websites, AI automation, integrations, dashboards, consultancy; its footer explicitly publishes `ian@mwangi.dev`.
- [VibeCheck](https://www.mwangi.dev/vibecheck): security, performance, accessibility, and discoverability diagnostics. A direct HTTP request returned 200 after the web reader failed to load it.


GitHub-native activity is linked, rather than copied into a static statistics panel. Repository totals, stars, follower counts, contributions, and language percentages are not hardcoded.
