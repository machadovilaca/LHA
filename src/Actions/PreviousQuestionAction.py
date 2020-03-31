from src.ActionManager.Action import Action

def create_action() -> Action:
    action: Action = Action("PreviousQuestion", ["anterior", "pergunta", "questão"], callback,
                            None)
    return action


def callback(answer: str):
    print("Quesão anterior")
