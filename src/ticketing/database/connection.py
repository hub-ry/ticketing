import sqlite3

"""
    User and Ticket Tables
    -----------------------------------------------------------------------------
    | 
    |- Even though every user will have purchased a ticket, normalizing
    |  the data to account for one user buying multiple tickets makes the program more flexible.
    |
    |- Flask will eventually call insert_user()
    |
    |- Enable foreign keys to prevent errors. It checks that the value in this column (or columns) must exist as a primary key in another table.
    """


DB_NAME = "ticket.db"


def get_connection():
  """
  Creates and returns a database connection with foreign keys enabled.
  """
  con = sqlite3.connect(DB_NAME)
  con.execute("PRAGMA foreign_keys = ON;")
  return con


def create_tables():
  """
  Creates the USER and TICKET tables if they do not already exist.
  """
  con = get_connection()
  cur = con.cursor()

  # Create User table
  cur.execute("""
      CREATE TABLE IF NOT EXISTS USER (
          user_id TEXT PRIMARY KEY,
          first_name TEXT NOT NULL,
          last_name TEXT NOT NULL,
          email TEXT,
          phone TEXT
      )
  """)

  # Create Ticket table
  cur.execute("""
      CREATE TABLE IF NOT EXISTS TICKET (
          ticket_id TEXT PRIMARY KEY,
          user_id TEXT NOT NULL,
          ticket_data TEXT NOT NULL,
          FOREIGN KEY (user_id) REFERENCES USER(user_id)
      )
  """)

  con.commit()
  con.close()


def insert_user(user_id, first_name, last_name, email=None, phone=None):
  """
  Inserts a user into the USER table.
  """
  if not user_id or not first_name or not last_name:
      raise ValueError("user_id, first_name, and last_name are required")
  
  con = get_connection()
  cur = con.cursor()

  cur.execute("""
      INSERT INTO USER (user_id, first_name, last_name, email, phone)
      VALUES (?, ?, ?, ?, ?)
  """, (user_id, first_name, last_name, email, phone))

  con.commit()
  con.close()

def insert_ticket(ticket_id, user_id, ticket_data):
  """
  Inserts a ticket into the TICKET table.
  """
  if not ticket_id or not user_id or not ticket_data:
      raise ValueError("ticket_id, user_id, and ticket_data are required")
  
  con = get_connection()
  cur = con.cursor()

  cur.execute("""
      INSERT INTO TICKET (ticket_id, user_id, ticket_data)
      VALUES (?, ?, ?)
  """, (ticket_id, user_id, ticket_data))

  con.commit()
  con.close()

def get_user(user_id):
  """
  Retrieves a specific user by user_id.
  """
  con = get_connection()
  cur = con.cursor()
  cur.execute("SELECT * FROM USER WHERE user_id = ?", (user_id,))
  result = cur.fetchone()
  con.close()
  return result

def get_user_tickets(user_id):
  """
  Retrieves all tickets for a specific user.
  """
  con = get_connection()
  cur = con.cursor()
  cur.execute("SELECT * FROM TICKET WHERE user_id = ?", (user_id,))
  results = cur.fetchall()
  con.close()
  return results

def get_ticket(ticket_id):
  """
  Retrieves a specific ticket by ticket_id.
  """
  con = get_connection()
  cur = con.cursor()
  cur.execute("SELECT * FROM TICKET WHERE ticket_id = ?", (ticket_id,))
  result = cur.fetchone()
  con.close()
  return result

# Run once on startup to ensure tables exist

if __name__ == "__main__":
  create_tables()