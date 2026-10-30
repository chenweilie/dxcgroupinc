"""Layout and block helpers for the DXC Group Inc. static site generator."""
import html
import json
import re

BASE = "https://dxcgroupinc.com"
EMAIL = "sales@dxcgroupinc.com"
UPDATED = "October 30, 2026"
UPDATED_ZH = "2026 年 10 月 30 日"

FONTS = ("https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500"
         "&family=IBM+Plex+Sans:wght@400;500;600"
         "&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&display=swap")


def mk(lang):
    """Return t(en, zh) that picks the string for this language."""
    return (lambda en, zh: en) if lang == "en" else (lambda en, zh: zh)


def url(lang, path=""):
    """Clean directory-style URL for a page path ('' is the home page)."""
    prefix = "/zh" if lang == "zh" else ""
    if not path:
        return prefix + "/"
    return prefix + "/" + path.strip("/") + "/"


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- blocks

def section(inner, eyebrow="", title="", intro="", cls="", narrow=False):
    head = ""
    if eyebrow or title:
        head = '<div class="sec-head">'
        if eyebrow:
            head += '<p class="eyebrow">%s</p>' % eyebrow
        if title:
            head += "<h2>%s</h2>" % title
        if intro:
            head += "<p>%s</p>" % intro
        head += "</div>"
    wrap = 'wrap narrow' if narrow else 'wrap'
    return '<section class="%s"><div class="%s">%s%s</div></section>\n' % (cls, wrap, head, inner)


def cards(items, cols=3):
    """items: (num, title, text, bullets, href, more)"""
    out = '<div class="grid%d">' % cols
    for num, title, text, bullets, href, more in items:
        tag = "a" if href else "article"
        attr = ' href="%s"' % href if href else ""
        out += '<%s class="card"%s>' % (tag, attr)
        if num:
            out += '<span class="num">%s</span>' % num
        out += "<h3>%s</h3><p>%s</p>" % (title, text)
        if bullets:
            out += "<ul>%s</ul>" % "".join("<li>%s</li>" % b for b in bullets)
        if href and more:
            out += '<span class="more">%s</span>' % more
        out += "</%s>" % tag
    return out + "</div>"


def steps(items):
    return '<ol class="steps">%s</ol>' % "".join(
        "<li><h3>%s</h3><p>%s</p></li>" % (a, b) for a, b in items)


def faq(items):
    return "".join("<details><summary>%s</summary><p>%s</p></details>" % (q, a) for q, a in items)


def ledger(head_l, head_r, rows, foot):
    """rows: (label, kind) where kind is 'auto' | 'human' with display text."""
    out = '<div class="ledger"><div class="ledger-head"><span>%s</span><span>%s</span></div><ol>' % (head_l, head_r)
    for i, (label, kind, ktext) in enumerate(rows, 1):
        out += '<li><span class="n">%02d</span><span>%s</span><span class="tag %s">%s</span></li>' % (i, label, kind, ktext)
    return out + '</ol><div class="ledger-foot">%s</div></div>' % foot


def facts(pairs):
    return '<dl class="facts">%s</dl>' % "".join(
        "<div><dt>%s</dt><dd>%s</dd></div>" % (a, b) for a, b in pairs)


def fit(good_title, good, bad_title, bad):
    def col(title, items, cls):
        return '<div class="fitcol %s"><h3>%s</h3><ul>%s</ul></div>' % (
            cls, title, "".join("<li>%s</li>" % i for i in items))
    return '<div class="fit">%s%s</div>' % (col(good_title, good, "yes"), col(bad_title, bad, "no"))


def bullets(items):
    return "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in items)


def cta(lang, title=None, text=None):
    t = mk(lang)
    title = title or t("Have a process in mind?", "心里有想改进的流程吗？")
    text = text or t("Tell us about it. A few lines are enough, and we reply within two business days.",
                     "简单说几句即可，我们会在两个工作日内回复。")
    return ('<section class="cta-band"><div class="wrap"><div><h2>%s</h2><p>%s</p></div>'
            '<a class="btn light" href="%s">%s</a></div></section>\n') % (
        title, text, url(lang, "contact"), t("Book a discovery call", "预约初步沟通"))


def page_hero(lang, crumbs, h1, lede, extra=""):
    t = mk(lang)
    trail = '<a href="%s">%s</a>' % (url(lang), t("Home", "首页"))
    for label, href in crumbs:
        trail += ' / ' + ('<a href="%s">%s</a>' % (href, label) if href else label)
    return ('<section class="page-hero"><div class="wrap"><p class="crumb">%s</p><h1>%s</h1>'
            '<p class="lede">%s</p>%s</div></section>\n') % (trail, h1, lede, extra)


# ---------------------------------------------------------------- layout

def nav_items(lang):
    t = mk(lang)
    return [
        (t("Services", "服务"), url(lang, "services")),
        (t("Demos", "演示应用"), url(lang, "demos")),
        (t("How we work", "合作方式"), url(lang, "how-we-work")),
        (t("Insights", "洞察"), url(lang, "insights")),
        (t("About", "关于我们"), url(lang, "about")),
    ]


