#!/usr/bin/python3
'''
    Consume an API https://jsonplaceholder.typicode.com/
    And save the results in a JSON
'''
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    url = url + "/" + user_id

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    dict = {user_id: []}
    for task in tasks:
        dict[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open(f'{user_id}.json', 'w') as filename:
        json.dump(dict, filename)
