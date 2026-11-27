#!/usr/bin/env python3
"""Checks docs/ before it goes public (run by .githooks/pre-push).

Fails on: TBD placeholders, root-absolute links, and relative links or
assets that point to files missing from docs/.
"""
import re, sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
errors = []
for page in sorted(root.rglob("*.html")):
    if page.name.startswith("_"):
        errors.append(f"{page}: template file must not be published")
        continue
    text = page.read_text(encoding="utf-8")
    body = re.sub(r"<!--.*?-->", "", text, flags=re.S)   # ignore comments
    if re.search(r'class="[^"]*\btbd\b', body):
        errors.append(f"{page}: contains TBD placeholder")
    for ref in re.findall(r'(?:href|src)="([^"]+)"', body):
        if re.match(r"[a-z][a-z0-9+.-]*:|#|//", ref):
            continue
        if ref.startswith("/"):
            errors.append(f"{page}: root-absolute link {ref}")
            continue
        target = (page.parent / ref.split("#")[0].split("?")[0]).resolve()
        if not target.exists():
            errors.append(f"{page}: broken link {ref}")
for css in root.rglob("*.css"):
    for ref in re.findall(r'url\("?([^")]+)"?\)', css.read_text(encoding="utf-8")):
        if ref and not re.match(r"data:|[a-z]+:", ref) and not (css.parent / ref).resolve().exists():
            errors.append(f"{css}: missing {ref}")

print("\n".join(errors) or f"OK: {root} is ready to publish")
sys.exit(1 if errors else 0)
