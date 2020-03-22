import logging

import speech_recognition


class SpeechRecognizer:
    sr: speech_recognition.Recognizer
    device_index: int
    sample_rate: int
    chunk_size: int

    def __init__(self, device_index: int = 0, sample_rate: int = 48000, chunk_size: int = 2048):
        self.sr = speech_recognition.Recognizer()
        self.device_index = device_index
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size

        self.verify_microphones()

    def verify_microphones(self):
        mic_list = speech_recognition.Microphone.list_microphone_names()
        if len(mic_list) <= self.device_index:
            raise ValueError(
                "Can't use microphone, available options are {}, set env variable MICRO:(index)".format(mic_list)
            )

    def parse_voice_input(self):
        with speech_recognition.Microphone(
                device_index=self.device_index, sample_rate=self.sample_rate,
                chunk_size=self.chunk_size) as source:
            self.sr.adjust_for_ambient_noise(source)

            logging.debug("A ouvir...")
            audio = self.sr.listen(source)
            logging.debug("Enviar para a Google...")

            try:
                transcript = self.sr.recognize_google(audio, language='pt-PT')
                logging.debug("Percebi: {}".format(transcript))
                return transcript

            except speech_recognition.UnknownValueError as e:
                logging.error(e)
                return ""

            except speech_recognition.RequestError as e:
                logging.error(e)
                return ""
