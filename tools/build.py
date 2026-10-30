#!/usr/bin/env python3
"""Build the DXC Group Inc. static site into ./site (run from anywhere)."""
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import BASE, layout, url  # noqa: E402
import pages_main as pm  # noqa: E402
import pages_rest as pr  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site"
SRC = Path(__file__).resolve().parent

DEMO_MAP = {"invoice-match": "invoice-matching", "ticket-triage": "ticket-triage",
            "document-extraction": "document-extraction"}

urls = []  # (path, [langs])


def write(rel, content):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def emit(lang, path, built, alternates=True, og_type="website"):
    title, desc, body, schema = built
    rel = (("zh/" if lang == "zh" else "") + (path + "/" if path else "")) + "index.html"
    write(rel, layout(lang, path, title, desc, body, schema, alternates, og_type))


def both(path, fn, *args):
    for lang in ("en", "zh"):
        emit(lang, path, fn(lang, *args))
    urls.append((path, ["en", "zh"]))


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    # assets
    css = (SRC / "assets-src/styles.css").read_text() + "\n" + (SRC / "assets-src/demo.css").read_text()
    write("assets/styles.css", css)
    shutil.copy(SRC / "assets-src/favicon.svg", OUT / "assets/favicon.svg")

    arts = pr.articles()
    ins_cards = [dict(slug=a["slug"], title=a["en"]["title"], desc=a["en"]["desc"]) for a in arts]

    # home (needs per-language article cards)
    for lang in ("en", "zh"):
        cards = [dict(slug=a["slug"], title=a[lang]["title"], desc=a[lang]["desc"]) for a in arts]
        emit(lang, "", pm.home(lang, cards))
    urls.append(("", ["en", "zh"]))

    both("services", pm.services_hub)
    rel = [dict(slug=a["slug"], services=a["services"]) for a in arts]
    for s in ("workflow-automation", "ecommerce-operations", "ai-advisory"):
        for lang in ("en", "zh"):
            rl = [dict(slug=a["slug"], title=a[lang]["title"], desc=a[lang]["desc"], services=a["services"]) for a in arts]
            emit(lang, "services/" + s, pm.service_page(lang, s, rl))
        urls.append(("services/" + s, ["en", "zh"]))

    both("how-we-work", pr.how_we_work)
    both("about", pr.about)
    both("contact", pr.contact)
    both("demos", pr.demos_hub)
    both("insights", pr.insights_hub)
    for a in arts:
        for lang in ("en", "zh"):
            emit(lang, "insights/" + a["slug"], pr.article_page(lang, a), og_type="article")
        urls.append(("insights/" + a["slug"], ["en", "zh"]))

    # demo apps: wrap the existing hand-written demo pages in the shared layout (English UI)
    for src, slug in DEMO_MAP.items():
        h = (SRC / "demo-src" / (src + ".html")).read_text()
        title = re.search(r"<title>(.*?)</title>", h).group(1)
        desc = re.search(r'<meta name="description" content="(.*?)"', h).group(1)
        main = re.search(r"<main>(.*?)</main>", h, re.S).group(1)
        script = re.search(r"(<script>.*?</script>)", h, re.S).group(1)
        main = (main.replace('href="/#cases"', 'href="%s"' % url("en", "demos"))
                    .replace('href="/#contact"', 'href="%s"' % url("en", "contact")))
        main = re.sub(r'<p class="crumb">.*?</p>',
                      '<p class="crumb"><a href="/">Home</a> / <a href="/demos/">Demos</a> / %s</p>' %
                      re.search(r"/ ([^<]+)</p>", main).group(1), main, count=1, flags=re.S)
        emit("en", "demos/" + slug, (title, desc, main + script, None), alternates=False)
        urls.append(("demos/" + slug, ["en"]))

    for kind in ("privacy", "terms", "security"):
        emit("en", kind, pr.legal(kind), alternates=False)
        urls.append((kind, ["en"]))

    t, d, b, s = pr.not_found()
    write("404.html", layout("en", "404", t, d, b, s, alternates=False, noindex=True))

    # sitemap
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for path, langs in urls:
        for lang in langs:
            sm.append("<url><loc>%s</loc>" % (BASE + url(lang, path)))
            if len(langs) == 2:
                for l2 in langs:
                    sm.append('<xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (l2, BASE + url(l2, path)))
                sm.append('<xhtml:link rel="alternate" hreflang="x-default" href="%s"/>' % (BASE + url("en", path)))
            sm.append("</url>")
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE)
    write("_headers", """/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()

/assets/*
  Cache-Control: public, max-age=86400
""")
    n = sum(1 for _ in OUT.rglob("*.html"))
    print("built %d html pages into %s" % (n, OUT))


if __name__ == "__main__":
    main()
