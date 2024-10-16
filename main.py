from time import sleep
from prometheus_client import start_http_server, Gauge
import schedule
import logging
import functools
import settings
import sys
from jobs import jobManager

if __name__ == "__main__":
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(settings.LOG_LEVEL)
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[handler]
    )
    logging.info("Starting Prometheus exporter")
    start_http_server(settings.LISTENING_PORT)
    logging.info(f"Listening on port {settings.LISTENING_PORT}")
    job_manager = jobManager()
    logging.info(f"Starting to monitor {settings.BASE_SERVER_URL}")

    gauge_myjobname = Gauge(
        name='my_metric_name', # Change the name of the metric
        documentation='my_metric_description', # Change the description of the metric
        labelnames=settings.GAUGE_LABEL_NAMES
    )

    schedule.every(settings.INTERVAL_MYJOB_SECONDS).seconds.do(
        functools.partial(job_manager.myjobname_job, gauge_myjobname)
    )

    # Add more jobs if needed

    while True:
        try:
            schedule.run_pending()
            sleep(30)
        except Exception as err:
            logging.error(f" Recived an error - {err}")
            sleep(120)