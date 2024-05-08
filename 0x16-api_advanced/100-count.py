#!/usr/bin/python3
""" recursive function that queries the Reddit API"""
import requests

after = None
count_dic = []


import requests

def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    This function recursively queries the Reddit API, parses hot article titles,
    and prints a sorted count of keywords (case-insensitive).

    Args:
        subreddit: The name of the subreddit.
        word_list: A list of keywords to count.
        after: An optional parameter for pagination (Reddit API after parameter).
        word_counts: A dictionary to store keyword counts (used internally during recursion).
    """

    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'My Reddit Keyword Counter v1.0'}

    # Construct the API URL with after parameter for pagination (if provided)
    url = f"https://reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    try:
        # Send a GET request without following redirects
        response = requests.get(url, allow_redirects=False, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Parse the JSON response
        data = response.json()

        # Check for valid data and data key
        if not data.get('data'):
            return

        # Initialize word counts dictionary if not provided
        if not word_counts:
            word_counts = {word.lower(): 0 for word in word_list}

        # Extract keywords from titles (case-insensitive, split by delimiters)
        for post in data['data']['children']:
            title = post['data']['title'].lower().split()
            for word in word_list:
                clean_word = word.lower().strip("!._-")
                word_counts[word] += sum(clean_word == w for w in title)

        # Check for next page and make recursive call if available
        after = data['data'].get('after')
        if after:
            count_words(subreddit, word_list, after, word_counts.copy())

    except requests.exceptions.RequestException:
        # Handle request exceptions
        return

    # Filter keywords with zero count and sort by count (descending) then alphabetically (ascending)
    filtered_counts = {word: count for word, count in word_counts.items() if count > 0}
    sorted_counts = sorted(filtered_counts.items(), key=lambda item: (-item[1], item[0]))

    # Print the sorted keyword counts
    if sorted_counts:
        for word, count in sorted_counts:
            print(f"{word}: {count}")
