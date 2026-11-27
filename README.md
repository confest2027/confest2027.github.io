# CONFEST 2027 website

Static site for **CONFEST 2027** — the umbrella conference on concurrency theory
and formal methods — hosted by the IMT School for Advanced Studies Lucca,
Lucca, Italy, **September 6–11, 2027**: pre-conference workshops on Monday, September 6, CONCUR Tuesday to Friday, September 7–10, QEST+FORMATS Wednesday to Friday, September 8–10, and post-conference workshops on Saturday, September 11.

Plain HTML + CSS. **No build step, no framework, no JavaScript.** Every page is a
file you edit directly. Deployed on GitHub Pages from `docs/` on `main`.

Branching and publishing protocol: see [AGENTS.md](AGENTS.md).

## Structure

```
.
├── AGENTS.md                   Branch / publishing protocol
├── README.md
├── .githooks/pre-push          Runs tools/check-public.py before publishing
├── tools/check-public.py       Pre-publication check
└── docs/                       Everything published. Paths below are relative to docs/.
    ├── .nojekyll               REQUIRED: stops GitHub Pages from running Jekyll
    ├── index.html              Umbrella homepage
    ├── registration.html       Central registration (all conferences + workshops)
    ├── program.html            Unified day-by-day program (times in CEST)
    ├── speakers.html           All invited speakers, pooled, grouped by conference
    ├── organization.html       All organizer roles (single source of truth)
    ├── code-of-conduct.html    Code of conduct (linked from every footer)
    ├── venue.html              San Francesco Complex, rooms, accessibility
    ├── travel.html             Getting to/around Lucca (airports, trains, ZTL)
    ├── accommodation.html      Hotels, areas, book-early warning
    ├── concur/
    │   └── index.html          CONCUR 2027 mini-site (self-contained)
    ├── qest-formats/
    │   └── index.html          QEST+FORMATS 2027 mini-site (structural mirror of concur/)
    ├── workshops/
    │   ├── index.html          Workshop list + Call for Workshops
    │   └── _template.html      Skeleton for hosted workshops (never linked)
    └── assets/
        ├── css/style.css       The ONLY stylesheet (design tokens + components)
        ├── img/                Photos (hero-cloister.jpg, speaker photos, …)
        │   └── logo/           The CONFEST 2027 mark — badge and lockup, in
        │                       navy / white / mono / grey. See img/logo/NOTES.md
        └── ics/                Per-session calendar files, once the program is fixed
```

## Golden rules

1. **All links are relative.** Root pages link `registration.html`; pages one
   folder deep (`concur/`, `qest-formats/`, `workshops/`) link
   `../registration.html` and `../assets/css/style.css`; workshop pages two
   levels deep (`workshops/<slug>/`) use `../../`. **Never** absolute root paths
   like `/registration.html` — the site must work at any GitHub Pages root.
   This covers assets too: the header lockup, the favicon and (on `index.html`)
   the hero badge are `src`/`href` attributes that need the same prefix.

2. **The header and footer are copy-paste snippets.** The canonical template
   lives in `index.html` between the comments
   `<!-- SITE HEADER -->…<!-- /SITE HEADER -->` and
   `<!-- SITE FOOTER -->…<!-- /SITE FOOTER -->`.
   Keep the block byte-identical on every page **except** for
   (a) the `../` prefixing rule above and
   (b) `aria-current="page"` on the nav link of the page you are on.
   When the nav changes, touch **every** HTML file (there is no build step):
   `index.html`, `registration.html`, `program.html`, `speakers.html`,
   `organization.html`, `code-of-conduct.html`, `venue.html`, `travel.html`,
   `accommodation.html`, `concur/index.html`, `qest-formats/index.html`,
   `workshops/index.html`, `workshops/_template.html`, and any
   `workshops/<slug>/index.html`.

3. **The TBD convention.** Any unknown 2027 fact (deadline, fee, room, speaker,
   chair, timetable) is rendered as a visible placeholder with `class="tbd"` —
   e.g. `<span class="tbd">TBD</span>` — never guessed, never silently omitted.
   An empty `.tbd` element renders "TBD" automatically via CSS. Audit what
   still needs filling in with:

   ```sh
   grep -rn 'class="tbd"' docs --include='*.html'
   ```

