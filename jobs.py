import logging
from MyApiManager import MyApiManager
import settings

class jobManager(object):
    def __init__(self):
        self.server_uri = settings.BASE_SERVER_URL
        self.instance_password = settings.PASSWORD
        self.instance_username = settings.USERNAME
        self.monitor_check = settings.SKIP_MONITOR_CHECK
        self.api_manager = MyApiManager(server_uri=self.server_uri,
                                        password=self.instance_password,
                                        username=self.instance_username)
    
    def _labels(self, gauge, code):
        if code < 400:
            gauge.labels(method='GET', base_server_uri=self.server_uri, skip_monitor_check=self.monitor_check).inc()
            gauge.labels(method='GET', base_server_uri=self.server_uri, skip_monitor_check=self.monitor_check).set(0)
            gauge.labels(method='GET', base_server_uri=self.server_uri, skip_monitor_check=self.monitor_check).set(0)
        elif code < 500:
            gauge.labels(method='GET', base_server_uri=self.server_uri, skip_monitor_check=self.monitor_check).set(0)
            gauge.labels(method='GET', base_server_uri=self.server_uri, skip_monitor_check=self.monitor_check).inc()
            gauge.labels(method='GET', base_server_uri=self.server_uri, skip_monitor_check=self.monitor_check).set(0)
        else:
            gauge.labels(method='GET', base_server_uri=self.server_uri, skip_monitor_check=self.monitor_check).set(0)
            gauge.labels(method='GET', base_server_uri=self.server_uri, skip_monitor_check=self.monitor_check).set(0)
            gauge.labels(method='GET', base_server_uri=self.server_uri, skip_monitor_check=self.monitor_check).inc()
    
    def myjobname_job(self, gauge):
        try:
            response = self.api_manager.get_my_end_point()
            logging.info(f"myjobname_job: status code: {response}")
            self._labels(gauge, response)
            gauge.labels(method='GET', base_server_uri=self.server_uri, skip_monitor_check=self.monitor_check).set(response)
        except Exception as err:
            logging.error(err)


    # Add more jobs if needed