# DXC Group Inc. website

Static site for [dxcgroupinc.com](https://dxcgroupinc.com): AI workflow automation and consulting, delivered remotely.

- `index.html`, `zh/index.html`: English and Chinese home pages
- `demos/`: three browser-only demo applications (invoice matching, ticket triage, document extraction). They use sample data and upload nothing.
- `privacy.html`, `terms.html`, `security.html`: legal and practice pages
- `assets/`: shared CSS and favicon

Preview locally: `python3 -m http.server 4311` then open http://localhost:4311

Deploy: Cloudflare Pages (root directory, no build step).
Contact: sales@dxcgroupinc.com