def layout(lang, path, title, desc, body, schema=None, alternates=True, og_type="website", noindex=False):
    t = mk(lang)
    canon = BASE + url(lang, path)
    links = "".join('<a href="%s">%s</a>' % (h, l) for l, h in nav_items(lang))
    other = "zh" if lang == "en" else "en"
    switch = '<a class="lang" href="%s" hreflang="%s" lang="%s">%s</a>' % (
        url(other, path), other, other, "中文" if lang == "en" else "EN") if alternates else ""
    alt = ""
    if alternates:
        alt = ('<link rel="alternate" hreflang="en" href="%s">'
               '<link rel="alternate" hreflang="zh" href="%s">'
               '<link rel="alternate" hreflang="x-default" href="%s">') % (
            BASE + url("en", path), BASE + url("zh", path), BASE + url("en", path))
    sch = ""
    if schema:
        sch = '<script type="application/ld+json">%s</script>' % json.dumps(schema, ensure_ascii=False)
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    menu = ('<details class="menu"><summary aria-label="%s">%s</summary><div class="menu-panel">%s'
            '<a href="%s">%s</a></div></details>') % (
        t("Menu", "菜单"), t("Menu", "菜单"), links, url(lang, "contact"), t("Contact", "联系"))
    head = f"""<!DOCTYPE html>
<html lang="{'en' if lang == 'en' else 'zh-Hans'}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{alt}{robots}
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="DXC Group Inc.">
<meta name="theme-color" content="#f8f6f1">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css">
{sch}
</head>
<body>
<a class="skip" href="#main">{t("Skip to content", "跳到正文")}</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{url(lang)}">DXC Group <small>INC</small></a>
<nav class="nav" aria-label="{t('Main', '主导航')}">{links}{switch}<a class="btn sm" href="{url(lang, 'contact')}">{t('Contact', '联系我们')}</a></nav>
{menu}
</div></header>
<main id="main">
"""
    foot = f"""</main>
<footer><div class="wrap">
<div class="cols">
<div><a class="brand" href="{url(lang)}" style="color:inherit">DXC Group <small style="color:inherit">INC</small></a>
<p style="margin-top:14px;max-width:36ch">{t('AI consulting and workflow automation, delivered remotely.', '远程交付的 AI 咨询与流程自动化。')}</p>
<p style="margin-top:10px"><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div><h4>{t('Services', '服务')}</h4><ul>
<li><a href="{url(lang, 'services/workflow-automation')}">{t('Workflow automation', '流程自动化')}</a></li>
<li><a href="{url(lang, 'services/ecommerce-operations')}">{t('E-commerce operations', '电商运营')}</a></li>
<li><a href="{url(lang, 'services/ai-advisory')}">{t('AI adoption advisory', 'AI 落地咨询')}</a></li>
<li><a href="{url(lang, 'demos')}">{t('Demos', '演示应用')}</a></li></ul></div>
<div><h4>{t('Company', '公司')}</h4><ul>
<li><a href="{url(lang, 'about')}">{t('About', '关于我们')}</a></li>
<li><a href="{url(lang, 'how-we-work')}">{t('How we work', '合作方式')}</a></li>
<li><a href="{url(lang, 'insights')}">{t('Insights', '洞察')}</a></li>
<li><a href="{url(lang, 'contact')}">{t('Contact', '联系')}</a></li></ul></div>
<div><h4>{t('Legal', '法律')}</h4><ul>
<li><a href="{url('en', 'privacy')}">{t('Privacy', '隐私政策')}</a></li>
<li><a href="{url('en', 'terms')}">{t('Terms', '使用条款')}</a></li>
<li><a href="{url('en', 'security')}">{t('Security', '安全实践')}</a></li></ul></div>
</div>
<p class="legal">{t('© 2026 DXC Group Inc., a California corporation. DXC Group Inc. is not affiliated with DXC Technology Company. Demos and examples on this site are illustrations built with sample data, not descriptions of client work.', '© 2026 DXC Group Inc.，加州公司。DXC Group Inc. 与 DXC Technology Company 无关联。本站的演示与示例均为使用示例数据的示意，并非客户项目的描述。')}</p>
</div></footer>
</body>
</html>
"""
    return head + body + foot


def org_schema():
    return {
        "@type": "ProfessionalService",
        "@id": BASE + "/#org",
        "name": "DXC Group Inc.",
        "url": BASE + "/",
        "email": EMAIL,
        "foundingDate": "2016",
        "description": "AI consulting and workflow automation services delivered remotely.",
        "areaServed": "US",
        "knowsAbout": ["Workflow automation", "E-commerce operations", "Document processing", "AI adoption"],
    }


def faq_schema(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in items]}


def graph(*nodes):
    return {"@context": "https://schema.org", "@graph": list(nodes)}
