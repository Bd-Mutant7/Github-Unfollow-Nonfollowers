<div align="center">

# GitHub Unfollow Non-Followers

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A Python script that uses the GitHub API to automatically unfollow users who don't follow you back.

</div>

## Features

- Fetches your followers and following lists
- Identifies users you follow who don't follow you back
- Option to automatically unfollow or preview before unfollowing
- Rate limit handling
- Progress tracking

## Prerequisites

- Python 3.6 or higher
- GitHub Personal Access Token

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/github-unfollow-nonfollowers.git
cd github-unfollow-nonfollowers
```
2. Install dependencies:
```markdown
pip install -r requirements.txt
```

## Create a GitHub Personal Access Token

3  Go to **GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)**.
4.  Click **Generate new token**.
5. Select the required scopes:
   - `read:user`
   - `user:follow`
6. Copy the generated token.

## Configure the Token

You can configure the token in one of the following ways:

### Option 1: Edit `config.py`

Add your GitHub username and token:

```python
GITHUB_USERNAME = "your_username"
GITHUB_TOKEN = "your_personal_access_token"
```
## Usage
Run the script
```bash
python unfollow_nonfollowers.py
```

By default, the script will only show who would be unfollowed. To actually unfollow, use:
```bash
python unfollow_nonfollowers.py --unfollow
```

## Options

- `--unfollow`  
  Actually perform the unfollow actions.

- `--preview`  
  Preview who would be unfollowed (default).

- `--help`  
  Show the help message.

  ## Example Output
  
  ```text
  Fetching followers...
   Found 150 followers
   Fetching following...
   Following 200 users

   Analyzing...
   You are following 50 users who don't follow you back:

  Users to unfollow:
   - user1 (https://github.com/user1)
   - user2 (https://github.com/user2)
   - user3 (https://github.com/user3)

   Run with --unfollow to unfollow these users



## Development

Want to contribute? Great! Check out our [contributing guidelines](CONTRIBUTING.md).

### Quick Setup for Development

```bash
# Clone your fork
git clone https://github.com/your-username/github-unfollow-nonfollowers.git
cd github-unfollow-nonfollowers

# Set up development environment
make install
cp .env.example .env
# Edit .env with your credentials

# Run tests
make test

# Format code
make format
```

## Security

Please report security issues **privately** via GitHub's [security advisory](https://docs.github.com/en/code-security/security-advisories) feature.

## Star History

If you find this useful, please consider giving it a star! ⭐

