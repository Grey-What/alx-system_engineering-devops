#!/usr/bin/python3

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users"
    url = api_url + "/" + employee_id

    response = requests.get(url)

    employee_name = response.json().get('name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    to_do = response.json()
    count = 0
    completed = []

    for task in to_do:
        if task.get('completed'):
            completed.append(task)
            count += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, count, len(to_do)))

    for task in completed:
        print("\t {}".format(task.get('title')))
