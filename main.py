import os
import random
from gtts import gTTS
import playsound
from wikipedia import wikipedia


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


try:
    a = str(input('Enter Number: '))
    wiki = wikipedia.summary(a)
    speak(audio_string=wiki)

except:
    print("This isn't valid value")