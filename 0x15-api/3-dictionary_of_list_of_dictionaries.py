#!/usr/bin/python3
"""
Exports all tasks in the JSON format.
"""
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()

    data = {}
    for user in users:
        user_id = str(user.get('id'))
        data[user_id] = []

        user_tasks = requests.get(url + user_id + '/todos').json()
        for task in user_tasks:
            task_data = {}
            task_data['task'] = task.get('title')
            task_data['completed'] = task.get('completed')
            task_data['username'] = user.get('username')
            data[user_id].append(task_data)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)
