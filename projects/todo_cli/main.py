import argparse

from task_manager import add_task, delete_task, complete_tasks, clear_file, list_tasks

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

# --- Add command ---
add_parser = subparsers.add_parser("add")
add_parser.add_argument("task_name")

# --- Remove command ---
remove_parser = subparsers.add_parser("remove")
remove_parser.add_argument("task_id")

# --- Complete Status Command ---
complete_status_parser = subparsers.add_parser("complete")
complete_status_parser.add_argument("task_id")

# --- List command ---
list_parser = subparsers.add_parser("list")

# --- Clear Command ---
clear_parser = subparsers.add_parser("clear")

args = parser.parse_args()


if args.command == "add":
    add_task(args.task_name)
elif args.command == "remove":
    delete_task(args.task_id)
elif args.command == "list":
    list_tasks()
elif args.command == "complete":
    complete_tasks(args.task_id)
elif args.command == "clear":
    clear_file()
else:
    "Command not found"
