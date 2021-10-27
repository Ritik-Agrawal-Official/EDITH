import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak('Good Morning!!! EDITH Here. How may I help you?')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!!! EDITH Here. How may I help you?')
    else:
        speak('Good Evening!!! EDITH Here. How may I help you?')

def takeCommand():
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
        # print(e)    
        print("Try Again! I can't Recognize...")
        return "None"
    return query

def there_exists(terms):
    for term in terms:
        if term in query:
            return True

if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower()


        if there_exists(['hey','hi','hello']):
            greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
            greet = greetings[random.randint(0,len(greetings)-1)]
            speak(greet)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search' in query:
            search_term=query.split("search")[-1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            speak("Showing results for "+search_term)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif there_exists(["how are you","how are you doing"]):
            speak("I'm very well, thanks for asking ")

        elif there_exists(["make a note","make note","notes","note"]):
            search_term=query.split("for")[-1]
            url="https://keep.google.com/#home"
            webbrowser.get().open(url)
            speak("Here you can make notes")
        
        elif there_exists(["open my mail","gmail","check my email"]):
            search_term = query.split("for")[-1]
            url="https://mail.google.com/mail/u/0/#inbox"
            webbrowser.get().open(url)
            speak("here you can check your gmail")

        elif there_exists(["play music","play"]):
            search_term= query.split("play")[-1]
            url="https://www.youtube.com/search/?q="+search_term
            webbrowser.get().open(url)
            speak("You are listening to"+ search_term +"enjoy sir")
            
        elif there_exists(["weather","tell me the weather report","whats the condition outside"]):
            search_term = query.split("for")[-1]
            url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
            webbrowser.get().open(url)
            speak("Here is what I found for on google")
            
        elif there_exists(["toss","flip","coin"]):
            moves=["head", "tails"]   
            cmove=random.choice(moves)
            speak("Tossing a Coin!!!")
            speak("And it's a " + cmove)
            
        elif there_exists(["exit", "quit", "goodbye","bye"]):
            speak("goodday sir! see you soon")
            exit()

