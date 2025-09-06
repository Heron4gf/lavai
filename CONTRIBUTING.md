# Contributing to Lavai

Thank you for your interest in contributing to Lavai! This document provides guidelines and instructions for contributing to this project.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Code Style](#code-style)
- [Release Process](#release-process)

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We expect all contributors to adhere to a professional and inclusive attitude.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/lavai.git
   cd lavai
   ```
3. Add the original repository as a remote:
   ```bash
   git remote add upstream https://github.com/Heron4gf/lavai.git
   ```

## Development Setup

1. Ensure you have Python 3.7+ installed
2. Install the package in development mode:
   ```bash
   pip install -e .
   ```
3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

Note: Currently, there are no explicit development dependencies specified. You may need to install testing tools manually:
```bash
pip install pytest pytest-cov black flake8
```

## Project Structure

```
lavai/
├── __init__.py      # Package initialization and main API
├── __main__.py      # Entry point for CLI
├── cli.py           # Click-based command line interface
├── client.py        # Client implementation for AI providers
├── credentials.py   # Credential storage management
├── responses.py     # Response handling utilities
```

## Making Changes

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

2. Make your changes following the code style guidelines

3. Add tests for your changes (if applicable)

4. Ensure all tests pass

5. Update documentation if needed

## Testing

While the project currently doesn't have extensive test coverage, we encourage adding tests for new features. To run tests:

```bash
pytest
```

If you add new functionality, please include appropriate tests. The project uses pytest for testing.

## Submitting Changes

1. Commit your changes with descriptive commit messages:
   ```bash
   git commit -m "feat: add support for new AI provider"
   # or
   git commit -m "fix: resolve credential storage issue"
   ```

2. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Create a Pull Request (PR) on GitHub from your branch to the main repository's main branch

4. Fill out the PR template with:
   - Description of changes
   - Related issues (if any)
   - Testing performed
   - Screenshots (if UI changes)

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Include docstrings for public functions and classes
- Keep functions focused and single-purpose
- Use type hints where appropriate

We recommend using black for code formatting:
```bash
black lavai/ *.py
```

And flake8 for linting:
```bash
flake8 lavai/ *.py
```

## Release Process

Releases are automatically published to PyPI when a new GitHub release is created. The workflow includes:

1. Building the package
2. Running tests
3. Publishing to PyPI

To prepare for a release:
- Update version in `setup.py`
- Update CHANGELOG.md (if available)
- Ensure all tests pass
- Create a GitHub release with release notes

## Questions?

If you have questions about contributing, please open an issue on GitHub or contact the maintainers.

Thank you for contributing to Lavai!