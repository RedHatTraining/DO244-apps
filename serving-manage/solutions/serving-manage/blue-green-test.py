#!/usr/bin/env python3

import time
import argparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def make_request(url):
    request = Request(url)
    try:
        response = urlopen(request)
        text = response.read().decode("utf-8")
    except HTTPError as e:
        print("Server responded with error ", e)
        text = ""
    except URLError as e:
        print("Server not reachable: ", e.reason)
        text = ""

    return text


def parse_args():
    parser = argparse.ArgumentParser(
        description="Traffic balancer tester for blue-green service.")
    parser.add_argument("url",
        help="URL to request")
    parser.add_argument("-s", "--sleep",
        type=float, default=0.1, help="Time in seconds between each request")

    return parser.parse_args()


def prepare_url(args):
    if not args.url.startswith("http"):
        return f"http://{args.url}"

    return args.url


if __name__ == "__main__":

    args = parse_args()
    url = prepare_url(args)

    print("\033[95mBlue-Green Release Test\033[0m")
    print(f"\033[92mSending requests to {args.url} ...\033[0m\n\n")

    while True:
        text = make_request(url).strip()
        print(text)
        time.sleep(args.sleep)