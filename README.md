# DXC Group Inc. website

Static, bilingual (English / 简体中文) site for [dxcgroupinc.com](https://dxcgroupinc.com): AI workflow automation and consulting, delivered remotely.

## Layout

- `tools/`: the generator. Page copy lives in `pages_main.py` and `pages_rest.py`, layout and shared blocks in `lib.py`, styles in `assets-src/`, and the three demo apps in `demo-src/`.
- `site/`: generated output, committed and deployed as-is. Do not edit by hand.

## Workflow

```
python3 tools/build.py      # regenerate site/
python3 -m http.server 4312 --directory site   # preview at http://localhost:4312
```

Commit both `tools/` and `site/`. Pushing to `main` deploys `site/` to Cloudflare Pages (project `dxcgroupinc`) via GitHub Actions.

Contact: sales@dxcgroupinc.com
