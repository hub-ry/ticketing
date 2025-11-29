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
    |- user : User
    |   An object from the User class
    |- ticked_id : str
    |   UUID generated to ensure ticket is unique
    |- qrcode : (idk the type)
    |   The QR Code associated with the UUID of ticket, of User, and name of User
    |- qrcode_string : str
    |   string format of all data stored in QR code (ticked_id, user_id, name)
    """

    def __init__(self, user : User):
        self.__user = user
        self.__ticket_id = str(uuid.uuid4())
        self.__qrcode_string = f"{user.get_first_name()}~{user.get_last_name()},{user.get_user_id()},{self.__ticket_id}"
        self.__qrcode = qrcode.make(self.qrcode_string)

    def __str__(self):
        return(
            f"User: {self.get_user()}"
            f"Ticked ID: {self.get_ticket_id()}\n"
            f"QR-Code String: {self.get_qrcode_string()}"
        )
    
    # Accessor methods
    def get_user(self) -> User:
        return self.__user
    def get_ticket_id(self) -> str:
        return self.__ticket_id
    def get_qrcode(self):
        return self.__qrcode
    def get_qrcode_string(self) -> str:
        return self.__qrcode_string
