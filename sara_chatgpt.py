import speech_recognition as sr
from gtts import gTTS
import os
from openai import AsyncOpenAI


async def process_and_respond(text):
  """
  Asynchronous function to call OpenAI API and handle response.
  """
  if not os.environ.get('OPENAI_API_KEY'):   #AIzaSyCL6z0Cfo5OjszrjHD3uKcOyyuZ0SYVoo8    GEMINI
      raise ValueError("Missing API key. Please set the environment variable 'OPENAI_API_KEY'.")
  client = AsyncOpenAI(api_key=os.environ.get('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'))
  response_text = await client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}])
  # Access the first response text
  return response_text.choices[0].text 


async def main():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Speak now...")
    audio = recognizer.listen(source)

  try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)

    # Await the response from the asynchronous function
    response_text = await process_and_respond(text)
    print("AI Response:", response_text)

    # Text-to-speech (optional)
    tts = gTTS(text=response_text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")  # Play the audio (uncomment if needed)

  except sr.UnknownValueError:
    print("Could not understand audio. Please try again.")
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
  except ValueError as e:
    print(e)  # Print error message related to missing API key

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())
