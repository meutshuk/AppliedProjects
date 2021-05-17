from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot=ChatBot('ChatBot',

        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database='./data.sqlite3')

chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train('chatterbot.corpus.english')
#chatbot.train('train.json')
