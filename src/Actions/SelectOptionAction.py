import re

from src.ActionManager.Action import Action
from src.Numbers.Numbers import extensiveNumbers


def create_action() -> Action:
    action: Action = Action("SelectOption", ["escolher", "selecionar", "bloquear"], callback,
                            parse_callback_arguments_from_transcript)
    return action


def callback(answer: str):
    print("Escolheu a opção {}".format(answer))


def parse_callback_arguments_from_transcript(transcript: str):
    numbers: [int] = [int(s) for s in re.findall(r'\b\d+\b', transcript)]

    if len(numbers) > 0:
        return [numbers[0]]

    for (number, extensiveNumber) in extensiveNumbers:
        if extensiveNumber in transcript:
            return [number]

    raise ValueError('No number present in transcript "{}"'.format(transcript))
