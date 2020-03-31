import src.Actions.SelectOptionAction as SelectOptionAction
import src.Actions.NextQuestionAction as NextQuestionAction
import src.Actions.PreviousQuestionAction as PreviousQuestionAction

def get_actions():
    return [
        SelectOptionAction.create_action(),
        NextQuestionAction.create_action(),
        PreviousQuestionAction.create_action()
    ]
