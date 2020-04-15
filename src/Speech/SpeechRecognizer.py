import logging
import speech_recognition

from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
from pydub import AudioSegment


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

    @staticmethod
    def parse_file_input(file):
        client = speech_v1p1beta1.SpeechClient()
        language_code = "pt-PT"

        encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
        config = {
            "language_code": language_code,
            "sample_rate_hertz": 44100,
            "encoding": encoding
        }

        try:
            mysound = AudioSegment.from_wav(file)
            mysound = mysound.set_channels(1)
            mysound = mysound.set_frame_rate(44100)

            audio = {"content": mysound.raw_data}
            logging.debug("Enviar para a Google...")
            response = client.recognize(config, audio)
            transcript = response.results[0].alternatives[0].transcript
            logging.debug("Percebi: {}".format(transcript))

            return transcript

        except FileNotFoundError as e:
            logging.error(e)
            return ""
