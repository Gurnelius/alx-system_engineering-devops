#!/usr/bin/python3
""" recursive function that queries the Reddit API"""
import requests
import sys


after = None
count_dic = []


def count_words(subreddit, word_list):
    """
    Counts occurrences of words from a word list in the titles
    of posts from a subreddit.

    Args:
    - subreddit (str): The name of the subreddit.
    - word_list (list): A list of words to search for in post titles.
    Returns:
    - dict: A dictionary containing word counts if successful, otherwise None.
    """
    if count_dic is None:
        count_dic = {}
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)
    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            count_words(subreddit, word_list, after=next_, count_dic=count_dic)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            title = title_.get('data').get('title')
            for word in word_list:
                if word in title:
                    count_dic[word] = count_dic.get(word, 0) + 1
        return count_dic
    else:
        return None
