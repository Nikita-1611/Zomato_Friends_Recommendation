"""Build the single-file prototype from template.html and assets/.

Writes prototype/taste-matched-picks.html (page body, published as an artifact)
and index.html at the repo root (same page wrapped in a full HTML document).
Run: python3 prototype/build.py
"""
import base64
import pathlib

HERE = pathlib.Path(__file__).parent
ASSETS = HERE / "assets"

# dish id -> (Fluent Emoji 3D codepoint, background from, background to)
DISH_ART = {
    "roll": ("1f32f", "#fff3df", "#f7d9a6"), "dal": ("1f372", "#fdeee6", "#f4cdb8"),
    "chroll": ("1f959", "#fff0e3", "#f5cfa8"), "butter": ("1f35b", "#ffece4", "#f7c6ad"),
    "chole": ("1f963", "#eef3fb", "#d4e0f3"), "rice": ("1f35a", "#f9f5ea", "#ece2c6"),
    "naan": ("1fad3", "#fff6e6", "#f2dcb0"), "jamun": ("1f9c6", "#fdf0e4", "#efd2b2"),
    "gdosa": ("1f32e", "#fff7df", "#f6e1a5"), "mdosa": ("1f32e", "#f3f7e6", "#dbe8b9"),
    "vada": ("1f369", "#fdf1e4", "#f1d5b3"), "bisi": ("1f35c", "#fff0e0", "#f4cfa0"),
    "filter": ("2615", "#f6efe9", "#e2d3c6"), "vbir": ("1f958", "#fff1df", "#f6d4a2"),
    "cbir": ("1f958", "#fdebe2", "#f2c4ae"), "kebab": ("1f356", "#fbeee6", "#ecc9b6"),
    "sheermal": ("1fad3", "#fff3e8", "#f5d2b4"), "raita": ("1f963", "#eef6f2", "#cfe6da"),
    "phirni": ("1f36e", "#fff8e8", "#f3e2b4"), "cold": ("1f964", "#f4eef9", "#e0d4ee"),
    "cappu": ("2615", "#f3ece6", "#dccbbb"), "croissant": ("1f950", "#fff5e3", "#f3dcae"),
    "sandwich": ("1f96a", "#f1f6e8", "#d8e6c2"), "cake": ("1f370", "#fbeef0", "#f0d0d6"),
}
# restaurant id -> two dishes for the card image, background
REST_ART = {
    "sr": ("1f32f", "1f372", "#fbe3c4", "#f1b98a"),
    "ll": ("1f958", "1f356", "#fde9cf", "#f3c48c"),
    "uc": ("1f32e", "2615", "#eaf3df", "#c9e0b0"),
    "bs": ("1f964", "1f950", "#efe7f6", "#d6c6ea"),
}

# home category row: id -> codepoint
CAT_ART = {
    "all": "1f37d-fe0f", "rolls": "1f32f", "thali": "1f35b", "biryani": "1f958",
    "dosa": "1f32e", "dessert": "1f9c6", "coffee": "2615",
}


def data_uri(path, mime):
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def dish(code):
    return data_uri(ASSETS / "dishes" / f"{code}.webp", "image/webp")


def build():
    cache = {}
    def img(code):
        if code not in cache:
            cache[code] = dish(code)
        return cache[code]

    css = []
    for k, (code, a, b) in DISH_ART.items():
        css.append(f".a-{k} {{ background: url({img(code)}) center/76% no-repeat, linear-gradient(135deg, {a}, {b}); }}")
        css.append(f".i-{k} {{ background: url({img(code)}) center/contain no-repeat; }}")
    for k, (c1, c2, a, b) in REST_ART.items():
        css.append(f".a-rest-{k} {{ background: url({img(c1)}) 24% 58%/38% no-repeat, url({img(c2)}) 76% 46%/34% no-repeat, linear-gradient(135deg, {a}, {b}); }}")

    for k, code in CAT_ART.items():
        css.append(f".c-{k} {{ background-image: url({img(code)}); }}")

    avatars = {p.stem: data_uri(p, "image/svg+xml") for p in sorted((ASSETS / "avatars").glob("*.svg"))}
    av_js = "const AV = {" + ", ".join(f'{k}: "{v}"' for k, v in avatars.items()) + "};"

    page = (HERE / "template.html").read_text()
    assert "/*@ART_CSS@*/" in page and "/*@AVATARS@*/" in page
    page = page.replace("/*@ART_CSS@*/", "\n".join(css)).replace("/*@AVATARS@*/", av_js)

    (HERE / "taste-matched-picks.html").write_text(page)
    (HERE.parent / "index.html").write_text(
        '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head>'
        '<body style="margin:0">\n' + page + "\n</body></html>\n"
    )
    print(f"built {len(page) // 1024} KB")


if __name__ == "__main__":
    build()
