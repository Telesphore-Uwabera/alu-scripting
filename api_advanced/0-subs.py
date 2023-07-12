#!/usr/bin/python3

"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
If the subreddit is invalid, returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent header

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    else:
        return 0
#!/usr/bin/python3

"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
If the subreddit is invalid, returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent header

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    else:
        return 0

