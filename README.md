# MyST Website Template

A reusable template for building websites with [MyST Markdown](https://mystmd.org/) and automated deployment via GitHub Actions.

## Features

- **MyST Markdown** source format with Jupyter notebook integration
- **GitHub Pages** deployment on push to `main`
- **Netlify PR previews** for pull request review
- **Pre-commit hooks**: Black, codespell, nbstripout for code quality

## Quick Start

1. Click **Use this template** on GitHub to create a new repository
2. Update `myst.yml` with your site title, author, and table of contents
3. Replace placeholder content in `book/` with your own pages
4. Push to GitHub to trigger automated builds

## Project Structure

```
.
├── myst.yml                    # MyST configuration
├── index.md                    # Landing page
├── requirements.txt            # Python dependencies
├── logo.png                    # Site logo
├── fav.ico                     # Favicon
├── CNAME                       # Custom domain (optional)
├── robots.txt                  # Search engine directives
├── book/                       # Site content
│   ├── preface.md
│   ├── part01/
│   │   ├── getting-started.md
│   │   └── installation.md
│   ├── part02/
│   │   └── first-example.md
│   ├── references.bib          # Bibliography
│   ├── jupytext.toml
│   └── images/                 # Shared images
├── .pre-commit-config.yaml     # Pre-commit hook configuration
├── CONTRIBUTING.md              # Contribution guidelines
├── CONDUCT.md                   # Code of conduct
└── .github/workflows/
    ├── build.yml               # PR preview builds (Netlify)
    └── deploy.yml              # Production deployment (GitHub Pages)
```

## Customization

### Site Metadata

Edit `myst.yml`:
- `project.title`: your site title
- `project.authors`: author name(s)
- `project.github`: your GitHub `username/repo`
- `project.toc`: table of contents structure

### Adding Pages

1. Create a new `.md` file in the appropriate `book/` subdirectory
2. Add the file to `project.toc` in `myst.yml`

## Building Locally

```bash
pip install -r requirements.txt
npm install -g mystmd
myst build --html
```

The built site will be in `_build/html/`.

## Deployment

### GitHub Pages (production)

Pushes to `main` automatically trigger the `deploy.yml` workflow, which builds the HTML site and deploys to GitHub Pages.

### Netlify (PR previews)

Pull requests trigger the `build.yml` workflow, which builds a preview and posts the URL as a PR comment. Requires `NETLIFY_AUTH_TOKEN` and `NETLIFY_SITE_ID` secrets.

## GitHub Secrets

| Secret | Purpose |
|--------|---------|
| `NETLIFY_AUTH_TOKEN` | Netlify authentication for PR previews |
| `NETLIFY_SITE_ID` | Netlify site ID for PR previews |

## License

[MIT](LICENSE)
