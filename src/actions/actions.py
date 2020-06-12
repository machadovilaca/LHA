import os
from typing import Dict

from watchdog.observers import Observer

from actions import file_to_action_parser
from actions.action import Action
from actions.action_change_handler import ActionChangeHandler


module_path = os.environ['MODULE_PATH']


class Actions:
    path: str = module_path + "/src/actions/catalog"
    actions: Dict[str, Action] = {}

    def __init__(self):
        self.load_all_actions()
        self.listen_actions_changes()

    def load_all_actions(self):
        self.actions = file_to_action_parser.parse_dir(self.path + "/")

    def listen_actions_changes(self):
        observer = Observer()
        observer.schedule(ActionChangeHandler(self.path+ "/", self.actions), self.path)
        observer.start()
