import glob
import logging
import re
from typing import Dict

import yaml
from pyext import RuntimeModule

from src.actions.action import Action
from src.actions.action_callback import ActionCallback


def validate_argument_parser(parser):
    valid_func_def_1 = re.compile(r'def( *)parse( *)\(( *)transcript( *):( *)str( *)\)( *):')
    valid_func_def_2 = re.compile(r'def( *)parse( *)\(( *)transcript( *)\)( *):')

    if not valid_func_def_1.search(parser) and not valid_func_def_2.search(parser):
        raise ValueError('function "def parser(transcript)" not defined')


def argument_parser_string_to_callable(parser: str):
    validate_argument_parser(parser)

    mod: RuntimeModule = RuntimeModule.from_string('parser', parser)
    return mod


def get_argument_parser_from_yaml(data):
    parser = data.get('parse_callback_arguments_from_transcript', None)

    if parser is None:
        return None

    return argument_parser_string_to_callable(parser)


def get_callback_from_yaml(data):
    callback = data['callback']
    arguments = callback.get('arguments', [])

    return ActionCallback(callback['request'], callback['url'], arguments)


def yaml_to_action(data, action_name: str):
    try:
        action = Action(
            action_name,
            data['tags'],
            get_callback_from_yaml(data),
            get_argument_parser_from_yaml(data)
        )
        logging.info("Action ({}) carregada com sucesso".format(action.name))
        return action
    except (IndentationError, Exception) as e:
        logging.error("Action ({}) contém erros: {}".format(action_name, str(e)))
        return None


def get_action_name(directory: str, filename: str):
    match = re.search(directory + "(.+?).yaml", filename)

    if not match:
        return None

    return match.group(1)


def parse_file(filename: str, action_name: str):
    with open(filename, 'r') as stream:
        data = yaml.safe_load(stream)
        action = yaml_to_action(data, action_name)

    return action


def parse_dir(directory: str):
    actions: Dict[str, Action] = {}
    filenames: [str] = glob.glob(directory + "*.yaml")

    for filename in filenames:
        action_name = get_action_name(directory, filename)
        action = parse_file(filename, action_name)

        if action is not None:
            actions[action_name] = action

    return actions
