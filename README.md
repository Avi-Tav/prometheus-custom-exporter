# Custom Prometheus Exporter

A custom Prometheus exporter built in Python that fetches data from a specified API endpoint and exposes metrics for Prometheus to scrape. This exporter is designed to be flexible, secure, and easy to configure, allowing you to monitor various metrics from any API that provides the necessary data.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Flexible Metric Collection**: Easily fetch and expose custom metrics from any API endpoint.
- **Secure Dependency Management**: Uses hashed dependencies to ensure package integrity.
- **Configurable via Environment Variables**: Adjust settings without modifying the source code.
- **Logging**: Comprehensive logging to monitor the exporter's operations and troubleshoot issues.
- **Error Handling**: Robust mechanisms to handle API call failures and other runtime errors.
- **Docker Support**: Containerize the exporter for seamless deployment across environments.

## Prerequisites

Before setting up the custom Prometheus exporter, ensure you have the following installed:

- **Python 3.6 or higher**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Prometheus**: [Download Prometheus](https://prometheus.io/download/)
- **Optional - Docker**: For containerized deployments. [Download Docker](https://www.docker.com/get-started)

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Avi-Tav/prometheus-custom-exporter.git
cd prometheus-custom-exporter
```

### 2. Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Configure Environment Variables

touch .env


Open the .env file in your preferred text editor and add the following configurations:

```bash
# .env

# Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL=INFO

# Port where the exporter will listen for Prometheus scrapes
LISTENING_PORT=8222

# Interval in seconds between each job execution
INTERVAL_MYJOB_SECONDS=30

# The base URL of the server/API you want to monitor
BASE_SERVER_URL=https://www.google.com/

# Whether to skip certain monitor checks (true/false)
SKIP_MONITOR_CHECK=false

# Authentication credentials (if required by the API)
USERNAME=username
PASSWORD=1234
```

Security Tip: Ensure that your .env file is not committed to version control by verifying that .env is listed in your .gitignore file.


```bash
Configuration
The exporter is configured via environment variables, allowing you to customize its behavior without altering the source code. Here's a breakdown of each environment variable:

Environment Variables
Variable	Description	Default Value
LOG_LEVEL	Sets the logging level for the exporter. Options include DEBUG, INFO, WARNING, ERROR, CRITICAL.	DEBUG
LISTENING_PORT	The port on which the exporter will expose metrics for Prometheus to scrape.	8222
INTERVAL_MYJOB_SECONDS	The interval in seconds at which the exporter will execute its job to fetch and update metrics.	300
BASE_SERVER_URL	The API endpoint from which the exporter fetches data to generate metrics.	No default (Required)
SKIP_MONITOR_CHECK	A boolean flag to skip certain monitor checks if set to true.	false
USERNAME	Username for authenticating with the API endpoint, if required.	No default (Optional)
PASSWORD	Password for authenticating with the API endpoint, if required.	No default (Optional)
Note: Sensitive information such as USERNAME and PASSWORD should be handled securely and never committed to version control.

Usage
Once installed and configured, you can start the Prometheus exporter using the following command:

bash
Copy code
python main.py
Upon running, the exporter will:

Initialize Logging: Sets up logging based on the specified LOG_LEVEL.
Start HTTP Server: Exposes an HTTP endpoint on the specified LISTENING_PORT for Prometheus to scrape metrics.
Initialize Job Manager: Sets up jobs to fetch data from the BASE_SERVER_URL at intervals defined by INTERVAL_MYJOB_SECONDS.
Expose Metrics: Updates and exposes metrics that can be scraped by Prometheus.
Running with Docker (Optional)
To run the exporter in a Docker container, follow these steps:

Build the Docker Image:

bash
Copy code
docker build -t custom-prometheus-exporter .
Run the Docker Container:

bash
Copy code
docker run -d -p 8222:8222 \
  --env LOG_LEVEL=INFO \
  --env LISTENING_PORT=8222 \
  --env INTERVAL_MYJOB_SECONDS=30 \
  --env BASE_SERVER_URL=https://www.google.com/ \
  --env SKIP_MONITOR_CHECK=false \
  --env USERNAME=username \
  --env PASSWORD=1234 \
  --name prometheus_exporter \
  custom-prometheus-exporter
Note: Replace the environment variable values as needed.

How It Works
The custom Prometheus exporter operates by periodically fetching data from a specified API endpoint and exposing this data as Prometheus metrics. Here's a step-by-step breakdown of its operation:

Initialization:

Logging Setup: Configures logging based on the LOG_LEVEL environment variable to monitor the exporter's operations and debug issues.
HTTP Server Start: Initiates an HTTP server on the specified LISTENING_PORT, providing an endpoint (/metrics) that Prometheus can scrape for metrics.
Job Scheduling:

Job Manager: Utilizes the jobManager class to manage and execute jobs that fetch data from the BASE_SERVER_URL.
Scheduling: Uses the schedule library to run the myjobname_job function at intervals defined by INTERVAL_MYJOB_SECONDS.
Fetching and Exposing Metrics:

API Calls: Makes HTTP GET requests to the BASE_SERVER_URL to retrieve data.
Metric Updates: Parses the received data and updates Prometheus gauges with the relevant metrics.
Error Handling: Logs any errors encountered during API calls or metric updates, ensuring that issues are traceable.
Prometheus Scraping:

Metrics Exposure: The exporter exposes the updated metrics at the /metrics endpoint.
Scraping by Prometheus: Prometheus is configured to scrape this endpoint at regular intervals, collecting the latest metrics for monitoring and alerting purposes.
Metrics
The exporter defines and exposes the following Prometheus metrics:

myjobname: A gauge metric that represents a specific metric fetched from the API.
Example Output:

plaintext
Copy code
# HELP myjobname myjobname job
# TYPE myjobname gauge
myjobname{method="GET",code="200",base_server_uri="https://www.google.com/",skip_monitor_check="false"} 65.5
# HELP python_gc_objects_collected_total ...
# TYPE python_gc_objects_collected_total counter
...
Note: Replace myjobname and its labels with actual metric names and labels relevant to your use case.

Environment Variables
Below is a detailed explanation of each environment variable required by the exporter:

LOG_LEVEL
Description: Sets the logging level for the exporter. Determines the verbosity of logs.
Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
Default: DEBUG
Example:
bash
Copy code
export LOG_LEVEL=INFO
LISTENING_PORT
Description: Specifies the port on which the exporter will listen for Prometheus scrape requests.
Default: 8222
Example:
bash
Copy code
export LISTENING_PORT=8222
INTERVAL_MYJOB_SECONDS
Description: Defines the interval in seconds between each execution of the data-fetching job.
Default: 300
Example:
bash
Copy code
export INTERVAL_MYJOB_SECONDS=30
BASE_SERVER_URL
Description: The API endpoint from which the exporter fetches data to generate metrics.
Required: Yes
Example:
bash
Copy code
export BASE_SERVER_URL=https://www.google.com/
SKIP_MONITOR_CHECK
Description: A boolean flag to skip certain monitoring checks if set to true.
Default: false
Options: true, false
Example:
bash
Copy code
export SKIP_MONITOR_CHECK=false
USERNAME
Description: Username for authenticating with the API endpoint, if required.
Required: Optional
Example:
bash
Copy code
export USERNAME=username
PASSWORD
Description: Password for authenticating with the API endpoint, if required.
Required: Optional
Example:
bash
Copy code
export PASSWORD=1234
Security Note: Avoid hardcoding sensitive information like USERNAME and PASSWORD directly into your code or committing them to version control. Always use environment variables or secure secrets management solutions.

Contributing
Contributions are welcome! Whether it's reporting bugs, suggesting features, or submitting pull requests, your input helps improve the project.

Steps to Contribute
Fork the Repository: Click the "Fork" button on the repository page to create your own copy.
Clone Your Fork:
bash
Copy code
git clone https://github.com/YourUsername/prometheus-custom-exporter.git
cd prometheus-custom-exporter
Create a New Branch:
bash
Copy code
git checkout -b feature/your-feature-name
Make Changes and Commit:
bash
Copy code
git add .
git commit -m "Add feature XYZ"
Push to Your Fork:
bash
Copy code
git push origin feature/your-feature-name
Create a Pull Request: Navigate to the original repository and create a pull request from your fork.
Guidelines
Code Style: Follow PEP 8 guidelines for Python code.
Testing: Ensure that your changes pass existing tests and add new tests for new features.
Documentation: Update the README.md and other documentation as necessary.
License
This project is licensed under the MIT License.

Contact
For any questions, suggestions, or support, feel free to reach out:

GitHub Issues: Open an issue
Email: a.tavdish@gmail.com
```