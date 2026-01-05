"""
TodoService containing business logic for todo operations.
"""
from typing import List, Optional
from ..models.todo_list import TodoList
from ..models.todo_item import TodoItem


class TodoService:
    """
    Business logic layer for todo operations.
    """
    
    def __init__(self):
        """Initialize the TodoService with a TodoList."""
        self._todo_list = TodoList()
    
    @property
    def todo_list(self) -> TodoList:
        """Get the TodoList managed by this service."""
        return self._todo_list
    
    def add_todo(self, description: str) -> TodoItem:
        """
        Add a new todo item.
        
        Args:
            description: Description of the new todo item
            
        Returns:
            The newly created TodoItem
            
        Raises:
            ValueError: If description is invalid
        """
        return self._todo_list.add_item(description)
    
    def list_todos(self) -> List[TodoItem]:
        """
        Get all todo items.
        
        Returns:
            List of all TodoItems
        """
        return self._todo_list.get_all_items()
    
    def complete_todo(self, item_id: int) -> bool:
        """
        Mark a todo item as complete.
        
        Args:
            item_id: ID of the todo item to mark complete
            
        Returns:
            True if the item was found and marked complete, False otherwise
        """
        return self._todo_list.update_item_status(item_id, True)
    
    def mark_incomplete(self, item_id: int) -> bool:
        """
        Mark a todo item as incomplete.
        
        Args:
            item_id: ID of the todo item to mark incomplete
            
        Returns:
            True if the item was found and marked incomplete, False otherwise
        """
        return self._todo_list.update_item_status(item_id, False)
    
    def delete_todo(self, item_id: int) -> bool:
        """
        Delete a todo item.
        
        Args:
            item_id: ID of the todo item to delete
            
        Returns:
            True if the item was found and deleted, False otherwise
        """
        return self._todo_list.delete_item(item_id)
    
    def get_todo(self, item_id: int) -> Optional[TodoItem]:
        """
        Get a specific todo item by ID.
        
        Args:
            item_id: ID of the todo item to retrieve
            
        Returns:
            The TodoItem if found, None otherwise
        """
        return self._todo_list.get_item(item_id)
    
    def get_completed_count(self) -> int:
        """
        Get the count of completed todo items.
        
        Returns:
            Number of completed items
        """
        return self._todo_list.get_completed_count()
    
    def get_pending_count(self) -> int:
        """
        Get the count of pending (not completed) todo items.
        
        Returns:
            Number of pending items
        """
        return self._todo_list.get_pending_count()
    
    def clear_completed(self) -> int:
        """
        Remove all completed todo items.
        
        Returns:
            Number of items that were removed
        """
        return self._todo_list.clear_completed()