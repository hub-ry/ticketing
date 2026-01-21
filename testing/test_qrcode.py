"""
Quick test script to generate and view a QR code.
"""
from src.ticketing.models import User, Ticket
from src.ticketing.display import save_qrcode
import subprocess
import sys
import os

# Create a test user and ticket
user = User("Test", "User", email="test@example.com")
ticket = Ticket(user)

# Save the QR code
filepath = save_qrcode(ticket, "test_ticket.png")
print(f"QR code saved to: {filepath}")
print(f"Ticket ID: {ticket.get_ticket_id()}")
print(f"User: {user.get_first_name()} {user.get_last_name()}")

# Open it automatically based on OS
if sys.platform == "darwin":  # macOS
    subprocess.run(["open", filepath])
elif sys.platform == "linux":  # Linux
    subprocess.run(["xdg-open", filepath])
elif sys.platform == "win32":  # Windows
    os.startfile(filepath)
else:
    print(f"Please open {filepath} manually")

