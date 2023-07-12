#!/usr/bin/python3

"""
0-subs

Queries the Reddit API and returns the number of subscribers for a given subreddit.
If not a valid subreddit, return 0.

Author: Telesphore Uwabera
Date: July 12, 2023
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If not a valid subreddit, return 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit.
            Returns 0 if the subreddit is invalid or an error occurs.

    Raises:
        None

    Example Usage:
        >>> number_of_subscribers('programming')
        756024
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Set a custom User-Agent header

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
