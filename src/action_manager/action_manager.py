import logging
from typing import Dict

from src.action_manager.action_calculator import ActionCalculator
from src.action_manager.action_executor import ActionExecutor
from src.actions.action import Action
from src.actions.actions import Actions


class ActionManager:
    actions: Dict[str, Action]

    def __init__(self):
        self.actions = Actions().actions

    def select_action(self, transcript):
        action = ActionCalculator(self.actions).select_action_to_execute(transcript)

        if action is None:
            logging.error("Não consigo executar a ação pedida.")
            raise ValueError('Não consigo executar a ação pedida.')

        logging.info("Ação Detetada: {}".format(action.name))
        executor = ActionExecutor(action, transcript)
        return executor.action_callback()
