
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        return 0
    return query


def search_web(input):
    driver = webdriver.chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower():

        speak("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():

        speak("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        else:

            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))

        return


# function used to open application
# present inside the system.
def open_application(input):
    if "chrome" in input:
        speak("opening Google Chrome")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Chrome')
        return

    elif "firefox" in input or "mozilla" in input:
        speak("Opening Mozilla Firefox")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox')
        return

    else:

        speak("Application not available")
        return


def process(input):
    try:
        if 'search' in input:
            # a basic web crawler using selenium
            search_web(input)
            return

        elif "who are you" in input or "define yourself" in input:
            say = '''Hello, I am Jarvis. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra'''
            speak(say)
            return

        elif "who made you" in input or "created you" in input:
            say = "I have been created by Rishu."
            speak(say)
            return

        elif "calculate" in input.lower():

            # write your wolframalpha app_id here
            app_id = "828XER-4EKQ5V74K7"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print(answer)
            speak("The answer is " + answer)
            return

        elif 'open' in input:

            # another function to open
            # different application availaible
            open_application(input.lower())
            return

        else:

            speak("I can search the web for you, Do you want to continue?")
            ans = takeCommand()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except:

        speak("I don't understand, I can search the web for you, Do you want to continue?")
        ans = takeCommand()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)
        else:
            return





        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour < 12:
            speak("Good Morning Professor!")

        elif hour >= 12 and hour < 15:
            speak("good Afternoon Professor!")

        else:
            speak("Good Evening Professor!")

        speak("what can i do for you?")

        while (1):
            query = takeCommand()

            if query == 0:
                speak("sorry! i can't hear that")
                continue

            query.lower()

            if "how are you" in query or "What's up" in query:
                speak("I am good Professor.How are you today?")
                ans = takeCommand()
                if "good" in ans or "fine" in ans or "great" in ans:
                    speak("that's great, any work for me Professor")
                else:
                    speak("get well soon,Professor")

            elif "exit" in str(query) or "bye" in str(query) or "sleep" in str(query):
                speak("see you soon Professor,bye!")
                break
            else:
                process(query)


if __name__=="__main__":
    
        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour < 12:
            speak("Good Morning Professor!")

        elif hour >= 12 and hour < 15:
            speak("good Afternoon Professor!")

        else:
            speak("Good Evening Professor!")

        speak("what can i do for you?")

        while (1):
            query = takeCommand()

            if query == 0:
                speak("sorry! i can't hear that")
                continue

            query.lower()

            if "how are you" in query or "What's up" in query:
                speak("I am good Professor.How are you today?")
                ans = takeCommand()
                if "good" in ans or "fine" in ans or "great" in ans:
                    speak("that's great, any work for me Professor")
                else:
                    speak("get well soon,Professor")

            elif "exit" in str(query) or "bye" in str(query) or "sleep" in str(query):
                speak("see you soon Professor,bye!")
                break
            else:
                process(query)