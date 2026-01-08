"""
Simple tests for the User model.
"""
import pytest
from src.ticketing.models import User


def test_user_creation_with_required_fields():
    """Test that a user can be created with just first and last name."""
    user = User("John", "Doe")
    
    assert user.get_first_name() == "John"
    assert user.get_last_name() == "Doe"
    assert user.get_user_id() is not None
    assert len(user.get_user_id()) > 0


def test_user_creation_with_optional_fields():
    """Test that a user can be created with email and phone."""
    user = User("Jane", "Smith", email="jane@example.com", phone="123-456-7890")
    
    assert user.get_first_name() == "Jane"
    assert user.get_last_name() == "Smith"
    # Note: get_email() and get_phone() currently return bool, not the actual values
    assert user.get_email() is True  # Returns True if email exists
    assert user.get_phone() is True  # Returns True if phone exists


def test_user_unique_ids():
    """Test that each user gets a unique ID."""
    user1 = User("Alice", "Brown")
    user2 = User("Bob", "Green")
    
    assert user1.get_user_id() != user2.get_user_id()

