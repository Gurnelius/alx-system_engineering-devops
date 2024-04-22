#!/usr/bin/python3

"""
    Consume an API https://jsonplaceholder.typicode.com/todos/1
"""

import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        total_tasks = 0
        completed_tasks = 0
        tasks_titles = ""
        for task in json:
            if task.get("userId") == int(id):
                total_tasks += 1
                tasks_titles += "\t" + task.get("title") + "\n"
                if task.get("completed"):
                    completed_tasks += 1
        tasks_titles = tasks_titles.rstrip()
        print("Employee {} is done with tasks({}/{}):".format(id, completed_tasks, total_tasks))
        print(tasks_titles)