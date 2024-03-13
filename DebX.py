import speech_recognition as sr
import pyttsx3
import os, sys
import google.generativeai as genai

# Configure GenerativeAI model
genai.configure(api_key="Your API Key")
model = genai.GenerativeModel('gemini-pro')

# Define speech rate
speech_rate = 180

engine = pyttsx3.init()
engine.setProperty('rate', speech_rate)  # Set speech rate once

while True:
    print("Ask me anything!")
    engine.say("Ask Me")
    engine.runAndWait()

    try:
        x = str(input())
        if x.lower() in ("w", "s"):
            if x.lower() == "s":
                recognizer = sr.Recognizer()
                with sr.Microphone() as source:
                    engine.say("Say..")
                    engine.runAndWait()
                    print("Speak Now..")
                    audio = recognizer.listen(source)

                try:
                    text = recognizer.recognize_google(audio)
                    if text.lower() == "stop":
                        sys.exit(0)

                    response = model.generate_content(text)
                    print(response.text)
                    engine.say(response.text) 
                    engine.runAndWait()

                except sr.UnknownValueError:
                    print("Couldn't hear you, Sorry!")
                    engine.say("Could you please repeat..")
                    engine.runAndWait()

                except sr.RequestError as e:
                    print("Server is down...")
                    engine.say("Oops! Server is down..")
                    engine.runAndWait()

            else: 
                print("Write now..")
                text = str(input())
                if text.lower() == "stop":
                    sys.exit(0)

                response = model.generate_content(text)
                print(response.text)
                print("Do you want me to say this?")
                engine.say("Would you like to hear my response.")
                engine.runAndWait()
                z = str(input(""))
                if z.lower() == "y":
                    engine.say(response.text)
                    engine.runAndWait()

        else:
            print("Use W or S")
            engine.say("Use W or S..")
            engine.runAndWait()

    except SystemExit:
        engine.say("Shutting Down..")
        engine.runAndWait()
        sys.exit(0)

    except:
        engine.say("Error has occurred.. Retry! or Close Window.")
        engine.runAndWait()
