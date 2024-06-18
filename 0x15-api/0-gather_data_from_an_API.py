#!/usr/bin/python3
""" a Python script that, using this REST API,
for a given employee ID, returns
information about his/her TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    """get the users from the users endpoint"""
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()
    """get the todos from the todos endpoint"""
    params = {"userId": employee_id}
    todo_response = requests.get(url + "todos/", params=params)
    todos = todo_response.json()

    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{})".format(user.get("name"), len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
