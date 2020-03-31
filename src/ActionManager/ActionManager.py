import logging
from typing import List

from src.ActionManager.Action import Action
from src.ActionManager.ActionCalculator import ActionCalculator
from src.ActionManager.ActionExecutor import ActionExecutor


class ActionManager:
    actions: List[Action]

    def __init__(self, actions: List[Action]):
        self.actions = actions

    def select_and_execute_action(self, transcript):
        action = ActionCalculator(self.actions).select_action_to_execute(transcript)

        if action is None:
            logging.error("Não consigo executar a ação pedida.")
            return
        
        logging.debug("Ação Detetada: {}".format(action.name))
        executor = ActionExecutor(action, transcript)
        executor.execute_action()
