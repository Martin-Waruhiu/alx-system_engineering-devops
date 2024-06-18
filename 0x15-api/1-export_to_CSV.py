#!/usr/bin/python3


"""Using what you did in the task #0, extend your Python script to export data in the Csv format"""

import csv
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
    username = user.get("name")
    """get the todos from the todos endpoint"""
    params = {"userId": employee_id}
    todo_response = requests.get(url + "todos/", params=params)
    todos = todo_response.json()

"""converting to a csv format"""

csv_file = "{}.csv".format(employee_id)
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    for todo in todos:
        writer.writerow([employee_id, username, todo.get("completed"), todo.get("title")])
