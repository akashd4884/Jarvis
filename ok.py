import random
import sys
import time
import webbrowser
import pywhatkit
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import pyjokes
import pyautogui
import smtplib
import requests
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

#Tex to Speech converter
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert Voice to Text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source,timeout=10,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#To Wish
def wish():
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello I am Jarvis sir, Please Tell me how can i help you today")

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akd010801@gmail.com','Asaaakd4884')
    server.sendmail('akashkumardubey48@gmail.com', to, content)
    server.quit()
    speak("email has been sent to akash")

def news():
    main_url = 'https://newsapi.org//v2/top-headlines?sources=techcrunch&apiKey=9c9b2d37fcdc4b6595f63f75b86a96ef'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first","second","third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

if __name__ == "__main__":
    wish()
    while True:
    #if 1:

        query = takecommand().lower()

        #Logic Building For Tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")


        elif "open paint" in query:
            ppath= "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(ppath)

        elif "close paint" in query:
            speak("okay sir, closing paint")
            os.system("taskkill /f /im mspaint.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
                    cap.release()
                    cv2.destoryAllWindows()

        elif "play music" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif "ip address please" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your ip address is, {ip}")

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("According To wikipedia")
            speak(results)
            print(results)

        elif "email akash" in query:
            try:
                speak("sir what should i say")
                content = takecommand().lower()
                to = "akashkumardubey48@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to akash")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this email to akash")

        elif "tell me a joke" in query:
            jokes = pyjokes.get_joke()
            speak(jokes)

        elif"open google" in query:
            speak("sir, what should I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif"open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif"who is Rahul" in query:
            speak("Cricketer")

        elif"send whatsapp message"in query:
            pywhatkit.sendwhatmsg("+917022603574", "Yo",1,27)

            speak("message has been sent")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news updates" in query:
            speak("please wait sir, feteching the latest news updates")
            news()

        elif"no thanks" in query:
            speak("Thanks sir, Hope you have a great day!")
            sys.exit()

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        speak("Sir, Do you need any other help!")