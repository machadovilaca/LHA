from collections import Callable


class Action:
    action_id: str
    callback: Callable
    name: str

    def __init__(self, action_id: int, name: str, callback: Callable):
        self.id = action_id
        self.name = name
        self.callback = callback
