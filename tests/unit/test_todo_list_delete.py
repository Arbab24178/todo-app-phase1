"""
Unit tests for TodoList delete functionality.
"""
import pytest
from todo_app.models.todo_list import TodoList


class TestTodoListDelete:
    """Test cases for TodoList delete functionality."""
    
    def test_delete_item_exists(self):
        """Test deleting an existing item."""
        todo_list = TodoList()
        item = todo_list.add_item("Test task")
        
        success = todo_list.delete_item(item.id)
        
        assert success is True
        assert len(todo_list.items) == 0
    
    def test_delete_item_not_exists(self):
        """Test deleting a non-existing item."""
        todo_list = TodoList()
        
        success = todo_list.delete_item(999)
        
        assert success is False
    
    def test_delete_item_with_multiple_items(self):
        """Test deleting one item when multiple items exist."""
        todo_list = TodoList()
        item1 = todo_list.add_item("Test task 1")
        item2 = todo_list.add_item("Test task 2")
        item3 = todo_list.add_item("Test task 3")
        
        success = todo_list.delete_item(item2.id)
        
        assert success is True
        assert len(todo_list.items) == 2
        
        # Verify other items still exist
        remaining_ids = [item.id for item in todo_list.items]
        assert item1.id in remaining_ids
        assert item3.id in remaining_ids
        assert item2.id not in remaining_ids