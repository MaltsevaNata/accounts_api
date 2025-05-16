from django.http import HttpRequest, HttpResponse
from prometheus_client import Counter

api_requests_status_codes = Counter(
    'api_requests_status_codes',
    'Number of requests partitioned by status codes',
    ['status_code', 'response_status']
)


def get_response_status(response_status_code: int) -> str:
    response_status = "undefined"

    if int(response_status_code) >= 500:
        response_status = "server_error"
    elif int(response_status_code) >= 400:
        response_status = "client_error"
    elif int(response_status_code) >= 300:
        response_status = "redirect"
    elif int(response_status_code) >= 200:
        response_status = "success"

    return response_status


class PrometheusMetricsCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)
        self.send_metrics_after_handle(request, response)
        return response

    def send_metrics_after_handle(self, request: HttpRequest, response: HttpResponse) -> None:
        response_status = get_response_status(response.status_code)
        status_code = response.status_code
        api_requests_status_codes.labels(status_code=status_code,
                                         response_status=response_status).inc()
