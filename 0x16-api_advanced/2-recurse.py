#!/usr/bin/python3
""" Query the Reddit API using recursive function """
import requests


after = None


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves posts from the hot section of a subreddit.

    Args:
    - subreddit (str): The name of the subreddit.
    - hot_list (list): A list to store post titles. Default is an empty list.

    Returns:
    - list: A list containing post titles if successful, otherwise None.
    """
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            recurse(subreddit, hot_list, after=next_)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return None
