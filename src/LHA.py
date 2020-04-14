import logging
import os
from typing import Dict
from src.ActionManager.ActionManager import ActionManager
from src.Actions.Action import Action
from src.Actions.Actions import Actions
from src.Speech.SpeechRecognizer import SpeechRecognizer
from flask import Flask

logging_format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logging_format)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/msi-gtfo/Downloads/LEI-MIEI-52d06bcdb32f.json"

app = Flask(__name__)


@app.route("/")
def receive_audio_blob():
    actions: Dict[str, Action] = Actions().actions
    action_manager: ActionManager = ActionManager(actions)

    try:
        #speech_recognizer = SpeechRecognizer(device_index=int(os.getenv('MICRO', '0')))
        transcript = SpeechRecognizer.parse_file_input("test.wav")
        action_manager.select_and_execute_action(transcript)
    except ValueError as e:
        logging.error(e)
        exit(1)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
