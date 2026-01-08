"""
Simple tests for the Ticket model.
"""
import pytest
from src.ticketing.models import User, Ticket


def test_ticket_creation():
    """Test that a ticket can be created for a user."""
    user = User("John", "Doe")
    ticket = Ticket(user)
    
    assert ticket.get_user() == user
    assert ticket.get_ticket_id() is not None
    assert len(ticket.get_ticket_id()) > 0


def test_ticket_qrcode_string_format():
    """Test that the QR code string contains user and ticket information."""
    user = User("Jane", "Smith")
    ticket = Ticket(user)
    
    qr_string = ticket.get_qrcode_string()
    
    assert user.get_first_name() in qr_string
    assert user.get_last_name() in qr_string
    assert user.get_user_id() in qr_string
    assert ticket.get_ticket_id() in qr_string


def test_ticket_unique_ids():
    """Test that each ticket gets a unique ID."""
    user = User("Alice", "Brown")
    ticket1 = Ticket(user)
    ticket2 = Ticket(user)
    
    assert ticket1.get_ticket_id() != ticket2.get_ticket_id()

