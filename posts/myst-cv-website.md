---
title: "Build a Professional CV Website with Auto PDF Generation Using MyST Markdown"
date: 2026-04-10
authors:
  - name: Qiusheng Wu
    email: qwu18@utk.edu
    orcid: 0000-0001-5437-4073
    url: https://gishub.org
description: A step-by-step tutorial on building a personal CV website with MyST Markdown and Typst that automatically generates a PDF version of your CV from the same Markdown source.
thumbnail: https://img.youtube.com/vi/KiceHVININs/maxresdefault.jpg
tags:
  - MyST Markdown
  - Typst
  - CV
  - GitHub Pages
  - Tutorial
keywords:
  - MyST Markdown
  - Typst
  - CV
  - GitHub Pages
  - Tutorial

---

# Build a Professional CV Website with Auto PDF Generation Using MyST Markdown

If you work in academia, chances are you maintain a personal website and a separate CV document – maybe in Google Docs, Microsoft Word, or LaTeX. Keeping the two in sync is tedious, and they inevitably drift apart. In this tutorial, I walk through how to set up a single Markdown-based source that powers both a live website and a professionally formatted PDF CV, all deployed automatically through GitHub Pages. You edit Markdown, push to GitHub, and both your website and your PDF update on their own.

:::{iframe} https://www.youtube.com/embed/KiceHVININs
:width: 100%
Video tutorial: Build a Professional CV Website with Auto PDF Generation
:::

## What You Will Need

