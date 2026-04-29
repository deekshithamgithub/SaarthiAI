from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text)
    tts.save("out.mp3")
    os.system("start out.mp3")