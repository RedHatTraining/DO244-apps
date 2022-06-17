import requests
from cloudevents.http import CloudEvent, to_binary


class EventsProducer:
    """
    Knative events
    """
    default_ce_headers = {
        "type": "com.redhat.training.OrderWasCreated",
        "source": "orders-processor"
    }

    def __init__(self, sink_url: str) -> None:
        self.sink_url = sink_url

    def emit(self, data, custom_ce_headers) -> None:
        self.post_event(
            CloudEvent(
                {**self.default_ce_headers, **custom_ce_headers},
                data
            )
        )

    def post_event(self, event) -> None:
        headers, body = to_binary(event)
        headers['Content-Type'] = 'application/json'
        r = requests.post(self.sink_url, data=body, headers=headers)
        print(f" - Sink: {self.sink_url}")
        print(f" - Sink response status: {r.status_code}")
        print(f"    - Sent " f"{event}")
