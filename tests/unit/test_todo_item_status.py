"""
Unit tests for TodoItem status updates.
"""
import pytest
from todo_app.models.todo_item import TodoItem


class TestTodoItemStatus:
    """Test cases for TodoItem status updates."""
    
    def test_mark_complete(self):
        """Test marking a TodoItem as complete."""
        item = TodoItem(1, "Test task")
        
        item.mark_complete()
        
        assert item.completed is True
    
    def test_mark_incomplete(self):
        """Test marking a TodoItem as incomplete."""
        item = TodoItem(1, "Test task", completed=True)
        
        item.mark_incomplete()
        
        assert item.completed is False
    
    def test_toggle_status(self):
        """Test toggling the completion status of a TodoItem."""
        item = TodoItem(1, "Test task")
        
        # Initially False
        assert item.completed is False
        
        # Toggle to True
        item.toggle_status()
        assert item.completed is True
        
        # Toggle back to False
        item.toggle_status()
        assert item.completed is False