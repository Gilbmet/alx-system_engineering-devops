#!/usr/bin/python3

import requests
import sys

if len(sys.argv) < 2:
    print("Please provide an employee ID")
    sys.exit(1)

employee_id = int(sys.argv[1])
url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

response = requests.get(url)

if response.status_code != 200:
    print("Error retrieving TODO list")
    sys.exit(1)

todos = response.json()
total_tasks = len(todos)
completed_tasks = sum(1 for todo in todos if todo['completed'])

employee_name = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()['name']

print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

for todo in todos:
    if todo['completed']:
        print("\t {}".format(todo['title']))
