"""
TodoItem model representing a single task in the todo application.
"""
from datetime import datetime
from typing import Union


class TodoItem:
    """
    Represents a single task with properties including ID (integer, unique identifier), 
    description (string, max 255 characters), status (boolean - completed/incomplete), 
    and creation timestamp (datetime).
    """
    
    def __init__(self, item_id: int, description: str, completed: bool = False):
        """
        Initialize a TodoItem instance.
        
        Args:
            item_id: Unique identifier for the todo item
            description: Task description (max 255 characters)
            completed: Status of the task (default: False)
        
        Raises:
            ValueError: If description is empty, None, or exceeds 255 characters
        """
        self._validate_description(description)
        
        self._id = item_id
        self._description = description
        self._completed = completed
        self._created_at = datetime.now()
    
    @property
    def id(self) -> int:
        """Get the unique identifier of the todo item."""
        return self._id
    
    @property
    def description(self) -> str:
        """Get the description of the todo item."""
        return self._description
    
    @description.setter
    def description(self, value: str) -> None:
        """Set the description of the todo item."""
        self._validate_description(value)
        self._description = value
    
    @property
    def completed(self) -> bool:
        """Get the completion status of the todo item."""
        return self._completed
    
    @completed.setter
    def completed(self, value: bool) -> None:
        """Set the completion status of the todo item."""
        if not isinstance(value, bool):
            raise ValueError("Completed status must be a boolean value")
        self._completed = value
    
    @property
    def created_at(self) -> datetime:
        """Get the creation timestamp of the todo item."""
        return self._created_at
    
    def mark_complete(self) -> None:
        """Mark the todo item as complete."""
        self._completed = True
    
    def mark_incomplete(self) -> None:
        """Mark the todo item as incomplete."""
        self._completed = False
    
    def toggle_status(self) -> None:
        """Toggle the completion status of the todo item."""
        self._completed = not self._completed
    
    def to_dict(self) -> dict:
        """Convert the TodoItem to a dictionary representation."""
        return {
            'id': self._id,
            'description': self._description,
            'completed': self._completed,
            'created_at': self._created_at.isoformat()
        }
    
    @staticmethod
    def _validate_description(description: Union[str, None]) -> None:
        """
        Validate the description according to business rules.
        
        Args:
            description: The description to validate
            
        Raises:
            ValueError: If description is invalid
        """
        if description is None:
            raise ValueError("Description cannot be None")
        
        if not description.strip():
            raise ValueError("Description cannot be empty or contain only whitespace")
        
        if len(description) > 255:
            raise ValueError(f"Description exceeds maximum length of 255 characters. "
                           f"Current length: {len(description)}")