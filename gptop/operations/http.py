import json
import requests
from enum import Enum

__all__ = ["HTTPOperation", "HTTPType"]


class HTTPType(str, Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class HTTPOperation():
    """
    An operation that executes an HTTP request.
    """

    def __init__(self, metadata: any, input: any):
        self.type = metadata["type"]
        self.url = metadata["url"]
        self.path = metadata["path"]
        self.params = input.get("params")
        self.body = input.get("body")
        self.headers = input.get("headers")

    def execute(self):
        result = None

        endpoint = self.url + self.path
        data = None
        if self.body:
            data = json.dumps(self.body).encode('utf-8')

        if self.type == HTTPType.POST:
            result = requests.post(
                url=endpoint,
                headers=self.headers,
                params=self.params,
                data=data
            )

        elif self.type == HTTPType.GET:
            result = requests.get(
                url=endpoint,
                headers=self.headers,
                params=self.params,
                data=data
            )

        elif self.type == HTTPType.PUT:
            result = requests.put(
                url=endpoint,
                headers=self.headers,
                params=self.params,
                data=data
            )

        elif self.type == HTTPType.PATCH:
            result = requests.patch(
                url=endpoint,
                headers=self.headers,
                params=self.params,
                data=data
            )

        elif self.type == HTTPType.DELETE:
            result = requests.delete(
                url=endpoint,
                headers=self.headers,
                params=self.params,
                data=data
            )

        if not result:
            return None

        return result.json()