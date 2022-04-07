#YOUR VOICE ASSISTANT
# import win32api
import sys
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechrecognition
import datetime #inbuilt
import wikipedia #pip install wikipedia
import webbrowser#inbuilt 
import os#inbuilt
import smtplib#inbuilt 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am your assistant sir,Please tell me how may i help you")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing..")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again plaese..")
            return "None"
        return query
if __name__ == "__main__":
    wishme()
    while True:
        query =takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            try:
                speak("What should i say?")
                content=takecommand()
            except Exception as e:
                print(e)
                speak("Sorry my friend,")