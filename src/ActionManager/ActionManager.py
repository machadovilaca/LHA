from typing import List
from src.ActionManager.Action import Action
from src.ActionManager.ActionExecutor import ActionExecutor


class ActionManager:
    actions: List[Action]

    def __init__(self, actions: List[Action]):
        self.actions = actions

    def select_and_execute_action(self, transcript):
        action = self.actions[0]  # select_action_to_execute(t)
        executor = ActionExecutor(action, transcript)
        executor.execute_action()
