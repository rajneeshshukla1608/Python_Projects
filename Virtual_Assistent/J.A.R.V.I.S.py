import pyttsx3
import webbrowser
import datetime
import wikipedia
# import playsound
import os
# import smtplib
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)

fathername = ""


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def starter():
    time = int(datetime.datetime.now().hour)
    if 0 <= time < 12:
        speak("Good Morning Sir..")
        print("Good Morning Sir..")
    elif 12 >= time < 18:
        speak("Good afternoon Sir..")
        print("Good afternoon sir..")
    else:
        speak("Good evening Sir..")
        print("print Good evening sir..")


starter()
speak("I am Friday your new virtual assistant how may I help you..")
print("I am your new virtual assistant how may I help you..")


# we can use engine.speak(), engine.say(), pyttsx.speak(), speak()

def recognize():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(f"say that again please{Exception}")

    return query


query = recognize().lower()

if "google" in query:
    speak("we got it opening google")
    webbrowser.open('https://www.google.com/')
    print("opened")

elif "youtube" in query:
    speak("we got it opening youtube")
    webbrowser.open_new_tab('https://www.youtube.com/')

elif "browser" in query:

    webbrowser.open('chrome')

elif "code" in query:
    path = "C:\\Users\\Lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
    os.startfile(path)

elif "the time" in query:
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {time}")

elif "wikipedia" in query:
    speak("we found")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=2)
    engine.setProperty('rate', 178)
    speak("According to wikipedia")
    speak(result)

elif ("what" or "who") in query:
    speak("Searching...")
    query = query.replace("is", "")
    result = wikipedia.summary(query, sentences=1)
    engine.setProperty('rate', 178)
    speak("we found")
    speak(result)

elif 'day' in query:
    day = datetime.date.today()
    speak(day)

elif 'father' in query:
    if fathername == "":
        speak("There is nothing related to your father")
        speak("want to tel us his name..")
        fat_recog = recognize().lower()
        fathername.replace(fat_recog)
        speak(f"Ok sir your father name is {fathername}")

    else:
        speak(f"Your father name is {fathername}")

elif "play music" in query:
    music_dir = "E:\\movies\\gane"
    gane = os.listdir(music_dir)
    speak("Playing music")
    os.startfile(os.path.join(music_dir, gane[0]))

elif "shutdown" in query:
    # dir = "C:\\Windows\\System32\\shutdown"
    os.system('shutdown -h')
    # os.startfile(dir)

elif "down" in query:
    engine.setProperty("volume", 0.3)
    engine.say("ok Volume down")
    engine.runAndWait()


elif "up" in query:
    engine.setProperty('volume', 1.0)
    engine.say("ok Volume up")
    engine.runAndWait()


elif "fast" in query:
    engine.setProperty('rate', 200)
    engine.say("ok I will be speaking fast")
    engine.runAndWait()

elif "lo" in query:
    engine.setProperty("rate", 150)
    engine.say("I am the text spoken after changing the speech rate.")
    engine.runAndWait()