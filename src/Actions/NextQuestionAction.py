from src.ActionManager.Action import Action

def create_action() -> Action:
    action: Action = Action("NextQuestion", ["próxima", "pergunta", "seguinte", "questão"], callback,
                            None)
    return action


def callback(answer: str):
    print("Próxima questão")
