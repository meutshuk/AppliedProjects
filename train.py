from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#For getting the spreadsheet data from csv
import os
import csv

import logging
logging.basicConfig(level=logging.INFO)

with open('data/trainingdata.yml', 'w') as f:
    f.write("categories:\r\n")
    f.write("- Conversations")
    f.write("\r\nconversations:")