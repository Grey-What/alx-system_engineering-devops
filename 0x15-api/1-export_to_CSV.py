#!/usr/bin/python3
"""connecting to REST api for employ information and storing in CSV"""

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

    with open("{}.csv".format(employee_id), 'w') as file:
        for task in to_do:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, uname,
                               task.get("completed"), task.get("title")))
