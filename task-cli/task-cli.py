import argparse
import json
from datetime import datetime
from pathlib import Path


def task_properties(task_id, description, status, createdAt, updatedAt):
    properties = {
        "task_id": task_id,
        "description": description,
        "status": status,
        "createdAt": createdAt,
        "updatedAt": updatedAt,
    }

    return properties


def add_task(args):
    if Path(tasks_file).is_file():
        try:
            with open(tasks_file, "r") as openfile:
                data_in = json.load(openfile)
        except Exception as e:
            print(f"An error has occurred: {e}")
            exit(1)

        print(data_in)

    if not Path(tasks_file).is_file():
        task_id = 1
        description = args.task
        status = "todo"
        createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updatedAt = createdAt

    data_in = task_properties(
        task_id,
        description,
        status,
        createdAt,
        updatedAt,
    )

    print(data_in)

    try:
        with open(tasks_file, "w") as f:
            json.dump(data_in, f)
    except Exception as e:
        print(f"An error has occurred: {e}")
        exit(1)


def list_tasks(args):
    with open(tasks_file, "r") as openfile:
        data_in = json.load(openfile)
    print(data_in)
    print(type(data_in))


def main():
    parser = argparse.ArgumentParser(description="To do app")

    subparsers = parser.add_subparsers(dest="action", required=True, help="Hi")

    parser_add_task = subparsers.add_parser("add", help="Add item to the list")
    parser_add_task.add_argument("task", help="Task description")
    parser_add_task.set_defaults(funct=add_task)

    parser_list_tasks = subparsers.add_parser("list", help="List tasks")
    parser_list_tasks.add_argument("--status", help="Task status")
    parser_list_tasks.set_defaults(funct=list_tasks)

    args = parser.parse_args()
    args.funct(args)


if __name__ == "__main__":

    tasks_file = "task_json.json"
    main()
