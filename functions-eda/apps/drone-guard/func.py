import logging
from parliament import Context


logging.basicConfig(level=logging.INFO)


def main(context: Context):
    """
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """

    if context.cloud_event:
        type = context.cloud_event["type"]
        eventdata = context.cloud_event.data
        logging.info(f"Incoming event {type}")
        logging.info(eventdata)


    return { "message": "Accepted" }, 202
