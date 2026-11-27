# CONFEST 2027 logo

Two formats, three colour treatments each.

| file | use |
| --- | --- |
| `confest-2027-logo.svg` | badge, navy on transparent — light backgrounds |
| `confest-2027-logo-white.svg` | badge, white on transparent (orange year kept) — the navy `#062A47` background |
| `confest-2027-logo-mono.svg` | badge, `currentColor` throughout — inline SVG, one-colour print, embroidery |
| `confest-2027-logo-grey.svg` | badge, flat `#B4BBC7` — the site footer |
| `confest-2027-lockup.svg` | horizontal lockup, navy — site header, letterhead, slide footer |
| `confest-2027-lockup-white.svg` | horizontal lockup, white on navy |
| `confest-2027-lockup-mono.svg` | horizontal lockup, `currentColor` |
| `confest-2027-lockup-grey.svg` | horizontal lockup, flat `#B4BBC7` |

The mono files inherit the surrounding text colour only when the SVG is inlined or loaded
where CSS colour applies; used through `<img>` they fall back to black. The `-grey` pair is the
one concession to that: the mono files with the colour baked in, generated (not edited) by

    sed 's/currentColor/#B4BBC7/g' confest-2027-logo-mono.svg   > confest-2027-logo-grey.svg
    sed 's/currentColor/#B4BBC7/g' confest-2027-lockup-mono.svg > confest-2027-lockup-grey.svg

so the site footer can use a plain `<img>` on the navy ground. Re-run those lines if the mono
masters ever change. The footer uses the badge; the grey lockup is there to keep the treatment
complete across both formats. A CSS `mask` over a coloured box does the same job without the
extra files, but it fails silently in browsers that parse the shorthand differently, which is
how it failed here.

Concept: the surveyed plan of Lucca's walls read as the transition graph of an automaton.
Three generic states sit at Baluardo San Donato (W), San Pietro (NE) and San Colombano (SE);
the three wall runs between them are directed edges, so the cycle is the passeggiata delle
Mura. No initial or accepting decoration — the states are unlabelled and undecorated on
purpose, since the mark is a logo and not a claim about a specific language.

## Geometry

320×240 viewBox. Walls are three open paths, stroke 6.5, miter joins, each ending in a solid
triangular arrowhead whose tip lands on the target state's boundary. Ten baluardi plus the
Piattaforma San Frediano tab, from surveyed OSM coordinates; spike vertices are pushed out
along their outward bisector so they survive the heavy stroke. States are circles r=13 at the
same stroke 6.5. Verified against `base/base.jpg`, Mirco's reference map.

Palette: navy `#062A47` for walls, states and arrowheads; orange `#F5852A` for the year line
only.

## Wordmark

Geometric monoline capitals, no font dependency. Cap height 30 (y 82–112 for CONFEST,
124–154 for 2027), stroke 5.5, round caps and joins. Ink widths C/O/N 21, F/E 17, S 18,
T 19. Optical gaps C|O 11, O|N 12, N|F 12.5, F|E 11, E|S 10.5, S|T 9.5 — an open flank (the
C aperture, the F/E arms, the T stem) is set tighter than a stem|stem pair, which is what
keeps the rhythm even across the mixed widths. The S is two 7.5-radius bowls meeting at
y=97, terminals cut at 45° to match the C's aperture.

Both lines are centred on x=171, not on the 320-box centre of 160. Across the wordmark band
the west curtain runs in diagonally from Santa Croce to San Donato (inner edge x≈56 at y=97)
while the east salient bulges out to x=301.7, so the enclosure's local centre there is x≈171;
a box-centred line crowds the first C against the west curtain.

To be re-set in a real outlined typeface if the mark is ever taken to print at large sizes.

## Lockup

viewBox 744.7×189.9, just under 4:1. The wall circuit sits on the left, CONFEST 2027 on one line to the
right, wordmark cap block centred on the mark's ink height. The mark is the badge minus its
interior wordmark — same paths, no redrawing — at scale 0.75. The wordmark is the badge
wordmark at scale 4/3 (cap 40, stroke 7.33), so the letterforms and their stroke-to-cap ratio
are identical to the badge's; only the word space is new, set to half the cap height, and the
year is tracked to the same optical system as the name rather than the badge's looser
one-line-of-four spacing.

The mark and the wordmark therefore do *not* carry equal stroke weight here (4.88 against
7.33). That is deliberate: this mark is a large, fine-lined ring, so stroke-matching would
force the type down to roughly a sixth of the mark's height and the name would stop carrying
the lockup. The type is the constant across the two formats; the mark is what gets scaled.

## History

Three finalist options were drawn in `option-{1,2,3}/` (comparison artifact:
https://claude.ai/code/artifact/0056cb94-6d24-4728-ac6e-b85d9a567503). Option 3 won, and
within it the wordmark-inside-the-walls variant B; the rejected options and option 3's other
formats (mark/lockup/mono, and variant A with one glyph per baluardo) were removed on
2026-09-01. Variant A cannot carry the CONFEST name as drawn: one glyph per state means
CONFEST2027's 11 glyphs need an eleventh state, i.e. the Piattaforma San Frediano promoted
from platform to baluardo.
