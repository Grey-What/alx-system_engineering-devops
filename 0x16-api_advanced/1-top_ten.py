#!/usr/bin/python3
""" queries reddit API"""

import requests


def top_ten(subreddit):
    """
    send GET request to reddit API and print titles of top ten hot post
    of the given subreddit

    Args:
    subreddit (str): name of subreddit to query
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    try:
        response = get(url, headers=user_agents, params={'limit': 10})
        result = response.json()

        content = result.get('data').get('children')

        for post in content:
            print(post.get('data').get('title'))

    except Exception:
        print("None")
