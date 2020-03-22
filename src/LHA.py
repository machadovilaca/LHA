import logging

from src.ActionManager.ActionManager import ActionManager
from src.Actions.Actions import get_actions
from src.Speech.SpeechRecognizer import SpeechRecognizer

logging_format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logging_format)

if __name__ == "__main__":
    action_manager: ActionManager = ActionManager(get_actions())
    speech_recognizer = SpeechRecognizer()
    transcript = speech_recognizer.get_speech()
    action_manager.select_and_execute_action(transcript)
