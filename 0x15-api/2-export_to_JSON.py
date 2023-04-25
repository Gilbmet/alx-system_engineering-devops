#!/usr/bin/python3
"""Export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(user_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id)).json()

    tasks = []
    for task in todos:
        tasks.append({'task': task.get('title'),
                      'completed': task.get('completed'),
                      'username': users.get('username')})

    with open('{}.json'.format(user_id), mode='w') as file:
        json.dump({user_id: tasks}, file)
