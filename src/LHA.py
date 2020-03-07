from typing import List
from src.actions.Action import Action
from src.actions.ActionManager import ActionManager


def create_action() -> Action:
    action: Action = Action(0, "Selector", callback)
    return action


def callback(answer: str, certainty: str):
    print("Selected {} with {} certainty.".format(answer, certainty))


if __name__ == "__main__":
    actions: List[Action] = [create_action()]
    action_manager: ActionManager = ActionManager(actions)
    action_manager.select_and_execute_action("")
