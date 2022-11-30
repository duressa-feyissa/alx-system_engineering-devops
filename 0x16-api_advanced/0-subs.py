#!/usr/bin/python3
""" Number of subs"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of susbs of reddit """
    if subreddit is None:
        return (0)
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": 'API Project by andreshugueth'}
    r = requests.get(url, headers=headers).json()
    subscribers = r.get("data", {}).get("subscribers", 0)
    return subscribers
