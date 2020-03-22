from typing import List

from Action import Action
from ActionExecutor import ActionExecutor
from ActionCalculator import ActionCalculator


class ActionManager:
    actions: List[Action]

    def __init__(self, actions: List[Action]):
        self.actions = actions

    def select_and_execute_action(self, transcript):
        #action = self.actions[0]  # select_action_to_execute(t)    
        action = ActionCalculator(self.actions).select_action_to_execute(transcript)
        executor = ActionExecutor(action, transcript)
        executor.execute_action()
