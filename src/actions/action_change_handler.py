import logging
from typing import Dict

from actions import file_to_action_parser
from actions.action import Action


class ActionChangeHandler:
    path: str
    actions: Dict[str, Dict[str, Action]]

    def __init__(self, path: str, actions: dict):
        self.path = path
        self.actions = actions

    def new_action(self, event, action_name):
        action: Action = file_to_action_parser.parse_file(event.src_path, action_name)
        lang = file_to_action_parser.get_lang_name(event.src_path)

        if lang not in self.actions:
            self.actions[lang] = {}

        if action is not None:
            self.actions[lang][action.name] = action

    def delete_action(self, event, action_name: str):
        lang = file_to_action_parser.get_lang_name(event.src_path)
        self.actions[lang].pop(action_name, None)

    def handle_action_change(self, event, action_name: str):
        logging.info("Action {}: {}".format(event.event_type, event.src_path))

        if event.event_type == "created":
            self.new_action(event, action_name)
        elif event.event_type == "modified":
            self.delete_action(event, action_name)
            self.new_action(event, action_name)
        elif event.event_type == "deleted":
            self.delete_action(event, action_name)

    def dispatch(self, event):
        if event.is_directory:
            return

        action_name = file_to_action_parser.get_action_name(self.path, event.src_path)

        if action_name is None:
            return

        self.handle_action_change(event, action_name)
