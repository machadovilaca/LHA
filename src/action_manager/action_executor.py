from src.Actions.Action import Action


class ActionExecutor:
    action: Action
    transcript: str

    def __init__(self, action: Action, transcript: str):
        self.action = action
        self.transcript = transcript

    def execute_action(self):
        request_body = {}

        if self.action.callback_arguments_parser is not None:
            args_names: list = self.action.callback.arguments
            args_values: list = self.action.callback_arguments_parser.parse(self.transcript)

            for i in range(len(args_names)):
                request_body[args_names[i]] = args_values[i]

        print("{} request to {} with body {}".format(
            self.action.callback.request,
            self.action.callback.url,
            request_body
        ))