4. **Organizer entry format.** Every organizer/committee entry, everywhere, is
   exactly:

   ```
   Name (Affiliation, Country) - Role
   ```

   e.g. `Mirco Tribastone (IMT School for Advanced Studies Lucca, Italy) - General Chair`.
   The name may be hyperlinked to a homepage. Unfilled roles render the literal
   template: `<li class="tbd">TBD (TBD, TBD) - Role</li>`.

5. **Slugs.** All folder names, anchors, and ids are lowercase ASCII with
   hyphens (`jane-doe`, `qest-formats`, `#important-dates`). No dots,
   apostrophes, accents, or spaces in URLs — the 2026 per-speaker URLs broke
   on exactly this.

## How to add (or remove) a main conference

1. **Copy a folder:** duplicate `qest-formats/` (or `concur/` — they are
   structural mirrors) to `<slug>/` and edit `<slug>/index.html`: title, About,
   dates, CFP, committees. Keep the section ids and the `../` links as they are.
2. **Add one nav entry to every HTML page:** insert
   `<li><a href="<slug>/index.html">NAME</a></li>` in the header nav
   (with the appropriate `../` prefix per page). The nav in each file carries an
   `ADD-A-CONFERENCE` comment marking the spot; rule 2 above lists every file.
3. **Add one homepage card:** copy an existing card in the
   conferences grid of `index.html` (a comment marks the spot). The grid auto-fits; no layout
   changes.
4. **Add one program section:** a `#<slug>` section on `program.html` (a comment
   marks the spot).

Nothing else changes. Removing a conference is the reverse: delete the folder,
remove the `<li>` from every page, remove the card and program section.

Both conferences are hosted **internally**. If a community keeps its own site
(e.g. qest-formats.org), link out with `class="external"`, but always mirror
dates, CFP, and committees locally.

## How to add a hosted workshop

1. Copy `workshops/_template.html` to `workshops/<ascii-slug>/index.html`
   (e.g. `workshops/express-sos/index.html`).
2. The clone sits one level **deeper** than the template: change every `../`
   link to `../../` (the template's leading comment flags this).
3. Replace the ALL-CAPS placeholders (name, organizers, CFP, program).
4. Add one row to the table on `workshops/index.html`.

Workshops with their own external site just get a table row with an outbound
link (`class="external"`) — no folder needed.

## Design system (assets/css/style.css)

- IMT Lucca palette as CSS custom properties on `:root`:
  navy `#062A47` (primary), orange `#F5852A` (accent), text `#051226`,
  cool grays for borders/surfaces. Change a color once, it changes site-wide.
- Inter 400/500/600 via a Google Fonts `<link>` in each page's `<head>`,
  with a system sans-serif fallback (the site works offline without it).
- Logo placements, all driven from `assets/img/logo/`:
  the white **badge** is the first nav item and the site's Home link
  (`.nav-home`, 2.75rem tall) — it carries the wordmark inside the walls, so
  there is no separate brand block and no "Home" label; the same badge is the
  homepage hero's `<h1>` (`.hero-logo`), set to the left of the two taglines by
  `.hero-layout` (stacking above them below 48em) with the dates and buttons
  full width underneath; the **grey badge** sits in the footer brand column
  (`.footer-brand img`). The badge also serves as the SVG favicon.
  Nav-link padding is 0.55rem rather than 0.65rem so the mark plus all 11 labels
  still fit on one row at the container's full width.
- Components: sticky header + wrapping nav (pure CSS), `.card-grid`
  (auto-fit, min 320px), `.table-scroll` for wide tables, `.dates-strip`,
  `.schedule-chart` (week-overview bars), `.news-timeline`, `.notice` / `.notice--warning` (e.g. the ZTL
  note and the early-booking warning), `.btn` / `.btn-secondary`, `.tbd`, print rules for `program.html`.

## Deployment (GitHub Pages)

Repository `confest2027/confest2027.github.io`, served at <https://confest2027.github.io/>.
Pages source: *Deploy from a branch*, `main` / `/docs`. Every push to `main`
republishes `docs/`. `docs/.nojekyll` must stay: without it Pages runs Jekyll,
which drops `_`-prefixed files. Work happens on `dev`; see [AGENTS.md](AGENTS.md)
for how pages move to `main`.

Because all links are relative, the same tree also works when previewed
locally (`python3 -m http.server -d docs`) and at any other Pages root.

## Content references

- CONFEST 2026 (Liverpool): <https://confest-2026.github.io/>
- CONFEST 2025 (Aarhus): <https://conferences.au.dk/confest2025/>
- CONFEST 2024 (Calgary): <https://confest2024.github.io/>
