import emotions
import Speech_recognition
from threading import Thread

emotion = Thread(target=emotions.Emotions)
speech = Thread(target=Speech_recognition.SpeechRecognition)
emotion.daemon = True
speech.daemon = True
speech.start()
emotion.start()
emotion.join()
speech.join()



