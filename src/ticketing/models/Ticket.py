# The ticket will also have a unique ID
import uuid

# This is to create the relevant QR code associated with the Ticket
import qrcode

# Every ticket will contain a User the ticket was issued to
from .User import User


class Ticket:
    """
    Represents a ticket object in the ticketing system.
    -----------------------------------------------------------------------------
    | Attributes:
    |- 
    """
