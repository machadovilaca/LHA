from typing import Dict

from watchdog.observers import Observer

from src.Actions import FileToActionParser
from src.Actions.Action import Action
from src.Actions.ActionChangeHandler import ActionChangeHandler


class Actions:
    path: str = "Actions/Catalog/"
    actions: Dict[str, Action] = {}

    def __init__(self):
        self.load_all_actions()
        self.listen_actions_changes()

    def load_all_actions(self):
        self.actions = FileToActionParser.parse_dir(self.path)

    def listen_actions_changes(self):
        observer = Observer()
        observer.schedule(ActionChangeHandler(self.path, self.actions), "Actions/Catalog")
        observer.start()
