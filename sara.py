import speech_recognition as sr
from gtts import gTTS
import os
import google.generativeai as genai

genai.configure(api_key="replace with your api key")
model = genai.GenerativeModel('gemini-pro')
recognizer = sr.Recognizer()
while True:
  with sr.Microphone() as source:
      print("Speak now...")
      audio = recognizer.listen(source)
    
  try:
      # Use Google Speech Recognition
      text = recognizer.recognize_google(audio)
      print("You said: " + text)
      if (text.lower() == "stop"):
        exit(0)
      
      response = model.generate_content(text)
      print(response.text)
      
      
      # Convert text to speech
      tts = gTTS(text=response.text, lang='en')
      tts.save("output.mp3") 
      # Play the audio using OS module
      os.system("start output.mp3")
    
  except sr.UnknownValueError:
      print("Could not understand audio")
  except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))
