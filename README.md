# Custom Prometheus Exporter

A Python-based Prometheus exporter that retrieves data from a specified API and exposes metrics for Prometheus. Easily configurable, secure, and supports Docker deployment.

## Features
- **Custom Metrics**: Fetch and expose metrics from any API.
- **Environment-Based Configuration**: Adjust settings without altering code.
- **Error Handling & Logging**: Comprehensive logging and error handling.
- **Docker Support**: Containerize for easy deployment.

## Prerequisites
- Python 3.6+ | [Install Python](https://www.python.org/downloads/)
- Git | [Install Git](https://git-scm.com/downloads)
- Prometheus | [Install Prometheus](https://prometheus.io/download/)
- (Optional) Docker | [Install Docker](https://www.docker.com/get-started)

## Installation

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/Avi-Tav/prometheus-custom-exporter.git
   cd prometheus-custom-exporter
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file with:
   ```bash
   LOG_LEVEL=INFO
   LISTENING_PORT=8222
   INTERVAL_MYJOB_SECONDS=30
   BASE_SERVER_URL=https://www.google.com/
   SKIP_MONITOR_CHECK=false
   USERNAME=username
   PASSWORD=1234
   ```

   Ensure `.env` is listed in `.gitignore`.

## Usage

Run the exporter:
```bash
python main.py
```

### Docker Usage (Optional)
1. **Build Docker Image**:
   ```bash
   docker build -t custom-prometheus-exporter .
   ```

2. **Run the Container**:
   ```bash
   docker run -d -p 8222:8222 --env-file .env custom-prometheus-exporter
   ```

## How It Works
- Fetches data from `BASE_SERVER_URL` at intervals (`INTERVAL_MYJOB_SECONDS`).
- Exposes metrics at `/metrics` for Prometheus to scrape.
- Logs and handles errors based on `LOG_LEVEL`.

## Metrics
- **`myjobname`**: Example metric exposed by the exporter.
   ```bash
   # HELP myjobname job
   # TYPE myjobname gauge
   myjobname{method="GET",code="200",base_server_uri="https://www.google.com/"} 65.5
   ```

## Contact
- GitHub Issues: Open an issue
- Email: a.tavdish@gmail.com
