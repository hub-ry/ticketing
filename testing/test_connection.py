"""
Simple tests for database connection and operations.
"""
import pytest
from src.ticketing.database import connection
from src.ticketing.models import User, Ticket


def test_create_tables(test_db):
    """Test that tables can be created successfully."""
    # Tables should be created by the fixture
    # Just verify we can connect and query
    con = connection.get_connection()
    cur = con.cursor()
    
    # Check that USER table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USER'")
    assert cur.fetchone() is not None
    
    # Check that TICKET table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='TICKET'")
    assert cur.fetchone() is not None
    
    con.close()


def test_insert_and_get_user(test_db):
    """Test inserting a user and retrieving it."""
    user = User("John", "Doe", email="john@example.com")
    
    connection.insert_user(
        user.get_user_id(),
        user.get_first_name(),
        user.get_last_name(),
        user.get_email(),
        None
    )
    
    retrieved = connection.get_user(user.get_user_id())
    
    assert retrieved is not None
    assert retrieved[0] == user.get_user_id()
    assert retrieved[1] == "John"
    assert retrieved[2] == "Doe"


def test_insert_and_get_ticket(test_db):
    """Test inserting a ticket and retrieving it."""
    user = User("Jane", "Smith")
    ticket = Ticket(user)
    
    # Insert user first (required for foreign key)
    connection.insert_user(
        user.get_user_id(),
        user.get_first_name(),
        user.get_last_name(),
        None,
        None
    )
    
    # Insert ticket
    connection.insert_ticket(
        ticket.get_ticket_id(),
        user.get_user_id(),
        ticket.get_qrcode_string()
    )
    
    retrieved = connection.get_ticket(ticket.get_ticket_id())
    
    assert retrieved is not None
    assert retrieved[0] == ticket.get_ticket_id()
    assert retrieved[1] == user.get_user_id()

