# Contributing

Thank you for your interest in contributing to this book project!

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-contribution`)
3. Make your changes
4. Run `pre-commit run --all-files` to ensure code quality
5. Commit your changes (`git commit -m 'Add my contribution'`)
6. Push to the branch (`git push origin feature/my-contribution`)
7. Open a Pull Request

## Development Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Install pre-commit hooks: `pre-commit install`

## Building the Book

### HTML (for web)

```bash
myst build --html
```

### PDF and EPUB (via Typst)

```bash
python build_translation.py en
```

## Code Style

- Python code follows [Black](https://black.readthedocs.io/) formatting
- Markdown files use [MyST Markdown](https://mystmd.org/) syntax
- All code is spell-checked with [codespell](https://github.com/codespell-project/codespell)

## Reporting Issues

Please use the GitHub issue tracker to report bugs or suggest features.
