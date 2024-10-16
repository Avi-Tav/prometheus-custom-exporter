import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
LISTENING_PORT = int(os.getenv('LISTENING_PORT', '8222'))

INTERVAL_MYJOB_SECONDS = int(os.getenv('INTERVAL_MYJOB_SECONDS', '300')) # set the interval for the job in seconds

BASE_SERVER_URL = os.getenv('BASE_SERVER_URL')
SKIP_MONITOR_CHECK = os.getenv('SKIP_MONITOR_CHECK', 'false')

PASSWORD = os.getenv('PASSWORD')
USERNAME = os.getenv('USERNAME')

GAUGE_LABEL_NAMES = ['method', 'base_server_uri', 'skip_monitor_check'] # Add more labels if needed

# Add more metrics labels if needed such as HISTOGRAM, COUNTER, etc.