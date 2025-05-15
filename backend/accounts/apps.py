import logging
import os

from django.apps import AppConfig

from accounts_api import settings

logger = logging.getLogger(__name__)


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        if os.environ.get('RUN_MAIN') == 'true' or 'manage.py' not in ' '.join(os.sys.argv):
            # Only start the server if we're likely in a worker process
            # or not running a management command like 'migrate' or 'shell'.
            try:
                from prometheus_client import start_http_server
                metrics_port = getattr(settings, 'PROMETHEUS_METRICS_PORT', 9091)
                start_http_server(metrics_port)
                logger.info(f"Started Prometheus metrics server on port {metrics_port}")
            except OSError as e:
                # Handle potential port binding issues, especially with runserver autoreload
                logger.warning(f"Could not start Prometheus metrics server on port {metrics_port}: {e}")
            except ImportError:
                logger.error("prometheus_client library not found. Cannot start metrics server.")
