"""
Simple test script to verify the todo application functionality.
"""
from todo_app.models.todo_item import TodoItem
from todo_app.models.todo_list import TodoList
from todo_app.services.todo_service import TodoService


def test_basic_functionality():
    """Test basic functionality of the todo application."""
    print("Testing basic functionality...")
    
    # Test TodoItem
    item = TodoItem(1, "Test task")
    assert item.id == 1
    assert item.description == "Test task"
    assert item.completed is False
    print("✓ TodoItem creation works")
    
    # Test TodoList
    todo_list = TodoList()
    assert len(todo_list.items) == 0
    print("✓ TodoList creation works")
    
    # Add item to list
    added_item = todo_list.add_item("New task")
    assert len(todo_list.items) == 1
    assert added_item.id == 1
    print("✓ Adding item to TodoList works")
    
    # Test TodoService
    service = TodoService()
    service.add_todo("Service test task")
    todos = service.list_todos()
    assert len(todos) == 1
    assert todos[0].description == "Service test task"
    print("✓ TodoService functionality works")
    
    # Test completing a task
    success = service.complete_todo(todos[0].id)
    assert success is True
    assert todos[0].completed is True
    print("✓ Completing a task works")
    
    # Test deleting a task
    delete_success = service.delete_todo(todos[0].id)
    assert delete_success is True
    assert len(service.list_todos()) == 0
    print("✓ Deleting a task works")
    
    print("\nAll basic functionality tests passed! ✓")


if __name__ == "__main__":
    test_basic_functionality()