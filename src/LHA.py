from src.ActionManager.ActionManager import ActionManager
from src.Actions.Actions import get_actions

if __name__ == "__main__":
    action_manager: ActionManager = ActionManager(get_actions())
    action_manager.select_and_execute_action("Escolhe aí a opção 1")
    action_manager.select_and_execute_action("Escolhe aí a nona opção")
