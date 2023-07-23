import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
# reating  recogniser or listener
listener = sr.Recognizer()
engine = pyttsx3.init()
#choose a kind of voice ie female
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#initiate conversation
def talk(text):
    engine.say(text)
    engine.runAndWait()

# sometime microphone might not work so
def take_command():
    try:
        with sr.Microphone() as source:
            engine.say('listening...')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
               #removing alexa from the string if it exists
               command = command.replace('alexa', '')
               print(command)
    except:
        pass
    return command
#run function
def run_alexa():
    command = take_command()
    print(command)
    #ie playing a song
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('current time is '+time)
    elif 'who is ' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry , i have a headache')
    elif 'are you single' in command:
        talk('i an in a relationship with WIFI')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again')
    #make it quite

while True:
    run_alexa()