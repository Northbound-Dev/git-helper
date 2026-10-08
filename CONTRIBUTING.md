# Contributing to git-helper

Thank you for considering contributing to git-helper! We welcome contributions from the community.

## How to Contribute

### Reporting Issues
Please use the GitHub issue tracker to report bugs or suggest features. When reporting issues, please include:
- A clear and descriptive title
- Steps to reproduce the issue (if applicable)
- Expected vs actual behavior
- Your environment (Python version, OS, etc.)

### Suggesting Enhancements
Feature requests are welcome! Please provide:
- A clear description of the feature
- Why it would be useful to users
- Any potential implementation considerations

### Making Code Contributions

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/git-helper.git
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** following the coding standards below
5. **Add tests** for new functionality
6. **Run the tests** to ensure everything works:
   ```bash
   python -m pytest tests/
   ```
7. **Commit your changes** with a clear message
8. **Push to your fork** and submit a pull request

## Coding Standards

- Follow [PEP 8](https://pep8.org/) for Python code style
- Write clear, descriptive docstrings for all public functions and classes
- Add type hints where possible
- Keep functions focused and single-purpose
- Write tests for new functionality

## Development Setup

1. Install development dependencies:
   ```bash
   pip install -e .[dev]
   ```
   (Note: We'll add dev dependencies in pyproject.toml as the project grows)

2. Run the test suite:
   ```bash
   python -m pytest tests/
   ```

## Issue Categories for Contribution Waves

We organize issues by difficulty to help contributors find appropriate tasks:

### 🟢 Trivial (Good for first-time contributors)
- Typos and documentation improvements
- Small bug fixes
- Help text enhancements
- Minor UI/UX improvements in CLI output

### 🟡 Medium 
- New feature implementations
- Refactoring existing code
- Adding new CLI command options
- Improving error handling
- Adding test coverage for existing features

### 🔴 High
- Major architectural changes
- Complex algorithm implementations
- Significant performance optimizations
- Major refactoring of core components
- Adding support for new platforms/environments

## Getting Help

If you have questions during your contribution process:
- Check existing issues to see if similar questions have been asked
- Feel free to ask for clarification in issue comments
- Maintainers are happy to help guide contributors

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

Thank you again for contributing to git-helper!
