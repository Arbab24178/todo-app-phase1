# CLI Contract: Console Todo App

## Command Interface

### Add Command
- **Command**: `add "<description>"`
- **Input**: A string description of the task (max 255 characters)
- **Output**: Success message with the created item ID
- **Error Cases**: 
  - Empty description → Error message prompting for valid input
  - Description too long → Error message indicating limit

### List Command
- **Command**: `list`
- **Input**: None
- **Output**: Formatted list of all todo items with ID, status, and description
- **Error Cases**: None

### Complete Command
- **Command**: `complete <id>`
- **Input**: Integer ID of the todo item to mark complete
- **Output**: Success message confirming the item was marked complete
- **Error Cases**:
  - Invalid ID format → Error message about valid ID format
  - ID not found → Error message indicating item doesn't exist

### Delete Command
- **Command**: `delete <id>`
- **Input**: Integer ID of the todo item to delete
- **Output**: Success message confirming the item was deleted
- **Error Cases**:
  - Invalid ID format → Error message about valid ID format
  - ID not found → Error message indicating item doesn't exist

### Exit Command
- **Command**: `exit`
- **Input**: None
- **Output**: Goodbye message and application termination
- **Error Cases**: None

## Data Contract

### TodoItem
- **id**: integer, unique identifier
- **description**: string (max 255 chars), task description
- **completed**: boolean, completion status
- **created_at**: datetime, timestamp of creation

### Display Format
- Incomplete items: `[ ] <id>. <description>`
- Completed items: `[x] <id>. <description>`