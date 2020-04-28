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
        self.pushButton_2.clicked.connect(self.TextActivate)
    def TextActivate(self):
        self.mind.speak("Command Received Succesfully")
        query=self.lineEdit.text()
        self.executeQuery(query)

    def MicActivate(self):
        self.label.setText("Listening...")
        self.mind.speak("I am Listening")
        query=self.mind.takeCommand()
        self.label.setText("User said: "+str(query))

        self.executeQuery(query)

        self.label.setText("Press the Mic Button to Activate Command Mode")

    def executeQuery(self,query):
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
        
        elif 'theme' in query.lower():
            self.mind.speak("You can choose one of the following theme\n1. Dark\n2. Light\n3. Original\n4. Grey\n")
            
            if 'dark' in query.lower():
                self.ApplyDark()
            elif 'light' in query.lower():
                self.ApplyLight()
            elif 'original' in query.lower():
                self.ApplyOrange()
            elif 'grey' in query.lower():
                self.ApplyQDark()
            else:
                pass
            

        elif 'sleep' in query.lower():
            self.mind.speak("Ok, {MASTER} I am off!!")
            self.mind=None
            exit(0)

        query=self.lineEdit.setText("")



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
