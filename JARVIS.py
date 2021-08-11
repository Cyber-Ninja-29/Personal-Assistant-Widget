import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sir")
    elif hour>=12 and hour<4:
        speak("Good afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am your Assistant JARVIS")
    
def takeCommand():
    # takes my command from microphone and gives text
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry Sir, can you repeat that again?")
        return takeCommand()
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        speak("what is your Query Sir")
        query = takeCommand()
        if 'wikipedia' in query:
                speak("searching in wikipedia")
                query = query.replace("wikipedia", " ")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/?gl=IN')
            speak("youtube is opened")
        elif 'open google' in query:
            webbrowser.open('google.com')
            speak("google is opened")
        elif 'open gmail' in query:
            webbrowser.open('gmail.com')
            speak("gmail is opened")
        elif 'open Whatsapp' in query:
            webbrowser.open('web.whatsapp.com')
            speak("whatsapp is opened")    
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is {strTime}")
        elif 'break the operation' in query:
            speak("see you soon Sir")
            break
        else :
            webbrowser.open(query)
      
