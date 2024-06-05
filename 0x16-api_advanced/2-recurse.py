#!/usr/bin/python3
""" queries reddit API"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    returning top 10 post of subreddit recursively

    Args:
    subreddit (str): subreddit to query
    hot_list (list): list of top ten titles
    """
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    param = {'after': after}

    results = requests.get(url, params=param, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)

        titles = results.json().get("data").get("children")
        for title in titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
