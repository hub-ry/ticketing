from flask import Flask, request, jsonify
from src.ticketing.models import User, Ticket
from src.ticketing.database import connection


app = Flask(__name__)


connection.create_tables()


# Route 1: Create a ticket
@app.route('/api/tickets', methods=['POST'])
def create_ticket():
  # Get JSON data from request
  data = request.json
  
  # Create user
  user = User(data['first_name'], data['last_name'])
  
  # Save user to database
  connection.insert_user(
      user.get_user_id(),
      user.get_first_name(),
      user.get_last_name(),
      None,
      None
  )
  
  # Create ticket
  ticket = Ticket(user)
  
  # Save ticket to database
  connection.insert_ticket(
      ticket.get_ticket_id(),
      user.get_user_id(),
      ticket.get_qrcode_string()
  )
    
  # Return JSON response
  return jsonify({
      'ticket_id': ticket.get_ticket_id(),
      'user_id': user.get_user_id()
  })




# Route 2: Get a ticket
@app.route('/api/tickets/<ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
  # Query database
  ticket_data = connection.get_ticket(ticket_id)
  
  # Return data
  return jsonify({
      'ticket_id': ticket_data[0],
      'user_id': ticket_data[1],
      'qrcode_string': ticket_data[2]
  })


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)