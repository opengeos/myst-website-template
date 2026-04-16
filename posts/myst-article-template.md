---
title: "Write Journal Articles with MyST Markdown: Auto-Generate PDFs and Websites"
date: 2026-04-15
authors:
  - name: Qiusheng Wu
    email: qwu18@utk.edu
    orcid: 0000-0001-5437-4073
    url: https://gishub.org
description: A step-by-step tutorial on writing journal articles in MyST Markdown with automatic PDF generation and website deployment using a GitHub template.
thumbnail: https://img.youtube.com/vi/iwL-s7aPNYQ/maxresdefault.jpg
tags:
  - MyST Markdown
  - GitHub Pages
  - Tutorial
  - PDF
  - Academic Writing
keywords:
  - MyST Markdown
  - GitHub Pages
  - Tutorial
  - PDF
  - Academic Writing
  - Journal Articles
  - Jupytext
---

# Write Journal Articles with MyST Markdown: Auto-Generate PDFs and Websites

Writing journal articles usually means choosing between tools that are easy to use and tools that produce professional output. Google Docs and Microsoft Word are simple but give you limited control over formatting and make collaboration through version control difficult. LaTeX produces beautiful PDFs but has a steep learning curve. What if you could write in plain Markdown, push to GitHub, and get both a publication-quality PDF and an interactive website generated automatically? That is exactly what the [myst-article-template](https://github.com/opengeos/myst-article-template) provides.

In this tutorial, I walk through the entire workflow step by step: creating a repository from the template, editing your article content, managing citations, adding figures and tables, including executable code blocks, generating a PDF, and deploying everything as a website. The whole process takes just a few minutes to set up.

:::{iframe} https://www.youtube.com/embed/iwL-s7aPNYQ
:width: 100%
Video tutorial: Write Journal Articles with MyST Markdown
:::

## What You Will Need

- A [GitHub](https://github.com) account (free).
- For local editing and preview: a code editor like [VS Code](https://code.visualstudio.com) or [Cursor](https://cursor.com), [Node.js](https://nodejs.org) (version 18 or later), and Python 3.
- For local PDF compilation: the [Typst](https://typst.app) CLI (optional, since GitHub Actions handles this automatically).

## What the Template Produces

Before diving into the setup, here is what you get out of the box:

- **A publication-ready PDF** with title, authors, affiliations, section headings, figures, tables, code blocks, and a full reference list. You can view a [sample PDF](https://opengeos.org/myst-article-template/article.pdf) to see the output quality.
- **An interactive website** deployed to GitHub Pages with hover-to-preview citations, clickable cross-references, and expandable code blocks. See the [demo website](https://opengeos.org/myst-article-template) for a live example.

The PDF and the website are both generated from the same Markdown source. You write once and get both outputs automatically whenever you push changes to GitHub.

## Create Your Repository from the Template

1. Go to the [myst-article-template](https://github.com/opengeos/myst-article-template) repository on GitHub.
2. Click the green **Use this template** button in the upper right corner, then select **Create a new repository**.
3. Choose your GitHub account as the owner and give the repository a name, for example `my-article`.
4. Optionally add a description like "Repository for my journal article."
5. Click **Create repository** and wait a few seconds for GitHub to copy the template.

## Enable GitHub Pages

The first deployment will fail because GitHub Pages is not enabled by default. To fix that:

1. Go to your new repository's **Settings** tab.
2. In the left sidebar, click **Pages**.
3. Under **Build and deployment**, change the source to **GitHub Actions**.
4. Go back to the **Actions** tab. Click into the failed workflow run, then click **Re-run failed jobs** to trigger a fresh build.
5. After a minute or two, your site will be live at `https://username.github.io/repo-name`.

To make the URL easy to find, go to the repository's **About** section (gear icon on the main page), check **Use your GitHub Pages website**, and save.

## What GitHub Actions Does for You

Every time you push changes to the repository, the GitHub Actions workflow automatically:

1. Builds the HTML website with `myst build --html`.
2. Generates the article PDF.
3. Deploys everything to GitHub Pages.

The PDF is always available at a stable URL: `https://username.github.io/repo-name/article.pdf`. You can share this link directly, and it will always point to the latest version of your article.

## Clone and Edit Locally

Clone the repository to your local machine and open it in your editor:

```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Start the local development server to preview your article:

```bash
myst start
```

This launches a preview at `http://localhost:3000` (or a similar port). Changes to your Markdown files are reflected in the browser automatically. For a side-by-side editing experience, split your editor window and open the preview URL in the built-in browser panel. Every time you save a file, the preview updates instantly.

## Update Article Metadata

The article content lives primarily in `article.md`. Open this file and update the frontmatter at the top:

- **Title**: Update the article title. Note that the title is also referenced in `myst.yml`, so update it in both places to keep the PDF and website consistent.
- **Authors**: Replace the template author names with your own. Each author entry supports `name`, `email`, `affiliations`, and other fields.
- **Affiliations**: Update department, institution, city, and country.
- **Subtitle**: If your article has a subtitle, you can add it in `myst.yml` under the project configuration.

The author and affiliation information appears in the PDF header. The website pulls its metadata from the same source, so you only need to update it once.

## Manage Citations

MyST Markdown makes citation management straightforward. All references are stored in a `references.bib` file using standard BibTeX format.

### Add a New Reference

1. Find the article you want to cite on [Google Scholar](https://scholar.google.com) or your preferred source.
2. Click the **Cite** button, then select **BibTeX** to get the formatted entry.
3. Copy the BibTeX entry and paste it into `references.bib`.
4. Optionally add a `doi` field if one is available. Make sure each entry has a unique citation key (the identifier after `@article{`).

### Cite in Your Article

MyST supports two citation styles:

- **Parenthetical citation**: `[@article-id]` renders as (Author, Year).
- **Narrative citation**: `@article-id` renders as Author (Year).

On the website, citations are interactive. Hovering over a citation shows the full reference in a tooltip, and clicking it scrolls to the reference list. In the PDF, citations are hyperlinked to the bibliography section.

### Add a DOI

To include a DOI in your reference, add a `doi` field to the BibTeX entry in `references.bib`:

```bibtex
@article{wu2020geemap,
  title={geemap: A Python package for interactive mapping with Google Earth Engine},
  author={Wu, Qiusheng},
  journal={Journal of Open Source Software},
  year={2020},
  doi={10.21105/joss.02305}
}
```

Make sure to include only the DOI identifier (e.g., `10.21105/joss.02305`), not the full URL. Also ensure there is a comma after every field in the BibTeX entry, as a missing comma will cause a build error.

## Add Figures, Tables, and Code

### Tables

You can create tables using standard Markdown table syntax. The template also supports the three-line table format commonly used in academic publishing:

```markdown
:::{table} Overview of Methods
:label: tbl-methods

| Method | Accuracy | Speed |
|--------|----------|-------|
| Method A | 95.2% | Fast |
| Method B | 97.1% | Moderate |
| Method C | 93.8% | Fast |
:::
```

Tables are automatically numbered. To reference a table elsewhere in your article, use `` {numref}`tbl-methods` ``, which renders as "Table 1" (or whatever the sequential number is). You never need to manually track table numbers.

### Figures

Figures work similarly. Add an image with a label and caption:

```markdown
:::{figure} ./images/study-area.png
:label: fig-study-area
:alt: Map of the study area

Map showing the study area boundary and sample locations.
:::
```

Reference figures with `` {numref}`fig-study-area` `` to get automatic numbering. On the website, hovering over a figure reference shows a preview of the figure in a tooltip, which is especially useful when the figure is on a different page or section of a long article.

### Code Blocks

One of the most powerful features of MyST Markdown is support for executable code blocks. You can include source code that readers can view, and on the website, interact with:

````markdown
```{code-block} python
import geoai

m = geoai.Map()
m
```
````

Code blocks appear in both the PDF and the website. On the website, they are syntax-highlighted and can be expanded or collapsed. This is particularly valuable for research articles that include data analysis or visualization code, making your work fully reproducible.

## Generate the PDF Locally

You do not need to generate the PDF locally since GitHub Actions handles it on every push. But if you want to preview the PDF before pushing:

```bash
python build_pdf.py
```

This runs the build script and produces `article.pdf` in the project root. Open it to verify that your title, authors, affiliations, citations, figures, tables, and code blocks all render correctly.

## Convert Between Markdown and Jupyter Notebooks

If your article contains executable code, you may want to run it interactively in a Jupyter notebook. The template supports [Jupytext](https://jupytext.readthedocs.io), which converts between MyST Markdown and Jupyter notebook formats.

### Markdown to Notebook

Convert your article to a Jupyter notebook:

```bash
jupytext --to ipynb article.md
```

This creates `article.ipynb` with all your code cells ready to execute. Open it in Jupyter or VS Code, select a kernel, and run the cells to verify your code produces the expected output.

### Notebook to Markdown

After editing or running code in the notebook, sync changes back to Markdown:

```bash
jupytext --to myst article.ipynb
```

One thing to keep in mind: converting back to MyST Markdown can sometimes simplify the frontmatter. Use version control (`git diff`) to review the changes and make sure no metadata was lost. It is a good practice to commit your Markdown changes before converting to a notebook, so you can always restore the original frontmatter if needed.

## Deploy and Verify

Once you are happy with your changes, commit and push to GitHub. For small updates, you can push directly to the `main` branch:

```bash
git add .
git commit -m "Update article content"
git push
```

For larger changes, create a feature branch and open a pull request:

```bash
git checkout -b update-article
git add .
git commit -m "Update article content"
git push -u origin update-article
```

Then create a pull request on GitHub. The template includes pre-commit hooks that catch common issues like typos, trailing whitespace, and formatting problems. Once the pull request checks pass, merge it into `main` and the updated website and PDF will be deployed automatically.

After deployment, verify both outputs:

- **Website**: Visit `https://username.github.io/repo-name` and check that your content, citations, figures, and tables render correctly.
- **PDF**: Navigate to `https://username.github.io/repo-name/article.pdf` and confirm the layout, references, and formatting.

## Why This Approach Works

Because everything is stored as plain text Markdown in a GitHub repository, you get several advantages over traditional document editors:

- **Version control**: Every change is tracked. You can always go back to a previous version if something goes wrong, which is far more reliable than the revision history in Google Docs or keeping multiple copies of a Word document.
- **Collaboration**: Multiple authors can work on the same article using branches and pull requests, with clear diffs showing exactly what changed.
- **Reproducibility**: Executable code blocks mean readers (and reviewers) can verify your analysis directly from the article.
- **Accessibility**: The web version of your article is publicly accessible without requiring readers to download attachments.
- **Focus on content**: You write in Markdown and let the tooling handle layout, numbering, citation formatting, and PDF compilation.

## What is Next

This tutorial covers the complete workflow from template to deployed article with automatic PDF generation. If you are interested in building a personal academic website using the same technology stack, check out [Build a Personal Website in 5 Minutes: No Coding Required](./build-personal-website). For a website that also includes automatic CV generation, see [Build a Professional CV Website with Auto PDF Generation Using MyST Markdown](./myst-cv-website).

The [MyST Markdown guide](https://mystmd.org/guide) is the best reference for all available directives and components. For customizing the PDF output, the [Typst documentation](https://typst.app/docs) covers layout and typography options.

If you use this template for your next article, feel free to share it on social media. I would love to see what you publish!
