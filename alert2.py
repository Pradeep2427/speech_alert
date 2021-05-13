import speech_recognition as sr
from playsound import playsound
import winsound as ws

global alert_list
alert_list = []

def beep():
    freq = 5000
    duration = 1000
    for _ in range(2):
        ws.Beep(freq,duration)

def check(to_check):
    global alert_list
    for i in alert_list:
        check = map(lambda x:x.lower(),to_check)
        if i in check:
            print("beep beep beep")
            beep()
    return
    
    
def google_recognizer(speech):
    #rec = sr.Recognizer()
    #mic = sr.Microphone()
    try :
        audio = rec.recognize_google(speech)
        print(audio)
        to_check = audio.split(" ")
        print(to_check)
        check(to_check)
    except sr.UnknownValueError as err:
        print (err)
        print("err 1")
        pass
    except sr.RequestError as err:
        print(err)
        print("err2")
        pass
    except KeyboardInterrupt as err:
        print (err)
        pass
    return
    
for i in range(5):
    alert_word = input("Enter the alert word : ")
    if alert_word == '':
        break
    alert_list.append(alert_word)

while True:
    rec = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print('All Set')
        speech = rec.listen(source)
        rec.adjust_for_ambient_noise(source)
        print (speech)
        google_recognizer(speech)

