"""
CLI controller for the todo application.
"""
import sys
from typing import List, Optional
from ..services.todo_service import TodoService


class CLIController:
    """
    Command-line interface controller for the todo application.
    """
    
    def __init__(self):
        """Initialize the CLI controller with a TodoService."""
        self._service = TodoService()
        self._running = True
    
    def run(self) -> None:
        """Run the main application loop."""
        print("Welcome to the Console Todo App!")
        print("Available commands: add, list, complete, delete, exit")
        
        while self._running:
            try:
                command = input("\n> ").strip()
                self._process_command(command)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break
    
    def _process_command(self, command: str) -> None:
        """
        Process a user command.
        
        Args:
            command: The command string entered by the user
        """
        if not command:
            return
        
        parts = command.split(maxsplit=1)
        cmd = parts[0].lower()
        
        if cmd == "add":
            if len(parts) < 2:
                print("Error: Please provide a description for the task")
                return
            self._handle_add(parts[1])
        elif cmd == "list":
            self._handle_list()
        elif cmd == "complete":
            if len(parts) < 2:
                print("Error: Please provide an ID for the task to complete")
                return
            self._handle_complete(parts[1])
        elif cmd == "delete":
            if len(parts) < 2:
                print("Error: Please provide an ID for the task to delete")
                return
            self._handle_delete(parts[1])
        elif cmd == "exit":
            self._handle_exit()
        else:
            print(f"Error: Unknown command '{cmd}'. Available commands: add, list, complete, delete, exit")
    
    def _handle_add(self, description: str) -> None:
        """
        Handle the 'add' command.
        
        Args:
            description: The task description to add
        """
        try:
            # Remove quotes if present
            if (description.startswith('"') and description.endswith('"')) or \
               (description.startswith("'") and description.endswith("'")):
                description = description[1:-1]
            
            item = self._service.add_todo(description)
            print(f"Added: {description} (ID: {item.id})")
        except ValueError as e:
            print(f"Error: {e}")
    
    def _handle_list(self) -> None:
        """Handle the 'list' command."""
        todos = self._service.list_todos()
        
        if not todos:
            print("Your todo list is empty")
            return
        
        for item in todos:
            status = "[x]" if item.completed else "[ ]"
            print(f"{status} {item.id}. {item.description}")
    
    def _handle_complete(self, id_str: str) -> None:
        """
        Handle the 'complete' command.
        
        Args:
            id_str: The string representation of the item ID
        """
        try:
            item_id = int(id_str)
        except ValueError:
            print(f"Error: Invalid ID format '{id_str}'. Please provide a valid integer ID.")
            return
        
        success = self._service.complete_todo(item_id)
        if success:
            print(f"Marked item {item_id} as complete")
        else:
            print(f"Error: Item with ID {item_id} does not exist")
    
    def _handle_delete(self, id_str: str) -> None:
        """
        Handle the 'delete' command.
        
        Args:
            id_str: The string representation of the item ID
        """
        try:
            item_id = int(id_str)
        except ValueError:
            print(f"Error: Invalid ID format '{id_str}'. Please provide a valid integer ID.")
            return
        
        success = self._service.delete_todo(item_id)
        if success:
            print(f"Deleted item {item_id}")
        else:
            print(f"Error: Item with ID {item_id} does not exist")
    
    def _handle_exit(self) -> None:
        """Handle the 'exit' command."""
        print("Goodbye!")
        self._running = False