"""
QR Code display and file saving utilities.
"""
import os
from pathlib import Path
from .models import Ticket


def save_qrcode(ticket: Ticket, filepath: str = None) -> str:
    """
    Saves a ticket's QR code to an image file.
    
    Args:
        ticket: A Ticket object containing a QR code
        filepath: Optional path where to save the file. If not provided,
                 generates a filename based on ticket ID.
    
    Returns:
        str: The filepath where the QR code was saved
    
    Raises:
        ValueError: If ticket is None or invalid
    """
    if ticket is None:
        raise ValueError("Ticket cannot be None")
    
    # Get the QR code image from the ticket
    qr_image = ticket.get_qrcode()
    
    # Generate filename if not provided
    if filepath is None:
        ticket_id = ticket.get_ticket_id()
        filepath = f"qrcode_{ticket_id}.png"
    
    # Ensure the directory exists
    filepath_obj = Path(filepath)
    filepath_obj.parent.mkdir(parents=True, exist_ok=True)
    
    # Save the image
    qr_image.save(filepath)
    
    return filepath


def save_qrcode_to_directory(ticket: Ticket, directory: str = "qrcodes") -> str:
    """
    Saves a ticket's QR code to a specified directory.
    
    Args:
        ticket: A Ticket object containing a QR code
        directory: Directory where to save the file (default: "qrcodes")
    
    Returns:
        str: The full filepath where the QR code was saved
    """
    if ticket is None:
        raise ValueError("Ticket cannot be None")
    
    # Create directory if it doesn't exist
    Path(directory).mkdir(parents=True, exist_ok=True)
    
    # Generate filename based on ticket ID
    ticket_id = ticket.get_ticket_id()
    filename = f"qrcode_{ticket_id}.png"
    filepath = os.path.join(directory, filename)
    
    # Save using the main function
    return save_qrcode(ticket, filepath)

