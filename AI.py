import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime('%I:%M')
    speak(Time)
def wishMe():
    speak('Welcome back')
    speak("the current time is")
    time()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    elif hour>=18 and hour<20:
        speak("Good evening")
    else:
        speak("Good night")
    speak("How can i help you")
wishMe()
def takeCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing for you")
        question = r.recognize_google(audio,langauge = 'en-in')
        print(question)
    except Exception as e:
        print(e)
        speak("Sorry. I did not get you")
        return 'none'
    return question
takeCommands()