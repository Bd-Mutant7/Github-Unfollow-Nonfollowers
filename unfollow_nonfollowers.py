#!/usr/bin/env python3
"""
GitHub Unfollow Non-Followers
==============================
Unfollows GitHub users who are not following you back.
Uses the official GitHub REST API with Personal Access Token auth.

Setup:
  pip install requests

Usage:
  python unfollow_nonfollowers.py

You will be prompted for your GitHub username and a Personal Access Token.
Generate a token at: https://github.com/settings/tokens
Required scopes: user:follow (to read followers/following and unfollow)
"""

import requests
import time
import sys

# ── Config ──────────────────────────────────────────────────────────────────
BASE_URL = "https://api.github.com"
PER_PAGE = 100          # max allowed by GitHub API
RATE_LIMIT_PAUSE = 0.5  # seconds between API calls to be polite


# ── Helpers ──────────────────────────────────────────────────────────────────

def get_session(token: str) -> requests.Session:
    """Return an authenticated requests session."""
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    return session


def paginate(session: requests.Session, url: str) -> list[dict]:
    """
    Fetch all pages from a paginated GitHub API endpoint.
    Returns the combined list of items.
    """
    results = []
    page = 1
    while True:
        resp = session.get(url, params={"per_page": PER_PAGE, "page": page})
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        results.extend(data)
        # If fewer results than requested, we've hit the last page
        if len(data) < PER_PAGE:
            break
        page += 1
        time.sleep(RATE_LIMIT_PAUSE)
    return results


def get_followers(session: requests.Session, username: str) -> set[str]:
    """Return set of logins who follow the given user."""
    url = f"{BASE_URL}/users/{username}/followers"
    users = paginate(session, url)
    return {u["login"] for u in users}


def get_following(session: requests.Session, username: str) -> set[str]:
    """Return set of logins the given user is following."""
    url = f"{BASE_URL}/users/{username}/following"
    users = paginate(session, url)
    return {u["login"] for u in users}


def unfollow(session: requests.Session, username: str) -> bool:
    """
    Unfollow a single user.
    Returns True on success, False otherwise.
    """
    url = f"{BASE_URL}/user/following/{username}"
    resp = session.delete(url)
    time.sleep(RATE_LIMIT_PAUSE)
    return resp.status_code == 204


def check_rate_limit(session: requests.Session) -> None:
    """Print current API rate limit status."""
    resp = session.get(f"{BASE_URL}/rate_limit")
    if resp.ok:
        core = resp.json()["resources"]["core"]
        remaining = core["remaining"]
        limit = core["limit"]
        reset_ts = core["reset"]
        reset_time = time.strftime("%H:%M:%S", time.localtime(reset_ts))
        print(f"  API rate limit: {remaining}/{limit} requests remaining (resets at {reset_time})")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 55)
    print("   GitHub Unfollow Non-Followers")
    print("=" * 55)

    # Prompt for credentials
    username = input("\nEnter your GitHub username: ").strip()
    if not username:
        print("Error: username cannot be empty.")
        sys.exit(1)

    token = input("Enter your GitHub Personal Access Token: ").strip()
    if not token:
        print("Error: token cannot be empty.")
        sys.exit(1)

    session = get_session(token)

    # Verify credentials
    print("\nVerifying credentials…")
    me = session.get(f"{BASE_URL}/user")
    if me.status_code == 401:
        print("Error: Invalid token. Please check your Personal Access Token.")
        sys.exit(1)
    me.raise_for_status()
    verified_username = me.json()["login"]
    print(f"  Authenticated as: {verified_username}")

    if verified_username.lower() != username.lower():
        print(f"  Warning: token owner '{verified_username}' differs from entered username '{username}'.")
        print(f"  Using token owner '{verified_username}' for unfollow operations.")
        username = verified_username

    check_rate_limit(session)

    # Fetch followers and following
    print(f"\nFetching followers of @{username}…")
    followers = get_followers(session, username)
    print(f"  → {len(followers)} followers found.")

    print(f"\nFetching accounts @{username} is following…")
    following = get_following(session, username)
    print(f"  → Following {len(following)} accounts.")

    # Find non-followers (people you follow who don't follow back)
    non_followers = following - followers
    print(f"\nAccounts not following you back: {len(non_followers)}")

    if not non_followers:
        print("\nEveryone you follow also follows you back. Nothing to do!")
        sys.exit(0)

    # List them
    print("\nUsers to unfollow:")
    for i, user in enumerate(sorted(non_followers), 1):
        print(f"  {i:>4}. {user}")

    # Confirm before acting
    print()
    answer = input(f"Unfollow all {len(non_followers)} users? [yes/no]: ").strip().lower()
    if answer not in ("yes", "y"):
        print("Aborted. No users were unfollowed.")
        sys.exit(0)

    # Unfollow loop
    print()
    success_count = 0
    fail_count = 0
    failed_users = []

    for i, user in enumerate(sorted(non_followers), 1):
        print(f"  [{i}/{len(non_followers)}] Unfollowing @{user}… ", end="", flush=True)
        if unfollow(session, user):
            print("✓")
            success_count += 1
        else:
            print("✗ (failed)")
            fail_count += 1
            failed_users.append(user)

    # Summary
    print("\n" + "=" * 55)
    print("  Done!")
    print(f"  Successfully unfollowed : {success_count}")
    print(f"  Failed                  : {fail_count}")
    if failed_users:
        print(f"  Failed users            : {', '.join(failed_users)}")
    print("=" * 55)


if __name__ == "__main__":
    main()
