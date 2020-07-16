import os
from typing import Dict

from watchdog.observers import Observer

from actions import file_to_action_parser
from actions.action import Action
from actions.action_change_handler import ActionChangeHandler


class Actions:
    catalog_path: str = os.path.join(os.path.dirname(__file__), "actions_catalog")
    actions: Dict[str, Dict[str, Action]] = {}

    def __init__(self):
        self.load_all_actions()
        self.listen_actions_changes()

    def load_all_actions(self):
        self.actions = file_to_action_parser.parse_dir(self.catalog_path + "/")

    def listen_actions_changes(self):
        observer = Observer()
        observer.schedule(ActionChangeHandler(self.catalog_path + "/", self.actions), self.catalog_path, recursive=True)
        observer.start()
