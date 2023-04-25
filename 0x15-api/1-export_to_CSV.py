#!/usr/bin/python3
"""
Exports data in the CSV format for a given employee ID,
using data from the JSONPlaceholder API.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(user_url)
    user_data = response.json()
    username = user_data.get('username')

    tasks_url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(tasks_url)
    tasks_data = response.json()

    filename = user_id + '.csv'
    with open(filename, mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks_data:
            if task.get('userId') == int(user_id):
                row = [
                    user_id,
                    username,
                    str(task.get('completed')),
                    task.get('title')
                ]
                writer.writerow(row)
