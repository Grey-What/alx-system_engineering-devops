#!/usr/bin/python3
"""connecting to REST api for employ information"""

import json
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(api_url)
    users = response.json()

    u_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'

        response = requests.get(url)
        tasks = response.json()

        u_dict[user_id] = []
        for task in tasks:
            u_dict[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(u_dict, file)
