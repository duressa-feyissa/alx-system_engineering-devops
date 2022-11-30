#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """ A function that queries the Reddit API parses the title of
    all hot articles, and prints a sorted count of given keywords
    """

    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0
    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    p = {'limit': 100, 'after': after}
    res = requests.get(url, headers=header, params=p, allow_redirects=False)
    if res.status_code != 200:
        return None
    try:
        hot = res.json()['data']['children']
        aft = res.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)
    except Exception:
        return None
    count_words(subreddit, word_list, aft, word_dict)
