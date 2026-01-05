"""
Unit tests for the TodoList model.
"""
import pytest
from todo_app.models.todo_list import TodoList
from todo_app.models.todo_item import TodoItem


class TestTodoList:
    """Test cases for the TodoList model."""
    
    def test_initial_state(self):
        """Test initial state of TodoList."""
        todo_list = TodoList()
        
        assert len(todo_list.items) == 0
        assert todo_list.next_id == 1
    
    def test_add_item(self):
        """Test adding an item to the TodoList."""
        todo_list = TodoList()
        
        item = todo_list.add_item("Test task")
        
        assert len(todo_list.items) == 1
        assert item.id == 1
        assert item.description == "Test task"
        assert item.completed is False
        assert todo_list.next_id == 2
    
    def test_add_item_with_validation_error(self):
        """Test that adding an item with invalid description raises ValueError."""
        todo_list = TodoList()
        
        with pytest.raises(ValueError, match="Description cannot be empty"):
            todo_list.add_item("")
    
    def test_get_item_exists(self):
        """Test retrieving an existing item."""
        todo_list = TodoList()
        item = todo_list.add_item("Test task")
        
        retrieved_item = todo_list.get_item(item.id)
        
        assert retrieved_item is not None
        assert retrieved_item.id == item.id
        assert retrieved_item.description == item.description
    
    def test_get_item_not_exists(self):
        """Test retrieving a non-existing item."""
        todo_list = TodoList()
        
        retrieved_item = todo_list.get_item(999)
        
        assert retrieved_item is None
    
    def test_update_item_status(self):
        """Test updating an item's completion status."""
        todo_list = TodoList()
        item = todo_list.add_item("Test task")
        
        success = todo_list.update_item_status(item.id, True)
        
        assert success is True
        assert item.completed is True
    
    def test_update_item_status_not_exists(self):
        """Test updating status of a non-existing item."""
        todo_list = TodoList()
        
        success = todo_list.update_item_status(999, True)
        
        assert success is False
    
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
    
    def test_get_all_items(self):
        """Test getting all items."""
        todo_list = TodoList()
        item1 = todo_list.add_item("Test task 1")
        item2 = todo_list.add_item("Test task 2")
        
        all_items = todo_list.get_all_items()
        
        assert len(all_items) == 2
        assert item1 in all_items
        assert item2 in all_items
    
    def test_get_completed_count(self):
        """Test getting the count of completed items."""
        todo_list = TodoList()
        item1 = todo_list.add_item("Test task 1")
        item2 = todo_list.add_item("Test task 2")
        todo_list.update_item_status(item1.id, True)  # Mark first item as complete
        
        completed_count = todo_list.get_completed_count()
        
        assert completed_count == 1
    
    def test_get_pending_count(self):
        """Test getting the count of pending items."""
        todo_list = TodoList()
        item1 = todo_list.add_item("Test task 1")
        item2 = todo_list.add_item("Test task 2")
        todo_list.update_item_status(item1.id, True)  # Mark first item as complete
        
        pending_count = todo_list.get_pending_count()
        
        assert pending_count == 1
    
    def test_clear_completed(self):
        """Test clearing completed items."""
        todo_list = TodoList()
        item1 = todo_list.add_item("Test task 1")
        item2 = todo_list.add_item("Test task 2")
        item3 = todo_list.add_item("Test task 3")
        
        # Mark items 1 and 3 as complete
        todo_list.update_item_status(item1.id, True)
        todo_list.update_item_status(item3.id, True)
        
        cleared_count = todo_list.clear_completed()
        
        assert cleared_count == 2
        assert len(todo_list.items) == 1
        assert todo_list.items[0].id == item2.id  # Only item 2 should remain