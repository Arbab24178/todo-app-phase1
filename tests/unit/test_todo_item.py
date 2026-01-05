"""
Unit tests for the TodoItem model.
"""
import pytest
from datetime import datetime
from todo_app.models.todo_item import TodoItem


class TestTodoItem:
    """Test cases for the TodoItem model."""
    
    def test_create_todo_item_valid(self):
        """Test creating a valid TodoItem."""
        item = TodoItem(1, "Test task")
        
        assert item.id == 1
        assert item.description == "Test task"
        assert item.completed is False
        assert isinstance(item.created_at, datetime)
    
    def test_create_todo_item_with_completion_status(self):
        """Test creating a TodoItem with initial completion status."""
        item = TodoItem(1, "Test task", completed=True)
        
        assert item.id == 1
        assert item.description == "Test task"
        assert item.completed is True
    
    def test_create_todo_item_empty_description_fails(self):
        """Test that creating a TodoItem with empty description raises ValueError."""
        with pytest.raises(ValueError, match="Description cannot be empty"):
            TodoItem(1, "")
    
    def test_create_todo_item_whitespace_description_fails(self):
        """Test that creating a TodoItem with whitespace-only description raises ValueError."""
        with pytest.raises(ValueError, match="Description cannot be empty"):
            TodoItem(1, "   ")
    
    def test_create_todo_item_none_description_fails(self):
        """Test that creating a TodoItem with None description raises ValueError."""
        with pytest.raises(ValueError, match="Description cannot be None"):
            TodoItem(1, None)
    
    def test_create_todo_item_long_description_fails(self):
        """Test that creating a TodoItem with description exceeding 255 chars raises ValueError."""
        long_desc = "x" * 256
        with pytest.raises(ValueError, match="Description exceeds maximum length"):
            TodoItem(1, long_desc)
    
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
    
    def test_description_setter_validation(self):
        """Test that the description setter validates input."""
        item = TodoItem(1, "Test task")
        
        with pytest.raises(ValueError, match="Description cannot be empty"):
            item.description = ""
        
        with pytest.raises(ValueError, match="Description exceeds maximum length"):
            item.description = "x" * 256
    
    def test_completed_setter_validation(self):
        """Test that the completed setter validates input."""
        item = TodoItem(1, "Test task")
        
        with pytest.raises(ValueError, match="Completed status must be a boolean value"):
            item.completed = "not a boolean"
    
    def test_to_dict(self):
        """Test converting TodoItem to dictionary."""
        item = TodoItem(1, "Test task", completed=True)
        item_dict = item.to_dict()
        
        expected = {
            'id': 1,
            'description': 'Test task',
            'completed': True,
            'created_at': item.created_at.isoformat()
        }
        
        assert item_dict == expected