"""
Unit tests for the TodoService.
"""
import pytest
from todo_app.services.todo_service import TodoService
from todo_app.models.todo_item import TodoItem


class TestTodoService:
    """Test cases for the TodoService."""
    
    def test_initial_state(self):
        """Test initial state of TodoService."""
        service = TodoService()
        
        assert len(service.list_todos()) == 0
        assert service.todo_list.next_id == 1
    
    def test_add_todo(self):
        """Test adding a todo item."""
        service = TodoService()
        
        item = service.add_todo("Test task")
        
        assert isinstance(item, TodoItem)
        assert item.id == 1
        assert item.description == "Test task"
        assert item.completed is False
        
        todos = service.list_todos()
        assert len(todos) == 1
        assert todos[0].id == 1
    
    def test_add_todo_validation_error(self):
        """Test that adding a todo with invalid description raises ValueError."""
        service = TodoService()
        
        with pytest.raises(ValueError, match="Description cannot be empty"):
            service.add_todo("")
    
    def test_list_todos(self):
        """Test listing all todo items."""
        service = TodoService()
        service.add_todo("Test task 1")
        service.add_todo("Test task 2")
        
        todos = service.list_todos()
        
        assert len(todos) == 2
        assert todos[0].description == "Test task 1"
        assert todos[1].description == "Test task 2"
    
    def test_complete_todo(self):
        """Test completing a todo item."""
        service = TodoService()
        item = service.add_todo("Test task")
        
        success = service.complete_todo(item.id)
        
        assert success is True
        assert item.completed is True
    
    def test_complete_todo_not_exists(self):
        """Test completing a non-existing todo item."""
        service = TodoService()
        
        success = service.complete_todo(999)
        
        assert success is False
    
    def test_mark_incomplete(self):
        """Test marking a todo item as incomplete."""
        service = TodoService()
        item = service.add_todo("Test task")
        service.complete_todo(item.id)  # First mark as complete
        
        success = service.mark_incomplete(item.id)
        
        assert success is True
        assert item.completed is False
    
    def test_mark_incomplete_not_exists(self):
        """Test marking a non-existing todo item as incomplete."""
        service = TodoService()
        
        success = service.mark_incomplete(999)
        
        assert success is False
    
    def test_delete_todo(self):
        """Test deleting a todo item."""
        service = TodoService()
        item = service.add_todo("Test task")
        
        success = service.delete_todo(item.id)
        
        assert success is True
        assert len(service.list_todos()) == 0
    
    def test_delete_todo_not_exists(self):
        """Test deleting a non-existing todo item."""
        service = TodoService()
        
        success = service.delete_todo(999)
        
        assert success is False
    
    def test_get_todo(self):
        """Test getting a specific todo item."""
        service = TodoService()
        item = service.add_todo("Test task")
        
        retrieved_item = service.get_todo(item.id)
        
        assert retrieved_item is not None
        assert retrieved_item.id == item.id
        assert retrieved_item.description == item.description
    
    def test_get_todo_not_exists(self):
        """Test getting a non-existing todo item."""
        service = TodoService()
        
        retrieved_item = service.get_todo(999)
        
        assert retrieved_item is None
    
    def test_get_completed_count(self):
        """Test getting the count of completed items."""
        service = TodoService()
        item1 = service.add_todo("Test task 1")
        item2 = service.add_todo("Test task 2")
        service.complete_todo(item1.id)  # Mark first item as complete
        
        completed_count = service.get_completed_count()
        
        assert completed_count == 1
    
    def test_get_pending_count(self):
        """Test getting the count of pending items."""
        service = TodoService()
        item1 = service.add_todo("Test task 1")
        item2 = service.add_todo("Test task 2")
        service.complete_todo(item1.id)  # Mark first item as complete
        
        pending_count = service.get_pending_count()
        
        assert pending_count == 1
    
    def test_clear_completed(self):
        """Test clearing completed items."""
        service = TodoService()
        item1 = service.add_todo("Test task 1")
        item2 = service.add_todo("Test task 2")
        item3 = service.add_todo("Test task 3")
        
        # Mark items 1 and 3 as complete
        service.complete_todo(item1.id)
        service.complete_todo(item3.id)
        
        cleared_count = service.clear_completed()
        
        assert cleared_count == 2
        assert len(service.list_todos()) == 1
        assert service.list_todos()[0].id == item2.id  # Only item 2 should remain