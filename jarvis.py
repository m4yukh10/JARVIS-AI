#jarvis banachi
import openai
import speech_recognition as sr
import pyttsx3
import os

def api_response(message):
    API_KEY = os.getenv('API_KEY')
    openai.api_key = API_KEY
    completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content":message}]
)
    response = completion.choices[0].message.content
    return response
    
recognizer = sr.Recognizer()
engine = pyttsx3.init()

#kotha bolche
engine.setProperty('rate', 150) 
engine.setProperty('volume', 0.9) 
engine.say("Hello, I am Jarvis! How can I help you, Sir?: ")
engine.runAndWait()

close = False
context_var = "" 
while close != True:
    with sr.Microphone() as source:
        print("Speak now...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=3)
            text = recognizer.recognize_google(audio_data)
            context_var = context_var + text
            if len(text) == 0:
                engine.say("say something, sir.")
                engine.runAndWait()   
            if text.lower() != "quit":
                boleche = api_response(context_var + "answer the last question only")
                print("you said:", text)
                engine.say(boleche)
                engine.runAndWait()
                    
            else:
                engine.say("thank you!")
                engine.runAndWait()
                close = True  
                context_var = ""  
                 
        except sr.UnknownValueError:
            engine.say("Couldn't hear what you said. Please say it again!")
            engine.runAndWait()
        
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}") 
