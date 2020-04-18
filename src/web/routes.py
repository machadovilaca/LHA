import json
import logging
from typing import Dict
from flask import request, Blueprint
from src.ActionManager.ActionManager import ActionManager
from src.Actions.Action import Action
from src.Actions.Actions import Actions
from src.Speech.SpeechRecognizer import SpeechRecognizer

web_app = Blueprint('web_app', __name__)


@web_app.route("/voice", methods=['POST'])
def receive_audio_blob():
    file = request.files['audio']
    if file.filename == "":
        return json.dumps({'error': "Missing file to transcript"}), 400, {'ContentType':'application/json'}

    actions: Dict[str, Action] = Actions().actions
    action_manager: ActionManager = ActionManager(actions)

    try:
        transcript = SpeechRecognizer.parse_file_input(file)
        action_manager.select_and_execute_action(transcript)
    except ValueError as e:
        logging.error(e)
        exit(1)
