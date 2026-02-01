# Ticketing System

A modular, offline-first ticketing solution for event management. Features QR code generation, digital ticket management, and a lightweight REST API for seamless cross-device integration. Originally developed for the Purdue Grand Prix, but architected for general-purpose event ticketing.

## Overview

This system provides end-to-end ticketing capabilities, from user registration through QR code generation and validation. Built with simplicity and scalability in mind, it enables fast ticket processing at event gates without requiring internet connectivity—making it ideal for large-scale events of any kind.

## Features

- **QR Code Tickets** – Generates unique, secure QR codes for each ticket
- **User Management** – Stores attendee information with efficient database operations
- **REST API** – Flask-based API for ticket creation and management
- **Offline Support** – Core functionality works without internet connection
- **Modular Design** – Clean separation of concerns with dedicated modules for models, database, and display
- **Testing** – Comprehensive test suite with pytest

## Tech Stack

- **Backend**: Python, Flask, Flask-CORS
- **Database**: SQLite with custom connection management
- **QR Codes**: qrcode library with PIL support
- **Testing**: pytest with coverage tracking

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Usage

Start the API server:

```bash
python app.py
```

Create a ticket via POST request:

```bash
curl -X POST http://localhost:5000/api/tickets \
  -H "Content-Type: application/json" \
  -d '{"first_name": "John", "last_name": "Doe"}'
```

## Project Structure

```
src/ticketing/
├── models/          # User and Ticket classes
├── database/        # Database connection and operations
├── display.py       # QR code generation and file handling
└── index.html       # Web interface
testing/             # Pytest test suite
```

## License

Built collaboratively for the Purdue Grand Prix
