from actions.action import Action


class ActionExecutor:
    action: Action
    transcript: str

    def __init__(self, action: Action, transcript: str):
        self.action = action
        self.transcript = transcript

    def action_callback(self):
        request_body = {}

        if self.action.callback_arguments_parser is not None:
            args_names: list = self.action.callback.arguments
            args_values: list = self.action.callback_arguments_parser.parse(self.transcript)

            for i in range(len(args_names)):
                request_body[args_names[i]] = args_values[i]

        return {
            "params": self.action.callback.params,
            "body": request_body
        }
