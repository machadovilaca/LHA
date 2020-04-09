import glob
import logging
import re
from typing import Dict

import yaml
from pyext import RuntimeModule

from src.Actions.Action import Action
from src.Actions.ActionCallback import ActionCallback


def string_to_callable(parser: str):
    mod: RuntimeModule = RuntimeModule.from_string('parser', parser)

    return mod


def get_argument_parser_from_yaml(data):
    parser = data.get('parse_callback_arguments_from_transcript', None)

    if parser is None:
        return None

    return string_to_callable(parser)


def get_callback_from_yaml(data):
    callback = data['callback']
    arguments = callback.get('arguments', [])

    return ActionCallback(callback['request'], callback['url'], arguments)


def yaml_to_action(data, action_name: str):
    return Action(
        action_name,
        data['tags'],
        get_callback_from_yaml(data),
        get_argument_parser_from_yaml(data)
    )


def get_action_name(directory: str, filename: str):
    match = re.search(directory + "(.+?).yaml", filename)

    if not match:
        return None

    return match.group(1)


def parse_file(filename: str, action_name: str):
    with open(filename, 'r') as stream:
        data = yaml.safe_load(stream)
        action = yaml_to_action(data, action_name)

    logging.debug("Action carregada com sucesso: {}".format(action.name))

    return action


def parse_dir(directory: str):
    actions: Dict[str, Action] = {}
    filenames: [str] = glob.glob(directory + "*.yaml")

    for filename in filenames:
        action_name = get_action_name(directory, filename)
        actions[action_name] = parse_file(filename, action_name)

    return actions
