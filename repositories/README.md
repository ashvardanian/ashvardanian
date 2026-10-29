# Repository Thumbnails

Export every new or refreshed repository cover as a matching `<name>.png` and `<name>.jpg` pair.
Keep established filenames, including version and dark-theme suffixes, because other repositories link to them.

- PNG: export the 1280 × 640 Figma frame at __3×__ (3840 × 1920), or at least __2×__ (2560 × 1280).
  Export from the source frame; do not upscale an old JPEG.
- JPEG: generate an RGB preview from that PNG, strictly below __1,000,000 bytes__.
  The preview command uses 2560 × 1280 pixels.
  Use the JPEG for README embeds and online previews, and the PNG for high-resolution reuse.
- Keep both files under the same stem rather than adding `@2x` or `@3x` to their names.
  The pixel dimensions record the export scale while existing URLs stay stable.

After saving PNG exports, generate their previews and check the pairs:

```sh
uv run repositories/thumbnails.py preview repositories/FatWheels.png repositories/TablEval.png
uv run repositories/thumbnails.py check repositories/FatWheels.png repositories/TablEval.png
```

Run `uv run repositories/thumbnails.py check` to audit the entire folder.
CI checks pairs touched by each push or pull request; older files remain visible in the full audit until their source artwork is re-exported.
The standalone `AAL.VC` and `unum-bio` logos are excluded from cover checks.
