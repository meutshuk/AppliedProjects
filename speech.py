from flask import Flask, render_template, request
from chatterbot import ChatBot
import csv
from codes import sound, voice, weather, googleSearch
import os
from config import chatBG, botAvatar

application = Flask(__name__)
chatbotName = "Sidney"
confidenceLevel = 0.7

# Create Log file
try:
    file = open('BotLog.csv', 'r')
except IOError:
    file = open('BotLog.csv', 'w')

bot = ChatBot(
    "ChatBot",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': confidenceLevel,
            'default_response': 'IDK'
        }
    ],
    # response_selection_method=get_random_response, #Comment this out if you want best response
    # input_adapter="chatterbot.input.VariableInputTypeAdapter",
    # output_adapter="chatterbot.output.OutputAdapter",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="botData.sqlite3"
)

introduction = "Hello my name is Sidney. i am an A.I chatbot how can i help you"
# sound(introduction)
'''text = voice()

for i in text.split():
    if i == 'weather':
        weather(text)
        break'''


@application.route("/")
def home():
    return render_template("index.html", botName=chatbotName, chatBG='./static/apple.jpg', botAvatar=botAvatar)


@application.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botReply = str(bot.get_response(userText))
    if botReply is "IDK":
        botReply = str(bot.get_response('IDKnull'))  ##Send the i don't know code back to the DB
        # if useGoogle == "yes":
        botReply = botReply + googleSearch(userText)

    ##Log to CSV file
    print("Logging to CSV file now")
    with open('BotLog.csv', 'a', newline='') as logFile:
        newFileWriter = csv.writer(logFile)
        newFileWriter.writerow([userText, botReply])
        logFile.close()
    return botReply


if __name__ == "__main__":
    # application.run()
    application.run(host='0.0.0.0', port=80)
