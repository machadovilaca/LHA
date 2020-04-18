import logging

import speech_recognition as sr


def parse_file_input(filename: str):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)

    try:
        logging.debug("Percebi: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        logging.debug("Google Speech Recognition não conseguiu processar o áudio")
    except sr.RequestError as e:
        logging.debug("Google Speech Recognition error: {0}".format(e))
