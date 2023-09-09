'''
import subprocess

def espeak(text: str, pitch: int=100) -> int:
    """ Use espeak to convert text to speech. """
    return subprocess.run(['espeak', f'-p {pitch}', text]).returncode

espeak ("hello world this is our iot device ")'''

import pyttsx3
 
def speak(text):
    engine = pyttsx3.init()
    engine.rate = 1000
    engine.say(text)
    engine.runAndWait()
 
 
speak('Hi there, what is your name?')