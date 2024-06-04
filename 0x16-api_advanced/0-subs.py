#!/usr/bin/python3
""" script send HTTP request to reddit API"""

import requests


def number_of_subscribers(subreddit):
    """
    GET number of subscriber of give subreddit

    Args:
    subreddit (str): subreddit to return the number of subscribers
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=user_agent, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
