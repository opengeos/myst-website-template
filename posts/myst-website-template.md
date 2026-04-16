---
title: "A Reusable Template for Building Websites with MyST Markdown"
date: 2026-04-07
authors:
  - name: Qiusheng Wu
    email: qwu18@utk.edu
    orcid: 0000-0001-5437-4073
    url: https://gishub.org
description: A GitHub template that bundles MyST Markdown, GitHub Pages deployment, Netlify PR previews, and pre-commit hooks into a ready-to-use starting point.
thumbnail: https://img.youtube.com/vi/wj0kAthmusA/maxresdefault.jpg
tags:
  - MyST Markdown
  - GitHub Template
  - GitHub Actions
  - Pre-commit
keywords:
  - MyST Markdown
  - GitHub Template
  - GitHub Actions
  - Pre-commit
---

# A Reusable Template for Building Websites with MyST Markdown

After rebuilding my [personal website](https://gishub.org) with [MyST Markdown](https://mystmd.org), I found myself wanting to share the setup with others. The configuration work -- GitHub Actions, pre-commit hooks, directory structure, deployment pipelines -- took real effort to get right. To make it easier for anyone to start from a working foundation, I created [myst-website-template](https://github.com/opengeos/myst-website-template), a GitHub template repository that bundles everything into a single click.

## Why a Template?

Starting a MyST site from scratch is straightforward if all you need is a single page. But a production-ready site involves more than content:

- A GitHub Actions workflow that builds and deploys on every push.
- A second workflow that generates preview builds for pull requests.
- Pre-commit hooks that catch formatting issues, typos, and bloated notebook metadata before they reach the repository.
- A sensible directory layout that scales as pages are added.
- Community files like a license, code of conduct, and contributing guide.

Setting all of this up by hand takes time and introduces opportunities for small mistakes. The template packages these pieces together so that a new project starts with a complete, tested setup rather than an empty directory.

## What Is Included

- **MyST Markdown with Jupyter integration** -- Write content in Markdown or Jupyter notebooks. MyST renders both into a polished HTML site with support for directives, roles, cross-references, and executable code cells.
- **Book theme** -- The built-in [book theme](https://mystmd.org/guide/website-templates) provides a sidebar, table of contents, and search out of the box. No custom templates needed.
- **Organized content structure** -- Pages live in a `pages/` directory organized into logical parts (`part01/`, `part02/`, etc.), making it easy to group related content.
- **BibTeX bibliography support** -- Add references to `pages/references.bib` and cite them directly in your Markdown files.
- **Jupytext** -- Round-trip conversion between `.ipynb` and `.md` formats, so notebooks can be version-controlled as plain text.
- **GitHub Pages deployment** -- The `deploy.yml` workflow builds the HTML site and publishes it to GitHub Pages on every push to `main`.
- **Netlify PR previews** -- The `build.yml` workflow builds a preview for every pull request, making it easy to review changes before merging.
- **Pre-commit hooks** -- [Black](https://github.com/psf/black) for Python and Jupyter formatting, [codespell](https://github.com/codespell-project/codespell) for typo detection, [nbstripout](https://github.com/kynan/nbstripout) for cleaning notebook metadata, plus standard checks for YAML, TOML, trailing whitespace, and large files.
- **Dependabot** -- Weekly dependency update checks for Python packages, GitHub Actions, and Docker images.
- **Community defaults** -- MIT license, Contributor Covenant code of conduct, and a contributing guide are included from the start.

## Getting Started

1. Go to the [template repository](https://github.com/opengeos/myst-website-template) and click **Use this template** to create a new repository.
2. Open `myst.yml` and update the project title, author name, GitHub URL, and table of contents to match your content.
3. Replace the placeholder pages in the `pages/` directory with your own Markdown files or Jupyter notebooks.
4. Push to `main`. GitHub Actions will build the site and deploy it to GitHub Pages automatically.

That is all it takes. PR previews will also work once you connect Netlify and add the `NETLIFY_AUTH_TOKEN` and `NETLIFY_SITE_ID` secrets to your repository.

## Customization

The template is designed to be modified. A few common adjustments:

- **Site metadata**: Edit the `project` section in `myst.yml` to set your title, authors, copyright year, and GitHub link.
- **Table of contents**: Add or remove entries in `project.toc` to control the sidebar navigation. Pages can be grouped under titled sections with `children` lists.
- **Custom domain**: Add a `CNAME` file with your domain name and remove the `BASE_URL` environment variable from `deploy.yml`.
- **Styling**: Uncomment the `style: custom.css` line in `myst.yml` and add your own CSS overrides.
- **Analytics**: Uncomment and fill in `analytics_google` in the site options to enable Google Analytics.

To build locally, install the dependencies and run:

```bash
pip install -r requirements.txt
npm install -g mystmd
myst build --html
```

The output will be in `_build/html/`.

To start running the website locally, run:
```bash
myst start
```

## Lessons Learned

- **Templates lower the barrier to entry.** Most of the setup work is invisible once it is done. Packaging it into a template means new projects start with a working deployment pipeline instead of spending their first hours on configuration.
- **Pre-commit hooks prevent common mistakes.** Catching formatting issues, typos, and bloated notebook metadata before they reach the repository keeps the commit history clean and reduces noise in code reviews.
- **Separating production from preview keeps feedback fast.** Having one workflow for GitHub Pages and another for Netlify PR previews means contributors can see their changes without affecting the live site.
- **Open-source defaults matter.** Including a license, code of conduct, and contributing guide from day one makes a repository welcoming to contributors without requiring extra effort later.
