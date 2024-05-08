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
    headers = {'User-Agent': 'Firelight emulator v3.34'}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json = response.json()
        try:
            if 'error' in json.keys():
                return 0
            else:
                return json['data']['subscribers']
        except Exception as e:
            return 0
    return 0
