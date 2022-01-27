import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import json
import sys
from random import randrange

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tars' in command:
                command = command.replace('tars', '')
                print(command)
    except:
        pass
    return command


def run_tars():
    try:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
        elif 'date' in command:
            date = datetime.datetime.now().strftime("%b %d %Y")
            talk('Today\'s date is' + date)
        elif 'tell me a joke' in command:
            talk(pyjokes.get_joke())
        elif 'repeat' in command:
            sente = command.replace('repeat', '')
            talk(sente)
        elif 'tell me a headline' in command:
            def get_news():
                url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=ae5ccbe2006a4debbe6424d7e4b569ec'
                news = requests.get(url).text
                news_dict = json.loads(news)
                articles = news_dict['articles']
                try:
                    return articles
                except:
                    return False
            talk(get_news()[randrange(7)]['title'])
        elif 'bye bye' in command:
            talk('ok I am happy to be of help')
            return True


    except:
        pass

def main():
    talk('I am ready to help you')
    while True:
        if (run_tars()) == True:
            sys.exit()


if __name__ == '__main__':
    main()