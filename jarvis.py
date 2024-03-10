import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import sys
import pyjokes

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#To convert text to voice
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :{query}")

    except Exception as e:
        speak("say that again please")
        return "none"
    return query

#To wish
def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning sir")
    elif hour>12 and hour<18:
        speak("good afternoon sir")
    else:
         speak("good evening sir")
    speak("i am jarvis . please tell me how can i help you")


if __name__=="__main__":
    wish()
    while True:

        query = takecommand().lower()

        #logic building for task

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open cmd" in query:
            os.system('start cmd')

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img =cap.read()
                cv2.inshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
                cap.release()
                cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\PC\\Music\\music"
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia..")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "play song on youtube" in query:

            pywhatkit.playonyt("kyon")

        elif "joke" in query:
            joke =pyjokes.get_joke()
            speak(joke)

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "shutdown the system" in query:
            os.system("shutdown /s")

        elif "restart the system" in query:
            os.system("shutdown /r /t s")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dill,SetSuspendState 0,1,0")



        elif "no thanks" in query:
            speak("thanks for using me sir , have a good day")
            sys.exit()

        speak("sir , do you have any other work")














