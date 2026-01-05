"""
Integration tests for the CLI functionality.
"""
import pytest
from io import StringIO
from unittest.mock import patch
from todo_app.cli.cli_controller import CLIController


class TestCLIIntegration:
    """Integration tests for the CLI controller."""
    
    def test_add_and_list_todos(self):
        """Test adding and listing todos."""
        controller = CLIController()
        
        # Add a few todos
        controller._handle_add("First task")
        controller._handle_add("Second task")
        
        # Capture the output of the list command
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            controller._handle_list()
            output = mock_stdout.getvalue()
        
        # Check that both tasks appear in the output
        assert "First task" in output
        assert "Second task" in output
        assert "[ ]" in output  # Check for pending status
    
    def test_add_complete_and_list_todos(self):
        """Test adding, completing, and listing todos."""
        controller = CLIController()
        
        # Add a todo
        controller._handle_add("Test task")
        
        # Complete the todo (ID should be 1)
        controller._handle_complete("1")
        
        # Capture the output of the list command
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            controller._handle_list()
            output = mock_stdout.getvalue()
        
        # Check that the task appears as completed
        assert "Test task" in output
        assert "[x]" in output  # Check for completed status
    
    def test_list_empty_todos(self):
        """Test listing when there are no todos."""
        controller = CLIController()
        
        # Capture the output of the list command
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            controller._handle_list()
            output = mock_stdout.getvalue()
        
        # Check that the empty list message appears
        assert "Your todo list is empty" in output