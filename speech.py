import requests
from flask import Flask, render_template, request
from chatterbot import ChatBot
from bs4 import BeautifulSoup
from codes import sound, voice
import os

application = Flask(__name__)
chatbotName = "Sidney"
confidenceLevel = 0.7

#Create Log file
try:
    file = open('BotLog.csv', 'r')
except IOError:
    file = open('BotLog.csv', 'w')

bote = ChatBot(
    name="ChatBot",
    logic_adapters=[

            'chatterbot.logic.BestMatch',
            'chatterbot.logic.TimeLogicAdapter',
            "chatterbot.logic.MathematicalEvaluation"
        ])




introduction = "Hello my name is Sidney. i am an A.I chatbot how can i help you"
sound(introduction)
text = voice()

for i in text.split():
    if i == 'weather':

        # creating url and requests instance
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
        break
