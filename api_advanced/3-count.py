#!/usr/bin/python3
"""Module documentation"""

import requests


def count_words(subreddit, word_list, after='', word_counts=None):
    if word_counts is None:
        word_counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        after = data['data']['after']

        for post in data['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                if f" {word.lower()} " in f" {title} ":
                    if word not in word_counts:
                        word_counts[word] = 1
                    else:
                        word_counts[word] += 1

        if after is not None:
            count_words(subreddit, word_list, after, word_counts)
        else:
            sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0].lower()))
            for word, count in sorted_counts:
                print(f"{word.lower()}: {count}")


# Example usage
subreddit = 'unpopular'
keywords = ['down', 'vote', 'downvote', 'you', 'her', 'unpopular', 'politics']
count_words(subreddit, keywords)

