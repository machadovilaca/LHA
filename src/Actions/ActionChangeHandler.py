import logging
from typing import Dict

from src.Actions import FileToActionParser
from src.Actions.Action import Action


class ActionChangeHandler:
    path: str
    actions: Dict[str, Action]

    def __init__(self, path: str, actions: dict):
        self.path = path
        self.actions = actions

    def new_action(self, event, action_name):
        action: Action = FileToActionParser.parse_file(event.src_path, action_name)
        self.actions[action.name] = action

    def delete_action(self, action_name: str):
        self.actions.pop(action_name, None)

    def handle_action_change(self, event, action_name: str):
        logging.debug("Action {}: {}".format(event.event_type, event.src_path))

        if event.event_type == "created":
            self.new_action(event, action_name)
        elif event.event_type == "modified":
            self.delete_action(action_name)
            self.new_action(event, action_name)
        elif event.event_type == "deleted":
            self.delete_action(action_name)

    def dispatch(self, event):
        if event.is_directory:
            return

        action_name = FileToActionParser.get_action_name(self.path, event.src_path)

        if action_name is None:
            return

        self.handle_action_change(event, action_name)