#!/usr/bin/python3

"""
    Consume an API https://jsonplaceholder.typicode.com/todos/1
"""

import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    url = url + "/" + userId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    total_tasks = response.json()
    completed = 0
    completed_tasks = []

    for task in total_tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, completed, len(total_tasks)))

    for completed_task in completed_tasks:
        print("\t {}".format(completed_task.get('title')))