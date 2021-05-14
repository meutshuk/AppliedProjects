import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import requests
from bs4 import BeautifulSoup

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

def googleSearch(text):
    return "Why dont you look at google: <a target='_blank' href='https://www.google.com/search?q=" + text + "'>" + text + "</a>"

def weather(text):
    url = "https://www.google.com/search?q=" + text
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    loc = soup.find('span', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # printing all data
    speakWord = "Today is " + time + " in " + loc + " with temperature of " + temp + " and " + sky + " sky"
    print(speakWord)
    sound(speakWord)