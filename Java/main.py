import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechrecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


print("initializing Jarvis")

MASTER = "Moses"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function will pronouce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("initializing Jarvis...")
# speak("Adewara mose is a good boy")

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    #speak("I am jarvis. How may I help you?")

# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login('adewarasalvation56@gmail.com', 'Adewara1')
    server.sendmail("oluwadamilaremoses56@gmail.com", to, content)
    server.close()
# main Program starts here....
def main():
    #speak("initializing Jarvis...")
    wishMe()
    query = takeCommand()

    #  Logic for executing takes as per the query
    if query:
        if 'wikipedia' in query.lower():
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            print(results)
            speak(results)

        elif 'open youtube' in query.lower():
            #webbrowser.open("youtube.com")
            url = "youtube.com"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query.lower():
            #webbrowser.open("google.com")
            url = "google.com"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open reddit' in query.lower():
            #webbrowser.open("youtube.com")
            url = "reddit.com"

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play music' in query.lower():
            songs_dir = "C:\\Users\\ADEWARA MOSES\\Music\\music"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")

        elif 'open code' in query.lower():
            codePath = "C:\\Users\\ADEWARA MOSES\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to moses' in query.lower():
            try:
                speak("What should i send")
                content = takeCommand()
                to = "adewarasalvation56@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully")

            except Exception as e:
                print(e)

main()
