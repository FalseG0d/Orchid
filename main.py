from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys
import os

from mind import *
from PyQt5.uic import loadUiType


ui,_=loadUiType('main.ui')


class MainApp(QMainWindow, ui):
    def __init__(self,parent=None):
        self.mind=Mind()
        if(self.mind.authorize()):
            self.mind.wishMe()
            super(MainApp,self).__init__(parent)
            QMainWindow.__init__(self)
            self.setupUi(self)
            self.InitUI()
            self.Handle_Buttons()
            self.label.setText("Press the Mic Button to Activate Command Mode")

    def InitUI(self):
        self.ApplyOrange()

    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.MicActivate)
        self.mind.speak("All the Functionalities have been loaded into the system")

    def MicActivate(self):
        self.label.setText("Listening...")
        self.mind.speak("I am Listening")
        query=self.mind.takeCommand()
        self.label.setText("User said: "+str(query))

        if query is None:
            self.mind.speak('Please Repeat the Command')
            #self.label.setText("Please Repeat the Command")
            
        elif 'wikipedia' in query.lower():# Search for x in wikipedia
            self.mind.speak('Searching in wikipedia...')
            query=query.split(' ')
            result=wikipedia.summary(query[2],sentences=2)
            print(result)
            self.mind.speak(result)

        elif 'website' in query.lower():#Open x website
            self.mind.speak('Initializing Web Browser...')
            query=query.split(' ')
            self.mind.speak("Looking for "+query[1])
            url=query[1]+".com"
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play' in query.lower():#Play x
            f_dir="C:\\Users\\ugarg\\Videos\\Captures"
            v_list=os.listdir(f_dir)

            os.startfile(os.path.join(f_dir, v_list[0]))

        elif 'time' in query.lower():#What's the time
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            self.mind.speak(f"The time is {strTime}")

        elif 'code' in query.lower():
            codePath="C:\\Users\\ugarg\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            self.mind.speak("Initializing Visual Studio Code")
            os.startfile(codePath)

        elif 'sleep' in query.lower():
            self.mind.speak("Ok, {MASTER} I am off!!")
            self.mind=None
            exit(0)

        self.label.setText("Press the Mic Button to Activate Command Mode")


    def ApplyOrange(self):
        self.setStyleSheet(None)
        style=open('themes/orange.css','r')
        style=style.read()
        self.setStyleSheet(style)

    def ApplyDark(self):
        self.setStyleSheet(None)
        style=open('themes/dark.css','r')
        style=style.read()
        self.setStyleSheet(style)
        
    def ApplyQDark(self):
        self.setStyleSheet(None)
        style=open('themes/qdark.css','r')
        style=style.read()
        self.setStyleSheet(style)

    def ApplyLight(self):
        self.setStyleSheet(None)
        style=open('themes/light.css','r')
        style=style.read()
        self.setStyleSheet(style)

    def ApplyNone(self):
        self.setStyleSheet(None)


def main():
    
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()

        
if __name__=='__main__':
    main()
