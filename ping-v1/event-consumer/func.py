from parliament import Context, event
import json


@event
def main(context: Context):

    event_data = json.dumps(context.cloud_event.data)

    print(f"Event data {context.cloud_event}")

    return event_data
