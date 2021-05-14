import speech_recognition as sr
import playsound
from gtts import gTTS
import os

def sound(textt):
    tts = gTTS(text=textt, lang='en')
    filename = 'temp.mp3'
    tts.save(filename)

    playsound.playsound(filename)
    os.remove(filename)  # remove temperory file

def voice():
    global text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        audio = r.listen(source)
    try:
        print('analysing')
        return r.recognize_google(audio)

    except sr.UnknownValueError:
        print("Could not understand audio")