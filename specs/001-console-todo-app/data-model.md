# Data Model: Console Todo App

## TodoItem Entity

**Fields**:
- `id`: integer, unique identifier (auto-incremented)
- `description`: string (max 255 characters), the task description
- `completed`: boolean, indicates if the task is completed (default: False)
- `created_at`: datetime, timestamp when the item was created

**Validation Rules**:
- `id` must be unique within the TodoList
- `description` must not be empty or None
- `description` must be 255 characters or less
- `completed` must be a boolean value
- `created_at` is set automatically when item is created

**State Transitions**:
- `completed` can transition from False to True (marking complete)
- `completed` can transition from True to False (marking incomplete)

## TodoList Entity

**Fields**:
- `items`: list of TodoItem objects, the collection of todo items
- `next_id`: integer, the next ID to assign to a new item (auto-incremented)

**Validation Rules**:
- All items in `items` must be valid TodoItem objects
- All `id` values in `items` must be unique
- No duplicate items allowed

**Operations**:
- Add a TodoItem to the list
- Remove a TodoItem from the list by ID
- Update a TodoItem's status by ID
- Retrieve all TodoItems
- Retrieve a specific TodoItem by ID
- Get count of completed items
- Get count of pending items