#!/usr/bin/python3
"""
    Consume an API https://jsonplaceholder.typicode.com/todos/
    And save the results in a CSV
"""

import requests
import sys

if __name__ == '__main__':
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    url = url + "/" + userId

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    with open('{}.csv'.format(userId), 'w') as file:
        for task in tasks:
            file.write(
                '"{}","{}","{}","{}"\n'
                .format(userId, username, task.get('completed'),
                        task.get('title'))
                )
