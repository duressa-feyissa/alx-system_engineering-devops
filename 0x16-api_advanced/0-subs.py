#!/usr/bin/python3
""" Number of subs"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of susbs of reddit """
    if subreddit is None:
        return (0)
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    x = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; /rv:107.0) "
    x += "Gecko/20100101 Firefox/107.0"
    headers = {"user-agent": x}
    r = requests.get(url, headers=headers).json()
    subscribers = r.get("data", {}).get("subscribers", 0)
    return subscribers
