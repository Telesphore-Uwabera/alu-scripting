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

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent header

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    else:
        return 0
