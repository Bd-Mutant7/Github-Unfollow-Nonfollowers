# GitHub Unfollow Non-Followers

A simple Python script that uses the **GitHub REST API** to automatically unfollow anyone who isn't following you back.


[![Support](https://img.shields.io/badge/Support-Paystack-00C3F7?style=for-the-badge&logo=paypal&logoColor=white)](https://paystack.shop/pay/bd-mutant7)

---

## Features

- Authenticates securely via a Personal Access Token
- Handles pagination — works even if you follow thousands of people
- Lists every user it plans to unfollow before doing anything
- Asks for confirmation before making any changes
- Rate-limit friendly — won't get you blocked by GitHub's API
- Prints a full success/failure summary when done

---

## Requirements

- Python 3.10+
- A GitHub account
- A GitHub Personal Access Token with the `user:follow` scope

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/Bd-Mutant7/github-unfollow-nonfollowers.git
cd github-unfollow-nonfollowers
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Generate a GitHub Personal Access Token**

Go to [github.com/settings/tokens](https://github.com/settings/tokens) and create a new token with the **`user:follow`** scope enabled. Copy the token — you won't be able to see it again.

---

## Usage

```bash
python unfollow_nonfollowers.py
```

You will be prompted to enter:
- Your GitHub username
- Your Personal Access Token

The script will then:
1. Fetch your full followers list
2. Fetch everyone you're following
3. Compute who isn't following you back
4. Show you the list and ask for confirmation
5. Unfollow them one by one and print a final summary

---

## Example Output

```
=======================================================
   GitHub Unfollow Non-Followers
=======================================================

Enter your GitHub username: Bd-Mutant7
Enter your GitHub Personal Access Token: ••••••••••••••••

Verifying credentials…
  Authenticated as: Bd-Mutant7
  API rate limit: 4998/5000 requests remaining (resets at 14:32:00)

Fetching followers of @Bd-Mutant7…
  → 142 followers found.

Fetching accounts @Bd-Mutant7 is following…
  → Following 200 accounts.

Accounts not following you back: 58

Users to unfollow:
     1. alice123
     2. bob_dev
     ...

Unfollow all 58 users? [yes/no]: yes

  [1/58] Unfollowing @alice123… ✓
  [2/58] Unfollowing @bob_dev… ✓
  ...

=======================================================
  Done!
  Successfully unfollowed : 58
  Failed                  : 0
=======================================================
```

---

## Notes

- Your token is never stored — it's only held in memory for the duration of the script.
- GitHub's API allows up to **5,000 requests per hour** for authenticated users. The script is well within those limits for typical use.
- You can safely re-run the script at any time — it only unfollows, never follows.

---

## License

MIT
