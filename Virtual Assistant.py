import speech_recognition as sr
import pyaudio
from time import ctime
import webbrowser as wb
import time
from gtts import gTTS
import os
import pyttsx3 as pt
import random
import playsound


def getv(ask=False):
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        r1.adjust_for_ambient_noise(source) 
        if ask:
            speak(ask)
        #print("Set minimum energy threshold to {}".format(r.energy_threshold))
        with sr.Microphone() as source: audio = r1.listen(source)
        voice = ''
        try:
            voice = r1.recognize_google(audio)  
        except sr.UnknownValueError: 
           speak('I did not get that')
        except sr.RequestError:
           speak('Sorry, the service is down. You are not connected to the internet. Try again when you are connected')
           exit()
        print(voice) 
        return voice.lower()

def speak(audi):
   
    engine = pt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    newVoiceRate = 130
    engine.setProperty('rate',newVoiceRate)
    engine.say(audi)
    engine.runAndWait()
    
def words(li,voice):
    for w in li:
        if w in voice:
            return True

def reply(voice):
    
    if words(["hello","hey","hi"],voice):
        greetings = ["hey, how can I help you ", "hey, what's up? ", "I'm listening", "hello"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        print(greet)
        speak(greet)
    if "how are you" in voice:
        ask=["I'm fine","I'm well,thank you,how can i help?","Pretty good what about you","Not too bad","Yeah, all right!"]
        askk = ask[random.randint(0,len(ask)-1)]
        print(askk)
        speak(askk)
    if "can i call you" in voice:
        print("But i already have a name")
        speak("But i already have a name, Avatar!")
    if "food recipes" in voice:
        url='https://google.com/search?q=food recipes'
        wb.get().open(url)
        print("Let's get cooking!")
        speak("Let's get cooking!")
    if "your name" in voice:
        print("My name is Avatar! always at your service")
        speak("My name is Avatar! always at your service")
    if "calculator" in voice:
        url='https://google.com/search?q=calculator online'
        wb.get().open(url)
        print("Calculator for you")
        speak("ohhh !I'm scared of maths")
    if "youtube" in voice:
        s=getv("What do you want to see?")
        url='https://youtube.com/search?q='+ s
        speak("On my way")
        wb.get().open(url)
        print("Here are the results")
        speak("Here are the results")
    if "time" in voice:
        print(ctime())
        speak(ctime())
    if "search" in voice:
        s=getv("What do u want 2 search")
        url='https://google.com/search?q=' +s
        wb.get().open(url)
        print("Here's what i found for "+ s)
        speak("Here's what i found for "+ s)
    if "location" in voice:
        loc=getv("What do u want 2 search")
        url='https://google.nl/maps/place/' +loc+ '/&amp;'
        wb.get().open(url)
        print("Here's what i found for "+ loc)
        speak("Here's what i found for "+ loc)
    if words(["exit", "quit", "goodbye","bye","byebye"],voice):
        bye=["Bye bye","Going offline","Come back soon"]
        byee=bye[random.randint(0,len(bye)-1)]
        print(byee)
        speak(byee)
        exit()    
        

time.sleep(1)
speak("How may I help you?")
while 1:
    voice=getv()
    reply(voice)
