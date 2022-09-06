import sys

import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import time
import requests
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.encoders import encode_base64


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query


# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour > 12 and hour < 16:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("I am jarvis, How can i help you today")


# To send Email
def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akd010801@gmail.com','Asaaakd4884')
    server.sendmail('akd010801@gmail.com', to, content)
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

        # logic building for task

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open paint" in query:
            ppath = "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(ppath)

        elif "open powerpoint" in query:
            tpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
            os.startfile(tpath)

        elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
                    cap.release()
                    cv2.destroyAllWindows()

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "play music" in query:
            music_dir = "D:\\New folder\\project music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")

        elif "open my gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+917022603574", "hello", 17, 50)

        elif "drop my needle" in query:
            kit.playonyt("iron man centuries")

        elif "email akash" in query:
            try:
                speak("sir what should i say")
                query = takecommand().lower()
                if "send a file" or "attach a file" in query:
                    email= 'akd010801@gmail.com'
                    password = 'Asaaakd4884'
                    send_to_email = "akashkumardubey48@gmail.com"
                    speak("okay sir, what is the subject for this email")
                    query= takecommand().lower()
                    subject = query
                    speak("and sir, what is the message for this email")
                    query2 = takecommand().lower()
                    message = query2
                    speak("sir please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here")
                    speak("please wait i am sending the email now")

                    msg = MIMEMultipart
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    msg.attach(part)
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('akd010801@gmail.com', 'Asaaakd4884')
                    text = msg.as_string()
                    server.sendmail('akd010801@gmail.com', send_to_email, text)
                    server.quit()
                    speak("email has been sent to akash")

                sendEmail(to, content)
                speak("Email has been sent to akash")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this email to akash")

        elif "close notepad" in query:
            speak("okay sir closing notepad")
            os.system('taskkill /f /im notepad.exe')

        elif "close paint" in query:
            speak("okay sir closing paint")
            os.system('taskkill /f /im mspaint.exe')

        elif "close powerpoint" in query:
            speak("okay sir closing power point")
            os.system('taskkill /f /im POWERPNT.exe')

        elif "go to sleep" in query:
            speak("thanks for using me sir have a great day.")
            sys.exit()

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("round1132.exe powrprof.d11,SetSuspendStae 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.keyUp("alt")

        elif "tell me news updates" in query:
            speak("please wait sir, feteching the latest news updates")
            news()

