import click
import json 
import os 

TODO_FILE = "todo.json"

# Function to load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4) 

@click.group()
def cli():
    """Simple To-Do List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """ADD a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})  # Add the new task to the list
    save_tasks(tasks)  # Save the updated task list
    click.echo(f"Task '{task}' added!")


@click.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks Found!")
        return
    for index, task in enumerate(tasks, 1):
        status = "yes" if task["done"] else "No" 
        click.echo(f"{index} . {task['task']} [{status}]")

@click.command()
@click.argument("task_number",type=int)
def complete(task_number):
    """Mark a task as Completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number -1]["done"] = True
        save_tasks(tasks) 
        click.echo(f"Task {task_number} marked as completed!")
    else:
        click.echo("Invalid task number.") 

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)  # Fixed variable name from 'remove_task' to 'removed_task'
        save_tasks(tasks)
        click.echo(f"Removed task: {removed_task['task']}")
    else:
        click.echo("Invalid task number.")




cli.add_command(add)  
cli.add_command(list) 
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli() 


