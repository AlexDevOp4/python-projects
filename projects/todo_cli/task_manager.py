import json
import os
from datetime import datetime

from colorama import Fore, Back, Style

file_path = "tasks.json"
current_datetime = datetime.now()


def write_tasks(tasks):
    try:
        with open(file_path, "w") as f:
            json.dump(tasks, f, indent=4)
        print("Updated data written back to file")
    except IOError as e:
        print(f"Error writting to file '{file_path}': {e}")


def add_task(task):
    # Step 1: Load existing tasks if file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            tasks = json.load(f)
    else:
        tasks = {}

    # Step 2: Add new task
    task_id = len(tasks) + 1
    tasks[task_id] = {
        "task": task,
        "status": "in-progress",
        "datetime": current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
    }

    # Step 3: Write updated task list
    return write_tasks(tasks)


def delete_task(taskId):
    with open(file_path, "r") as f:
        tasks = json.load(f)

    if taskId in tasks:
        del tasks[taskId]
        print(f"Task {taskId} removed successfully")
    else:
        print(f"Task {taskId} not found.")

    write_tasks(tasks)


def complete_tasks(taskId):
    with open(file_path, "r") as f:
        tasks = json.load(f)

    if taskId in tasks:
        tasks[taskId]["status"] = "complete"
        print(f"Task {taskId} status updated!")
    else:
        print(f"Task {taskId} not found.")

    write_tasks(tasks)


def clear_file():
    with open(file_path, "r") as f:
        tasks = json.load(f)

    tasks.clear()

    write_tasks(tasks)


def list():
    with open(file_path, "r") as f:
        tasks = json.load(f)
    sorted_tasks = dict(
        sorted(
            tasks.items(),
            key=lambda item: datetime.strptime(
                item[1]["datetime"], "%Y-%m-%d %H:%M:%S"
            ),
        )
    )

    # Print result
    for task_id, info in sorted_tasks.items():
        if info['status'] == 'complete':
            print(Fore.GREEN + info["status"])
            print(info)
        else:
            print(Fore.RED + info["status"])
            print(info)

