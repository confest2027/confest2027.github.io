# AGENTS.md — CONFEST 2027 website

Repository: `confest2027/confest2027.github.io`
Public site: <https://confest2027.github.io/>

## Layout

```
site/                        The website. The ONLY published directory.
AGENTS.md                    This protocol. Never published.
README.md                    Site conventions (links, header/footer, TBD, slugs).
.github/workflows/           pages.yml deploys site/ from main;
                             check-public.yml checks pull requests to main.
tools/check-public.py        The pre-publication check (also run it locally).
```

Read `README.md` before editing anything under `site/`. Its rules apply on both branches.

## Branches

| branch | content | published |
|---|---|---|
| `dev` (default) | Full work-in-progress site. | No |
| `main` | Simplified public site. | Yes, on every push touching `site/` |

`main` is intentionally a reduced version of `dev`, not an older snapshot of it.

## Rules

1. All editing happens on `dev` (or short-lived branches off `dev`).
2. Never merge `dev` into `main`. Never push directly to `main`. A merge would publish
   work in progress.
3. Never merge `main` into `dev`. It would overwrite full pages with their simplified versions.
4. Shared files (`AGENTS.md`, `README.md`, `.gitignore`, `.github/`) are changed on `main`
   first (through a pull request), then brought to `dev` with `git cherry-pick`.
5. Nothing outside `site/` is served. Notes, drafts and tooling stay outside `site/`.
6. Public pages carry settled facts only. On `main`: no TBD placeholders, no links to
   pages that are not published, no `_template` files. Unknown items are omitted, not
   marked. (On `dev` the README's TBD convention applies as usual.)

## Publishing a page

```sh
git switch main && git pull
git switch -c publish/<slug>                 # e.g. publish/venue
git checkout dev -- site/venue.html          # bring finished files from dev
# simplify for the public: remove links to pages not yet on main,
# trim the nav to the published pages, drop unfinished sections
git commit -m "Publish venue page"
git push -u origin publish/<slug>
gh pr create --base main
```

Merging the pull request deploys the site. Before merging:

- `python3 tools/check-public.py site` passes (the pull request runs it too): no TBDs,
  no broken or root-absolute links, no missing assets.
- The header nav and footer are identical on every published page (README rule 2) and
  list only published pages.

## Preview

```sh
python3 -m http.server -d site 8000          # http://localhost:8000
```

## Deployment

GitHub Pages source: GitHub Actions (`.github/workflows/pages.yml`). The `github-pages`
environment accepts deployments from `main` only. Jekyll is not involved; no `.nojekyll`
needed. A failed deploy leaves the previous version online; see the repository's Actions tab.
