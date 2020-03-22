from typing import List

from src.ActionManager.Action import Action
from src.ActionManager.ActionExecutor import ActionExecutor
from src.ActionManager.ActionCalculator import ActionCalculator


class ActionManager:
    actions: List[Action]

    def __init__(self, actions: List[Action]):
        self.actions = actions

    def select_and_execute_action(self, transcript):
        action = ActionCalculator(self.actions).select_action_to_execute(transcript)
        if action is None:
            print("Não consigo executar a ação pedida.")
            return
        executor = ActionExecutor(action, transcript)
        executor.execute_action()
