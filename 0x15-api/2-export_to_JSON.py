#!/usr/bin/python3
"""connecting to REST api for employ information"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users"
    url = api_url + "/" + employee_id

    response = requests.get(url)

    uname = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    to_do = response.json()
    count = 0
    completed = []

    json_dict = {employee_id: []}
    for task in to_do:
        json_dict[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": uname
            })

    with open('{}.json'.format(employee_id), 'w') as json_file:
        json.dump(json_dict, json_file)
