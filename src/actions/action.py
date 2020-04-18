from pyext import RuntimeModule

from src.actions.action_callback import ActionCallback


class Action:
    name: str
    tags: [str]
    callback: ActionCallback
    callback_arguments_parser: RuntimeModule

    def __init__(
            self,
            name: str,
            tags: [str],
            callback: ActionCallback,
            callback_arguments_parser: RuntimeModule
    ):
        self.name = name
        self.tags = tags
        self.callback = callback
        self.callback_arguments_parser = callback_arguments_parser
