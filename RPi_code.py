#sudo nano /home/pi/.bashrc
#echo Running at boot 
#sudo python /home/pi/sample.py


import os  # accessing the os functions
import os

import os
import speech_recognition as sr
import pyttsx3
import time
import warnings
warnings.filterwarnings("ignore")
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.setProperty('rate',170)
    engine.say(command)
    engine.runAndWait()

    
r = sr.Recognizer()


    
def speach():
    while(1):
        try:
            print('start speaking...')
            # use the microphone as source for input. 
            with sr.Microphone() as source1:                                
                r.adjust_for_ambient_noise(source1, duration=.5) 
                            
                audio2 = r.listen(source1) 
                print("Stop speaking until get response...!")
                            
                MyText = r.recognize_google(audio2) 
                MyText = MyText.lower()

                print("you: "+MyText)
                time.sleep(.2)
                break
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e)) 
                    
        except sr.UnknownValueError: 
            print("unknown error occured")
    return MyText

# The text that you want to convert to audio
mytext = ' Hello Welcome to Chat bot System'

SpeakText(mytext)

# for fetching wikipedia articles 
import wikipedia 

while (1):
          txt2=speach()
          
          if txt2=='Exit' or txt2=='exit' or txt2=='EXIT':
              SpeakText('Thank you for using chatbot')
              break
          else:
              print(wikipedia.summary(txt2, sentences = 1))
              SpeakText(wikipedia.summary(txt2,sentences = 1))

    

