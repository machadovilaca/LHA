import logging
from typing import Dict

from src.ActionManager.ActionCalculator import ActionCalculator
from src.ActionManager.ActionExecutor import ActionExecutor
from src.Actions.Action import Action


class ActionManager:
    actions: Dict[str, Action]

    def __init__(self, actions: Dict[str, Action]):
        self.actions = actions

    def select_and_execute_action(self, transcript):
        action = ActionCalculator(self.actions).select_action_to_execute(transcript)

        if action is None:
            logging.error("Não consigo executar a ação pedida.")
            return

        logging.debug("Ação Detetada: {}".format(action.name))
        executor = ActionExecutor(action, transcript)
        executor.execute_action()
