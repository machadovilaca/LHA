import logging
import os

from src.ActionManager.ActionManager import ActionManager
from src.Actions.Actions import get_actions
from src.Speech.SpeechRecognizer import SpeechRecognizer

logging_format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logging_format)

if __name__ == "__main__":
    action_manager: ActionManager = ActionManager(get_actions())

    try:
        speech_recognizer = SpeechRecognizer(device_index=int(os.getenv('MICRO', '0')))
        transcript = speech_recognizer.parse_voice_input()
        action_manager.select_and_execute_action(transcript)
    except ValueError as e:
        logging.error(e)
        exit(1)

