# Log Server

This repository contains a simple Flask-based log viewer. It reads `.txt` files from the `logs` directory and serves them via a web interface.

## Requirements

- Python 3.x
- Flask (`pip install Flask`)

## Usage

1. Install dependencies:
   ```bash
   pip install Flask
   ```
2. Start the server:
   ```bash
   python log_server.py
   ```
3. Open your browser and navigate to `http://localhost:5000` to view the available log files.

Log files placed in the `logs` folder will be listed on the main page. Clicking a file name displays its contents.
