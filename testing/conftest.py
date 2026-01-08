"""
Shared pytest fixtures for testing.
"""
import pytest
import os
import sqlite3
from src.ticketing.database import connection
from src.ticketing.database.connection import create_tables, get_connection


@pytest.fixture
def test_db():
    """
    Creates a temporary test database for each test.
    """
    # Use a test database file
    test_db_name = "test_ticket.db"
    
    # Remove test database if it exists
    if os.path.exists(test_db_name):
        os.remove(test_db_name)
    
    # Temporarily replace the DB_NAME
    original_db = connection.DB_NAME
    connection.DB_NAME = test_db_name
    
    # Create tables with the test database
    create_tables()
    
    yield test_db_name
    
    # Cleanup: restore original DB name and remove test database
    connection.DB_NAME = original_db
    if os.path.exists(test_db_name):
        os.remove(test_db_name)

