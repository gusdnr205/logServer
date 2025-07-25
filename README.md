# Log Server


This repository contains two ways to view log files stored in the `logs` directory.

1. **Flask-based viewer** – A very small Python application that lists text logs
   and displays them in a web page.
2. **ELK stack** – A Docker Compose setup that uses Elasticsearch, Logstash and
   Kibana to ingest logs and provide a rich GUI for searching and visualising
   them.

## Using the Flask viewer

The original example is kept for reference. Install Flask and run the app:

```bash
pip install Flask
python log_server.py
```

Navigate to `http://localhost:5000` to view the list of log files and their
contents.

## Using the ELK stack

The recommended approach is to run the included Docker Compose configuration.
It launches Elasticsearch, Logstash and Kibana. Logstash is configured to read
`*.txt` files from the `logs` directory.

### Requirements
- Docker
- Docker Compose

### Steps
1. Start the stack:
   ```bash
   docker-compose up
   ```
2. Once all containers are running, open `http://localhost:5601` in your browser
   to access Kibana. Logs will be indexed under indices named
   `logserver-YYYY.MM.DD`.
3. Place additional `.txt` files in the `logs` folder and Logstash will ingest
   them automatically.

Stop the stack with `Ctrl+C` and `docker-compose down` when finished.
