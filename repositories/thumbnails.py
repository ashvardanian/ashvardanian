# /// script
# requires-python = ">=3.10"
# dependencies = ["Pillow>=11"]
# ///

import argparse
from io import BytesIO
from pathlib import Path
import subprocess

from PIL import Image


DIRECTORY = Path(__file__).resolve().parent
LIMIT = 1_000_000
LOGOS = {"AAL.VC", "unum-bio"}
EXTENSIONS = {".png", ".jpg", ".jpeg"}


def check(stems):
    errors = []
    for stem in sorted(stems):
        files = [DIRECTORY / f"{stem}{suffix}" for suffix in (".png", ".jpg", ".jpeg")]
        if stem in LOGOS or not any(path.exists() for path in files):
            continue
        png, *previews = files
        previews = [path for path in previews if path.exists()]
        if not png.exists():
            errors.append(f"{stem}: missing PNG source export")
        if len(previews) != 1:
            errors.append(f"{stem}: expected one JPEG companion")
        png_size = None
        for path in ([png] if png.exists() else []) + previews:
            try:
                with Image.open(path) as image:
                    width, height = image.size
                    expected = "PNG" if path == png else "JPEG"
                    if image.format != expected:
                        errors.append(f"{path.name}: expected {expected} data")
                    if width != 2 * height:
                        errors.append(f"{path.name}: expected a 2:1 cover")
                    if path == png:
                        png_size = image.size
                        if width < 2560 or height < 1280:
                            errors.append(f"{path.name}: PNG must be at least 2560 × 1280")
                    else:
                        if width < 1280 or height < 640:
                            errors.append(f"{path.name}: preview must be at least 1280 × 640")
                        if png_size and (width > png_size[0] or height > png_size[1]):
                            errors.append(f"{path.name}: preview exceeds PNG dimensions")
                        if image.mode != "RGB":
                            errors.append(f"{path.name}: preview must be RGB")
                        if path.stat().st_size >= LIMIT:
                            errors.append(f"{path.name}: JPEG must be below {LIMIT:,} bytes")
                    image.verify()
            except (OSError, ValueError) as error:
                errors.append(f"{path.name}: {error}")
    return errors


def preview(path):
    if path.suffix != ".png":
        raise ValueError(f"{path}: expected a PNG export")
    with Image.open(path) as source:
        if source.format != "PNG" or source.width < 2560 or source.width != 2 * source.height:
            raise ValueError(f"{path}: export a 2:1 PNG at 2× or 3× first")
        image = Image.new("RGB", source.size, "white")
        rgba = source.convert("RGBA")
        image.paste(rgba, mask=rgba.getchannel("A"))
        image.thumbnail((2560, 1280), Image.Resampling.LANCZOS)
        for quality in range(95, 39, -5):
            output = BytesIO()
            image.save(output, format="JPEG", quality=quality, optimize=True, progressive=True)
            if output.tell() < LIMIT:
                destination = path.with_suffix(".jpg")
                destination.write_bytes(output.getvalue())
                print(f"{destination.name}: {output.tell():,} bytes, quality {quality}")
                return
    raise ValueError(f"{path}: could not produce a JPEG below {LIMIT:,} bytes")


def main():
    parser = argparse.ArgumentParser(description="Prepare and validate repository thumbnail pairs.")
    parser.add_argument("command", choices=("check", "preview"))
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--base", help="Check image pairs changed between this Git ref and HEAD.")
    args = parser.parse_args()
    if args.command == "preview":
        if not args.paths or args.base:
            parser.error("preview requires PNG paths and does not accept --base")
        for path in args.paths:
            preview(path)
        return
    if args.base:
        if args.paths:
            parser.error("choose paths or --base")
        changed = subprocess.check_output(
            ["git", "diff", "--name-only", "-z", args.base, "HEAD", "--", "repositories/"],
            cwd=DIRECTORY.parent,
        ).decode().split("\0")
        paths = [DIRECTORY.parent / path for path in changed if path]
    else:
        paths = args.paths or list(DIRECTORY.iterdir())
    stems = {path.stem for path in paths if path.resolve().parent == DIRECTORY and path.suffix in EXTENSIONS}
    errors = check(stems)
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(1)
    print(f"Checked {len(stems - LOGOS)} thumbnail pairs.")


if __name__ == "__main__":
    main()
