#!/usr/bin/python3
"""."""

import json
import requests
import sys

TASK_URL = "https://jsonplaceholder.typicode.com/todos"
USER_URL = "https://jsonplaceholder.typicode.com/users/"


def employee_info(user_id: str):
    """."""
    task_response = requests.get(TASK_URL + "?userId=" + user_id).json()
    user_response = requests.get(USER_URL + user_id).json()

    name = user_response.get("username")

    tasks = []
    for task in task_response:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": name,
        }
        tasks.append(task_info)

    data = {user_id: tasks}

    file_name = f"{user_id}.json"
    with open(file_name, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: 2-export_to_JSON.py <employee_id>")
    user_id = sys.argv[1]
    employee_info(user_id)
