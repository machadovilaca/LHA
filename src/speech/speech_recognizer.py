import logging

import speech_recognition as sr


def parse_file_input(file, language):
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)

        try:
            transcript = r.recognize_google(audio, language=language)  # TODO: change to recognize_google_cloud
            logging.info("Percebi: " + transcript)
            return transcript
        except sr.UnknownValueError:
            raise ValueError("Google speech Recognition não conseguiu processar o áudio")
        except sr.RequestError as e:
            raise ValueError("Google speech Recognition error: {0}".format(e))
