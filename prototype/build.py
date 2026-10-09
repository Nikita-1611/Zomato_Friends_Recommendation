"""Build the single-file prototype from template.html.

Real photos live in assets/photos/<id>.jpg (free stock, credited in
assets/photos/CREDITS.md). Any id without a photo gets a plain neutral
stand-in tile, so the page always builds.

Writes prototype/taste-matched-picks.html (page body, published as an
artifact) and index.html at the repo root (same page as a full document).
Run: python3 prototype/build.py
"""
import base64
import json
import pathlib

HERE = pathlib.Path(__file__).parent
PHOTOS = HERE / "assets" / "photos"


def data_uri(path):
    mime = "image/png" if path.suffix == ".png" else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def build():
    page = (HERE / "template.html").read_text()
    # Embed every photo in assets/photos; the file name (without extension) is the dish id.
    found, css = [], []
    for p in sorted(PHOTOS.glob("*")) if PHOTOS.exists() else []:
        if p.suffix.lower() not in (".jpg", ".jpeg", ".png"):
            continue
        found.append(p.stem)
        css.append(f".p-{p.stem} {{ background-image: url({data_uri(p)}); }}")
    page = page.replace("/*@PHOTO_CSS@*/", "\n".join(css))
    page = page.replace("/*@HAS_PHOTO@*/[]", json.dumps(found))

    (HERE / "taste-matched-picks.html").write_text(page)
    (HERE.parent / "index.html").write_text(
        '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head>'
        '<body style="margin:0">\n' + page + "\n</body></html>\n"
    )
    print(f"built {len(page) // 1024} KB, {len(found)} photos")


if __name__ == "__main__":
    build()
