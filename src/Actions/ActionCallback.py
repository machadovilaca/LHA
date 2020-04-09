from typing import List


class ActionCallback:
    request: str
    url: str
    arguments: List[str]

    def __init__(self, request: str, url: str, arguments: List[str]):
        self.request = request
        self.url = url
        self.arguments = arguments
