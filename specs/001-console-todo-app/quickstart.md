# Quickstart Guide: Console Todo App

## Getting Started

1. Make sure you have Python 3.8+ installed on your system
2. Clone or navigate to the project directory
3. Run the application with: `python -m todo_app.main`

## Basic Usage

Once the application starts, you can use the following commands:

- `add "Your task description"` - Add a new todo item
- `list` - View all todo items
- `complete <id>` - Mark a todo item as complete (replace <id> with the item number)
- `delete <id>` - Delete a todo item (replace <id> with the item number)
- `exit` - Exit the application

## Example Session

```
> add "Buy groceries"
Added: Buy groceries (ID: 1)

> add "Walk the dog"
Added: Walk the dog (ID: 2)

> list
1. [ ] Buy groceries
2. [ ] Walk the dog

> complete 1
Marked item 1 as complete

> list
1. [x] Buy groceries
2. [ ] Walk the dog

> exit
Goodbye!
```

## Error Handling

The application will display helpful error messages if you enter invalid commands or incorrect IDs. For example:
- If you try to complete an item that doesn't exist, you'll see an error message
- If you enter an empty task description, you'll be prompted to enter a valid one