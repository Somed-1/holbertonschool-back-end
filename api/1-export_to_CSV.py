#!/usr/bin/python3
"""."""

import csv
import requests
import sys

TASK_URL = "https://jsonplaceholder.typicode.com/todos"
USER_URL = "https://jsonplaceholder.typicode.com/users/"


def employee_info(user_id: str):
    """."""
    task_response = requests.get(TASK_URL + "?userId=" + user_id).json()
    user_response = requests.get(USER_URL + user_id).json()

    name = user_response.get("username")

    with open(f"{user_id}.csv", "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in task_response:
            writer.writerow([user_id, name, task.get("completed"),
                             task.get("title")])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: 1-export_to_CSV.py <employee_id>")
    user_id = sys.argv[1]
    employee_info(user_id)
