"""
Simple tests for QR code display/saving functionality.
"""
import pytest
import os
from pathlib import Path
from src.ticketing.models import User, Ticket
from src.ticketing.display import save_qrcode, save_qrcode_to_directory


def test_save_qrcode_with_custom_filepath():
    """Test that a QR code can be saved to a specified filepath."""
    user = User("John", "Doe")
    ticket = Ticket(user)
    
    test_filepath = "test_qrcode.png"
    
    # Remove file if it exists
    if os.path.exists(test_filepath):
        os.remove(test_filepath)
    
    # Save the QR code
    saved_path = save_qrcode(ticket, test_filepath)
    
    # Verify file was created
    assert os.path.exists(test_filepath)
    assert saved_path == test_filepath
    
    # Verify it's a valid image file (check file size > 0)
    assert os.path.getsize(test_filepath) > 0
    
    # Cleanup
    os.remove(test_filepath)


def test_save_qrcode_with_default_filename():
    """Test that a QR code can be saved with auto-generated filename."""
    user = User("Jane", "Smith")
    ticket = Ticket(user)
    
    # Save without specifying filepath
    saved_path = save_qrcode(ticket)
    
    # Verify file was created with expected naming pattern
    assert os.path.exists(saved_path)
    assert saved_path.startswith("qrcode_")
    assert saved_path.endswith(".png")
    assert ticket.get_ticket_id() in saved_path
    
    # Cleanup
    os.remove(saved_path)


def test_save_qrcode_to_directory():
    """Test that a QR code can be saved to a specific directory."""
    user = User("Alice", "Brown")
    ticket = Ticket(user)
    
    test_dir = "test_qrcodes"
    
    # Remove directory if it exists
    if os.path.exists(test_dir):
        import shutil
        shutil.rmtree(test_dir)
    
    # Save to directory
    saved_path = save_qrcode_to_directory(ticket, test_dir)
    
    # Verify directory was created
    assert os.path.exists(test_dir)
    assert os.path.isdir(test_dir)
    
    # Verify file was created in directory
    assert os.path.exists(saved_path)
    assert saved_path.startswith(test_dir)
    assert ticket.get_ticket_id() in saved_path
    
    # Cleanup
    import shutil
    shutil.rmtree(test_dir)

