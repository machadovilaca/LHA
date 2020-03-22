from collections import Callable


class Action:
    name: str
    tags: [str]
    callback: Callable
    parse_callback_arguments_from_transcript: Callable

    def __init__(
            self,
            name: str,
            tags: [str],
            callback: Callable,
            parse_callback_arguments_from_transcript: Callable = None
    ):
        self.name = name
        self.tags = tags
        self.callback = callback
        self.parse_callback_arguments_from_transcript = parse_callback_arguments_from_transcript
