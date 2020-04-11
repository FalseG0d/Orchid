import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

MASTER="Apoorv"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#Pronounces String
def speak(text):
    engine.say(text)
    engine.runAndWait()
#Greeting Function
def wishMe():

    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Godd Morning "+MASTER)
    elif hour>=12 and hour<=18:
        speak("Godd Afternoon "+MASTER)
    else:
        speak("Godd Evening "+MASTER)

    speak(", I am Orchid. How may I help you?")
#Take voice command
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Please Repeat: "+str(e))
        query=None
    
    return query

speak("Initializing Orchid...Listening")
wishMe()

while(True):

    query=takeCommand()

    if query is None:
        continue
        
    elif 'wikipedia' in query.lower():# Search for x in wikipedia
        speak('Searching in wikipedia...')
        query=query.split(' ')
        result=wikipedia.summary(query[2],sentences=2)
        print(result)
        speak(result)

    elif 'website' in query.lower():#Open x website
        speak('Initializing Web Browser...')
        query=query.split(' ')
        speak("Looking for "+query[1])
        url=query[1]+".com"
        chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play' in query.lower():#Play x
        f_dir="C:\\Users\\ugarg\\Videos\\Captures"
        v_list=os.listdir(f_dir)

        os.startfile(os.path.join(f_dir, v_list[0]))

    elif 'time' in query.lower():#What's the time
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'code' in query.lower():
        codePath="C:\\Users\\ugarg\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Initializing Visual Studio Code")
        os.startfile(codePath)

    elif 'sleep' in query.lower():
        speak("Ok, {MASTER} I am off!!")
        break