- A [GitHub](https://github.com) account (free).
- For local preview and customization: a code editor like [VS Code](https://code.visualstudio.com) or [Cursor](https://cursor.com), [Node.js](https://nodejs.org) (version 18 or later), and Python 3.

## Create Your Repository from the Template

1. Go to the [myst-cv-template](https://github.com/opengeos/myst-cv-template) repository on GitHub.
2. Click the green **Use this template** button in the upper right corner, then select **Create a new repository**.
3. Choose your GitHub account as the owner and give the repository a name – something like `my-cv` or `cv`.
4. Set the repository to **Public** or **Private**. Either works; the deployed website will be public regardless.
5. Click **Create repository** and wait a few seconds for GitHub to copy the template.

## Enable GitHub Pages

The first deployment will fail because GitHub Pages is not enabled by default. To fix that:

1. Go to your new repository's **Settings** tab.
2. In the left sidebar, click **Pages**.
3. Under **Build and deployment**, change the source to **GitHub Actions**.
4. Go back to the **Actions** tab. Click into the failed workflow run, then click **Re-run all jobs** to trigger a fresh build.
5. After a minute or two, your site will be live at `https://username.github.io/repo-name`.

To make the URL visible on your repository page, go to the repository's **About** section (gear icon), check **Use your GitHub Pages website**, and save.

## Clone and Customize Your Content

Clone the repository to your local machine:

```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

Open the project in your code editor. The content lives in these key files:

- **`myst.yml`**: Controls the site title, navigation menu, and theme. The `toc` (table of contents) section defines which pages appear in the sidebar. Add, remove, or reorder entries here.
- **`index.md`**: The homepage. Update your name, title, subtitle, and recent news.
- **`pages/about.md`**: Biography, education, and appointments.
- **`pages/research.md`**: Publications, patents, books, and grants.
- **`pages/software.md`**: Open-source packages and tools.
- **`pages/teaching.md`**: Courses and mentoring.
- **`pages/talks.md`**: Workshops, invited talks, and conference presentations.
- **`pages/awards.md`**: Awards and honors.
- **`pages/services.md`**: Professional and institutional service tables.
- **`pages/media.md`**: Social media and press coverage.

### Bulk-Replace the Template Name

The fastest way to start is to use your editor's **Find and Replace** across the entire project. Search for the placeholder name used in the template and replace it with your own name. This updates the homepage, page headers, and configuration in one step.

Then update your title, position, department, and other details in `index.md` and the individual page files. Every page uses plain Markdown with YAML frontmatter, so there is no HTML to wrestle with.

## Preview Locally

Install the Python dependencies and start the local development server:

```bash
pip install -r requirements.txt
myst start
```

This launches a preview at `http://localhost:3000`. Changes to your Markdown files are reflected in the browser automatically. You can also use your editor's built-in browser panel to preview side by side as you edit.

## How the CV PDF Generation Works

The template includes a Python script called `generate_cv.py` that reads the same Markdown files powering your website and produces a [Typst](https://typst.app) source file (`cv.typ`). Typst is a modern typesetting system – think of it as a faster, simpler alternative to LaTeX.

The script pulls content from your page files (`about.md`, `research.md`, `software.md`, `teaching.md`, `talks.md`, `awards.md`, `services.md`, `media.md`) and assembles them into a single document. The header section of `generate_cv.py` is the only part you need to customize – it contains your name, email, GitHub username, website URL, and other contact details that appear at the top of the PDF.

You can control which sections appear in your CV by editing `generate_cv.py`. Not everything on your website needs to be in the PDF; you pick what to include.

## Generate the PDF Locally (Optional)

You do not need to generate the PDF locally – GitHub Actions handles it automatically on every push. But if you want to preview it:

```bash
python generate_cv.py
typst compile cv.typ cv.pdf –font-path ./fonts –ignore-system-fonts
```

Before running Typst locally, download the required fonts. The command is in the repository's `README.md` file. The fonts include Font Awesome icons used for social media links in the CV header.

The generated `cv.pdf` is listed in `.gitignore`, so it will not be committed to your repository. The production PDF is built fresh during each GitHub Actions deployment.

## Add Blog Posts

The template includes a built-in blog. To add a new post:

1. Create a new Markdown file in the `blog/` directory (e.g., `blog/my-first-post.md`).
2. Add YAML frontmatter with `title`, `date`, `description`, and other metadata.
3. Write your content in Markdown.
4. Open `pages/blog.md` (or `blog.md`, depending on the template version) and add a new `:::{card}` entry inside the grid:

```markdown
:::{card} My First Blog Post
:link: ./blog/my-first-post
April 10, 2026 – A short description of the post.
:::
```

The grid layout (`1 1 2 2`) means one column on small screens and two columns on larger screens, keeping the layout responsive.

The template also generates RSS and Atom feeds automatically, so readers can subscribe to your blog. The feed links appear on the blog index page.

## Deploy and Verify

Once you are happy with your changes, commit and push:

```bash
git add .
git commit -m "Update website content"
git push
```

GitHub Actions will:

1. Build the HTML site with `myst build –html`.
2. Download fonts for the CV.
3. Run `generate_cv.py` to produce the Typst source.
4. Compile the PDF with Typst.
5. Deploy everything to GitHub Pages.

After a minute or two, visit your site and click the CV link. The PDF is served at a stable URL (`https://username.github.io/repo-name/cv.pdf`) that you can share with anyone. It includes bookmarks and a clickable table of contents for easy navigation, especially useful as your CV grows longer.

### Using Pull Requests

For larger changes, consider creating a feature branch and opening a pull request instead of pushing directly to `main`. The template includes a pre-commit configuration that catches typos, trailing whitespace, and formatting issues. This workflow also triggers a Netlify preview deployment so you can review your changes before merging.

## Responsive Layout and Theming

The site uses the MyST book theme, which supports both light and dark modes. The layout is responsive – grid components like `::::{grid} 2 2 4 4` show two columns on small screens and four on large screens. You can adjust these numbers on any grid to fit your content.

For further visual customization, the template includes a `custom.css` file where you can override theme defaults without modifying the MyST source.

## What is Next

This tutorial covers the full workflow from template to deployed site with automatic CV generation. For background on why I chose this approach for my own website, see [Launching My New Website with MyST Markdown and Typst](./launching-new-website). If you are looking for a simpler website without the CV feature, check out [Build a Personal Website in 5 Minutes: No Coding Required](./build-personal-website).

The [MyST Markdown guide](https://mystmd.org/guide) is the best reference for learning what directives and components are available. For Typst customization, the [Typst documentation](https://typst.app/docs) and the [modern-cv](https://typst.app/universe/package/modern-cv/) package page are good starting points.

If you build a site using this template, feel free to share it on social media. I would love to see what you create!
