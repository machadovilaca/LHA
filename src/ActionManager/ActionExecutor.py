import logging

from src.ActionManager.Action import Action


class ActionExecutor:
    action: Action
    transcript: str

    def __init__(self, action: Action, transcript: str):
        self.action = action
        self.transcript = transcript

    def execute_action(self):
        try:
            args: list = self.action.parse_callback_arguments_from_transcript(self.transcript)
            self.action.callback(*args)

        except ValueError:
            logging.error("Erro no processo dos argumentos")
