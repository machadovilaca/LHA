import json

from flask import request, Blueprint, send_file

from src.action_manager.action_manager import ActionManager
from src.speech.speech_recognizer import parse_file_input

web_app = Blueprint('web_app', __name__)
action_manager: ActionManager = ActionManager()


def build_response(value: dict, status: int):
    return json.dumps(value), status, {'ContentType': 'application/json'}


@web_app.errorhandler(Exception)
def all_exception_handler(error: Exception):
    return build_response({"error": str(error)}, 400)


@web_app.route("/voice", methods=["POST"])
def receive_audio_blob():
    language = request.form.get("language", "pt-PT")
    file = request.files["audio"]

    transcript = parse_file_input(file, language)
    callback = action_manager.select_action(transcript)

    return build_response(callback, 200)


@web_app.route('/demo/<string:file>')
def demo(file):
    return send_file('../demo/' + file)
