import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time

# Initialize speech recognition engine and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greet the user
speak("Hi, I am your personal voice assistant. How can I help you?")

# Loop to listen for user input
while True:
    # Reset the microphone source and device index
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 4000
        print("Listening...")
        audio = r.listen(source, timeout=10, phrase_time_limit=15)

    # Try to recognize the user's speech
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}")

        # Process user input
        if 'wikipedia' in query.lower():
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query.lower():
            speak('Opening YouTube...')
            webbrowser.open('https://www.youtube.com')

        elif 'open google' in query.lower():
            speak('Opening Google...')
            webbrowser.open('https://www.google.com')

        elif 'time' in query.lower():
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif 'open code' in query.lower():
            speak('Opening Visual Studio Code...')
            os.startfile("C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'stop listening' in query.lower():
            speak("Stopping listening...")
            break

        else:
            speak("Sorry, I didn't understand that. Could you please repeat?")

    # If speech cannot be recognized
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that. Could you please repeat?")

    time.sleep(3)  # Wait for 3 seconds between each iteration
