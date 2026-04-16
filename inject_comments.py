#!/usr/bin/env python3
"""Inject Giscus comment widget into blog post HTML files after MyST build.

Before using this script, set up Giscus for your repository:
1. Visit https://giscus.app to configure Giscus
2. Update the data-repo, data-repo-id, data-category, and data-category-id below
3. Enable GitHub Discussions on your repository

Usage: python inject_comments.py
"""

from pathlib import Path

LIGHT_THEME_FILE = "giscus-light.css"

# TODO: Update these values with your Giscus configuration from https://giscus.app
GISCUS_SNIPPET = """
<script>
(function() {
  function getSiteTheme() {
    var root = document.documentElement;
    if (root.classList.contains('dark')) {
      return 'dark';
    }
    if (root.classList.contains('light')) {
      return 'light';
    }

    var savedTheme = localStorage.getItem('myst:theme');
    if (savedTheme === 'dark' || savedTheme === 'light') {
      return savedTheme;
    }

    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function getSiteRootUrl() {
    var marker = '/posts/';
    var pathname = window.location.pathname;
    var markerIndex = pathname.indexOf(marker);
    var rootPath = markerIndex === -1 ? '/' : pathname.slice(0, markerIndex + 1);
    return window.location.origin + rootPath;
  }

  function getGiscusTheme() {
    if (getSiteTheme() === 'dark') {
      return 'dark';
    }
    return getSiteRootUrl() + 'giscus-light.css';
  }

  function syncGiscusTheme() {
    var iframe = document.querySelector('iframe.giscus-frame');
    if (!iframe || !iframe.contentWindow) return false;

    iframe.contentWindow.postMessage(
      { giscus: { setConfig: { theme: getGiscusTheme() } } },
      'https://giscus.app'
    );
    return true;
  }

  function waitForGiscusFrame() {
    var attempts = 0;
    var timer = setInterval(function() {
      attempts++;
      if (syncGiscusTheme() || attempts > 60) {
        clearInterval(timer);
      }
    }, 250);
  }

  function initGiscus() {
    // Find the article content area to append comments inside it
    var article = document.querySelector('article') || document.querySelector('main');
    if (!article) return false;

    // Don't duplicate
    if (document.getElementById('giscus-comments')) return true;

    var container = document.createElement('div');
    container.id = 'giscus-comments';
    container.style.cssText = 'margin: 2rem 0; color: var(--color-text, inherit);';
    container.innerHTML = '<h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: inherit;">Comments</h2>';
    article.appendChild(container);

    var s = document.createElement('script');
    s.src = 'https://giscus.app/client.js';
    s.setAttribute('data-repo', 'opengeos/myst-website-template');           // TODO: Update
    s.setAttribute('data-repo-id', 'REPLACE_WITH_REPO_ID');         // TODO: Update
    s.setAttribute('data-category', 'General');              // TODO: Update
    s.setAttribute('data-category-id', 'REPLACE_WITH_CATEGORY_ID');   // TODO: Update
    s.setAttribute('data-mapping', 'pathname');
    s.setAttribute('data-strict', '0');
    s.setAttribute('data-reactions-enabled', '1');
    s.setAttribute('data-emit-metadata', '0');
    s.setAttribute('data-input-position', 'bottom');
    s.setAttribute('data-theme', getGiscusTheme());
    s.setAttribute('data-lang', 'en');
    s.setAttribute('crossorigin', 'anonymous');
    s.async = true;
    container.appendChild(s);
    waitForGiscusFrame();
    return true;
  }

  // Retry until React has finished rendering the article content
  function tryInit() {
    var attempts = 0;
    var timer = setInterval(function() {
      attempts++;
      if (initGiscus() || attempts > 100) clearInterval(timer);
    }, 300);
  }
  tryInit();

  // Re-initialize on SPA navigation (MyST book theme uses client-side routing)
  var lastUrl = location.href;
  var navObserver = new MutationObserver(function() {
    if (location.href !== lastUrl) {
      lastUrl = location.href;
      // Only init on post pages
      if (location.pathname.indexOf('/posts/') !== -1) {
        tryInit();
      }
    }
  });
  navObserver.observe(document.body, { childList: true, subtree: true });

  // Update Giscus theme when the site theme toggles
  var themeObserver = new MutationObserver(function() {
    syncGiscusTheme();
  });
  themeObserver.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
})();
</script>
"""


def copy_theme_asset(build_dir: Path) -> None:
    """Copy the custom light theme into the built site."""
    source = Path(__file__).parent / LIGHT_THEME_FILE
    target = build_dir / LIGHT_THEME_FILE

    if not source.exists():
        print(f"Theme file not found: {source}")
        return

    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Copied {LIGHT_THEME_FILE} to {target}")


def main():
    """Inject Giscus comments into blog post HTML files."""
    build_dir = Path(__file__).parent / "_build" / "html"
    blog_dir = build_dir / "posts"

    if not build_dir.exists():
        print(f"No build directory found at {build_dir}")
        return

    copy_theme_asset(build_dir)

    if not blog_dir.exists():
        print(f"No blog directory found at {blog_dir}")
        return

    count = 0
    for html_file in blog_dir.rglob("*.html"):
        content = html_file.read_text(encoding="utf-8")
        if "giscus-comments" in content:
            continue
        # Insert before closing </body> tag
        if "</body>" in content:
            content = content.replace("</body>", f"{GISCUS_SNIPPET}\n</body>")
            html_file.write_text(content, encoding="utf-8")
            count += 1
            print(f"Injected comments into {html_file.name}")

    print(f"Done. Injected comments into {count} file(s).")


if __name__ == "__main__":
    main()
