#!/usr/bin/python3

"""
0-subs

Queries the Reddit API and returns the number of subscribers for a given subreddit.
If not a valid subreddit, return 0.

Author: Your Name
Date: July 12, 2023
"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Set a custom User-Agent header
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)

