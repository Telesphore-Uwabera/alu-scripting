#!/usr/bin/python3
"""Module documentation"""

import json
import requests


def count_words(subreddit, word_list, after='', hot_list=None):
    if hot_list is None:
        hot_list = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url, params={'after': after},
                           allow_redirects=False,
                           headers={'User-Agent': 'My User Agent 1.0'})

    if request.status_code == 200:
        data = request.json()

        for topic in data['data']['children']:
            title_words = topic['data']['title'].split()
            for word in title_words:
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        hot_list[i] += 1

        after = data['data']['after']
        if after is None:
            word_counts = {}
            for i, word in enumerate(word_list):
                if i not in word_counts:
                    word_counts[i] = hot_list[i]
                else:
                    word_counts[i] += hot_list[i]

            sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], word_list[x[0]].lower()))

            for i, count in sorted_counts:
                if count > 0:
                    print("{}: {}".format(word_list[i].lower(), count))
        else:
            count_words(subreddit, word_list, after, hot_list)
