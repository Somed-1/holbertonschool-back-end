#!/usr/bin/python3
"""."""

import json
import requests

TASK_URL = "https://jsonplaceholder.typicode.com/todos"
USER_URL = "https://jsonplaceholder.typicode.com/users/"


def employee_info():
    """."""
    task_response = requests.get(TASK_URL).json()
    user_response = requests.get(USER_URL).json()

    user_ids = set([task["userId"] for task in task_response])

    tasks_by_user = {}

    for user_id in user_ids:
        username = next(
            (user["username"] for user in user_response
             if user["id"] == user_id), None
        )

        user_tasks = [task for task in task_response
                      if task["userId"] == user_id]

        task_list = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in user_tasks
        ]

        tasks_by_user[user_id] = task_list

    output_json = json.dumps(tasks_by_user)

    with open("todo_all_employees.json", "w") as file:
        file.write(output_json)


if __name__ == "__main__":
    employee_info()
