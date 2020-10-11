import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import *
import random
from time import ctime # get time details
import webbrowser # open browser
import yfinance as yf # to fetch financial data
import ssl
import certifi
import time
import os # to remove created audio files
line=""
cnt=0
words=[]

def convert(lst): 
    return line.split()

def main():
    global words
    global line 
    print(line)
    complete_words=convert(line)
    for i in complete_words:
        if i =="room" or i=="Room" or i== "room1" or i== "Room1" or i== "room2" or i== "Room2" or i== "1" or i== "2" or  i=="kitchen" or  i=="Kitchen" or  i=="hall" or  i=="Hall" or i== "charging" or  i=="Charging":
            words.append(i)

def searchRooms():
    global words
    global line
    for i,word in enumerate(words):
        if word.isdigit():
            if i>0:
                words[i-1]=words[i-1]+word
                words.pop(i)
    return words
def word():
    global words
    global line
    print("The appended words are :",words)
    co=0
    for i in words:
        if i=="room1" or i=="Room1":
            speak("going to room one")
            os.system("python temp.py")
            speak("reached room one")
        if i=="room2" or i=="Room2":
            speak("going to room two")
            os.system("python temp.py")
            speak("reached room two")
        if i=="kitchen" or i=="Kitchen":
            speak("going to kitchen")
            os.system("python temp.py")
            speak("reached kitchen")
        if i=="hall" or i=="Hall":
            speak("reached hall")
            os.system("python temp.py")
            speak("reached hall")
        if i=="charging" or i=="Charging":
            speak("going to cahrging port")
            os.system("python temp.py")
            speak("reached cahrging port")
        words.pop(co)
        co=co+1




def excecute():
    main()
    searchRooms()
    word()
class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() 
def record_audio(ask=False):
    global words
    global line
    global cnt
    import pyaudio
    import speech_recognition as sr
    print("speak")

    r=sr.Recognizer()
    r.energy_threshold=3000
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) 
        audio=r.listen(source)

    voice_data=""
    try:
        voice_data = r.recognize_google(audio)  # convert audio to text
        line=voice_data
        excecute()
    except LookupError:
        print("Oops! Didn't catch that")
    except sr.UnknownValueError: # error: recognizer does not understand
        pass
    except sr.RequestError:
        speak('Sorry, the service is down') # error: recognizer is not connected
    print(voice_data.lower()) # print what user said
    return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) 
    playsound.playsound(audio_file) 
    print({audio_string}) 
    os.remove(audio_file)

def respond(voice_data):
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you ", "hey, what's up?", "I'm listening ", "how can I help you? ", "hello "]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)
    if there_exists(['hey','hi','hello']):
        print("jo",voice_data)

time.sleep(1)

person_obj = person()
speak("please tell me where to go")
while(1):
    #os.system("play beep-08b.wav")
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond


