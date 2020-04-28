import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

class Mind:

    #Constructor
    def __init__(self):
        self.master="Apoorv"
        self.speak("Initializing Orchid")

    def authorize(self):
        self.speak("No functionalities are available rightnow.....You first must load them into the system")
        while(True):
            self.speak("How can I help you??")
            speaker=str(self.takeCommand())
            if "come to life" in speaker.lower():
                engine.setProperty('voice',voices[1].id)
                return True
            else:
                self.speak("No functionalities are available right now")

    #Pronounces String
    def speak(self,text):
        engine.say(text)
        engine.runAndWait()
    #Greeting Function
    def wishMe(self):

        hour=int(datetime.datetime.now().hour)

        if hour>=0 and hour <12:
            self.speak("Godd Morning "+self.master)
        elif hour>=12 and hour<=18:
            self.speak("Godd Afternoon "+self.master)
        else:
            self.speak("Godd Evening "+self.master)

    #Take voice command
    def takeCommand(self):
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


