# AGENTS.md — CONFEST 2027 website

Repository: `confest2027/confest2027.github.io`
Public site: <https://confest2027.github.io/>

## Layout

```
docs/                        The website. The ONLY published directory.
AGENTS.md                    This protocol. Never published.
README.md                    Site conventions (links, header/footer, TBD, slugs).
tools/check-public.py        The pre-publication check.
.githooks/pre-push           Runs the check before any push to publish/* or main.
```

Read `README.md` before editing anything under `docs/`. Its rules apply on both branches.

After cloning, enable the hook once: `git config core.hooksPath .githooks`

## Branches

| branch | content | published |
|---|---|---|
| `dev` (default) | Full work-in-progress site. | No |
| `main` | Simplified public site. | Yes, on every push |

`main` is intentionally a reduced version of `dev`, not an older snapshot of it.

## Rules

1. All editing happens on `dev` (or short-lived branches off `dev`).
2. Never merge `dev` into `main`. Never push directly to `main`. A merge would publish
   work in progress.
3. Never merge `main` into `dev`. It would overwrite full pages with their simplified versions.
4. Shared files (`AGENTS.md`, `README.md`, `.gitignore`, `.githooks/`, `tools/`) are changed
   on `main` first (through a pull request), then brought to `dev` with `git cherry-pick`.
5. Nothing outside `docs/` is served. Notes, drafts and tooling stay outside `docs/`.
6. Public pages carry settled facts only. On `main`: no TBD placeholders, no links to
   pages that are not published, no `_template` files. Unknown items are omitted, not
   marked. (On `dev` the README's TBD convention applies as usual.)
7. `docs/.nojekyll` must exist on both branches.

## Publishing a page

```sh
git switch main && git pull
git switch -c publish/<slug>                 # e.g. publish/venue
git checkout dev -- docs/venue.html          # bring finished files from dev
# simplify for the public: remove links to pages not yet on main,
# trim the nav to the published pages, drop unfinished sections
git commit -m "Publish venue page"
git push -u origin publish/<slug>            # the pre-push hook runs the check
gh pr create --base main
```

Merging the pull request publishes the site within a minute or two. Before merging:

- `python3 tools/check-public.py docs` passes: no TBDs, no broken or root-absolute
  links, no missing assets. GitHub does not run it; the hook or you must.
- The header nav and footer are identical on every published page (README rule 2) and
  list only published pages.

## Preview

```sh
python3 -m http.server -d docs 8000          # http://localhost:8000
```

## Deployment

GitHub Pages source: *Deploy from a branch*, `main` / `/docs` (Settings → Pages).
No workflows in this repository. A failed build leaves the previous version online;
see the repository's Actions tab ("pages build and deployment").
