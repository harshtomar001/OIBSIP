import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def assistant():
    speak("Hello! I am your voice assistant.")
    
    while True:
        command = listen()

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")

        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "your name" in command:
            speak("I am a simple Python voice assistant.")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        elif command != "":
            speak("I can do simple tasks like telling time or opening websites.")

assistant()
