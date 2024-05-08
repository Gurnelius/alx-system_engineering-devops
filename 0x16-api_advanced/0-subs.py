#!/usr/bin/python3
"""
Query the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: The number of subscribers if successful, otherwise 0.
    """
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers", 0)
    return 0
