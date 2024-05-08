#!/usr/bin/python3
""" Query the Reddit API """
import requests
import sys


def top_ten(subreddit):
    """
    Retrieves the top ten posts from a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.

    Returns:
    - None
    """
    headers = {'User-Agent': 'Firelite v3.3.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
