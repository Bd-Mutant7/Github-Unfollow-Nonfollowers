# Contributing to GitHub Unfollow Non-Followers

First off, thank you for considering contributing! 🎉

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list to see if the problem has already been reported. When you create a bug report, include as many details as possible:

- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Provide specific examples (commands run, error messages)
- Describe the behavior you observed vs what you expected

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- Use a clear and descriptive title
- Provide a step-by-step description of the suggested enhancement
- Explain why this enhancement would be useful

### Pull Requests

1. Fork the repo and create your branch from `main`
2. Install development dependencies: `pip install -r requirements-dev.txt`
3. Make your changes
4. Test your changes thoroughly
5. Update documentation if needed
6. Submit the pull request!

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/your-username/github-unfollow-nonfollowers.git
cd github-unfollow-nonfollowers
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

4. Create your **.env** file:

```bash
cp .env.example .env
# Edit .env with your credentials
```

## Style Guidelines

- Follow **PEP 8** guidelines.
- Use **descriptive variable names**.
- Add **docstrings** for functions and classes.
- Keep **functions focused and small**.

## Testing
Run tests before submitting
```bash
python -m pytest tests/
```

**Thank you for contributing! 🚀**
