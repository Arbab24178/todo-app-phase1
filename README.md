# Console Todo App

A simple console-based todo application implemented in Python with in-memory storage.

## Features

- Add new todo items
- View all todo items
- Mark items as complete/incomplete
- Delete todo items
- Exit the application

## Requirements

- Python 3.8+

## Installation

No installation required. The application uses only Python standard library.

## Usage

Run the application:

```bash
python3 -m todo_app.main
```

The application will start and show a prompt. Available commands:

- `add "description"` - Add a new todo item
- `list` - View all todo items
- `complete <id>` - Mark a todo item as complete
- `delete <id>` - Delete a todo item
- `exit` - Exit the application

## Example Session

```
> add "Buy groceries"
Added: Buy groceries (ID: 1)

> add "Walk the dog"
Added: Walk the dog (ID: 2)

> list
[ ] 1. Buy groceries
[ ] 2. Walk the dog

> complete 1
Marked item 1 as complete

> list
[x] 1. Buy groceries
[ ] 2. Walk the dog

> exit
Goodbye!
```

## Project Structure

```
todo_app/
├── __init__.py
├── main.py              # Entry point and CLI interface
├── models/
│   ├── __init__.py
│   ├── todo_item.py     # TodoItem data model
│   └── todo_list.py     # TodoList collection model
├── services/
│   ├── __init__.py
│   └── todo_service.py  # Business logic for todo operations
└── cli/
    ├── __init__.py
    └── cli_controller.py # Command-line interface controller

tests/
├── __init__.py
├── unit/
│   ├── __init__.py
│   ├── test_todo_item.py
│   ├── test_todo_list.py
│   └── test_todo_service.py
├── integration/
│   ├── __init__.py
│   └── test_cli_integration.py
└── conftest.py
```

## Testing

To run the tests:

```bash
pip install pytest
python -m pytest tests/ -v
```

## Architecture

The application follows a clean architecture with separation of concerns:

- **Models**: Handle data structures and validation
- **Services**: Contain business logic
- **CLI**: Handle user interaction