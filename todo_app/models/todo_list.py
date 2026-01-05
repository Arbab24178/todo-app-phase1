"""
TodoList model representing a collection of todo items.
"""
from typing import List, Optional
from .todo_item import TodoItem


class TodoList:
    """
    Collection of TodoItem objects that represents the user's complete list of tasks.
    """
    
    def __init__(self):
        """Initialize an empty TodoList."""
        self._items: List[TodoItem] = []
        self._next_id = 1
    
    @property
    def items(self) -> List[TodoItem]:
        """Get all todo items in the list."""
        return self._items.copy()  # Return a copy to prevent external modification
    
    @property
    def next_id(self) -> int:
        """Get the next ID to assign to a new item."""
        return self._next_id
    
    def add_item(self, description: str) -> TodoItem:
        """
        Add a new todo item to the list.
        
        Args:
            description: Description of the new todo item
            
        Returns:
            The newly created TodoItem
            
        Raises:
            ValueError: If description is invalid according to TodoItem validation rules
        """
        new_item = TodoItem(self._next_id, description, completed=False)
        self._items.append(new_item)
        self._next_id += 1
        return new_item
    
    def get_item(self, item_id: int) -> Optional[TodoItem]:
        """
        Retrieve a specific todo item by ID.
        
        Args:
            item_id: ID of the todo item to retrieve
            
        Returns:
            The TodoItem if found, None otherwise
        """
        for item in self._items:
            if item.id == item_id:
                return item
        return None
    
    def update_item_status(self, item_id: int, completed: bool) -> bool:
        """
        Update the completion status of a todo item.
        
        Args:
            item_id: ID of the todo item to update
            completed: New completion status
            
        Returns:
            True if the item was found and updated, False otherwise
        """
        item = self.get_item(item_id)
        if item:
            item.completed = completed
            return True
        return False
    
    def delete_item(self, item_id: int) -> bool:
        """
        Remove a todo item from the list by ID.
        
        Args:
            item_id: ID of the todo item to delete
            
        Returns:
            True if the item was found and deleted, False otherwise
        """
        for i, item in enumerate(self._items):
            if item.id == item_id:
                del self._items[i]
                return True
        return False
    
    def get_all_items(self) -> List[TodoItem]:
        """
        Retrieve all todo items in the list.
        
        Returns:
            List of all TodoItems
        """
        return self._items.copy()
    
    def get_completed_count(self) -> int:
        """
        Get the count of completed todo items.
        
        Returns:
            Number of completed items
        """
        return sum(1 for item in self._items if item.completed)
    
    def get_pending_count(self) -> int:
        """
        Get the count of pending (not completed) todo items.
        
        Returns:
            Number of pending items
        """
        return len(self._items) - self.get_completed_count()
    
    def clear_completed(self) -> int:
        """
        Remove all completed todo items from the list.
        
        Returns:
            Number of items that were removed
        """
        initial_count = len(self._items)
        self._items = [item for item in self._items if not item.completed]
        return initial_count - len(self._items)