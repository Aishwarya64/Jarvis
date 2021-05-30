import os
import webbrowser
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import smtplib
import random


engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hr=int(datetime.datetime.now().hour)
    if hr >= 0 and hr < 12 :
        speak("Good Morning Aishwarya")
    elif hr >=13 and hr < 18 :
        speak("Good afternooon Aishwarya")
    else:
        speak("Good evening Aishwarya")
    speak("I am Jarvis . please tell me how may I help you")

def takecommand():
    reco=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        reco.pause_threshold = 1
        audio=reco.listen(source)

    try :
        print("Recognizing...")
        query=reco.recognize_google(audio, language='en-in')
        print("You said : {} ".format(query))
    except Exception as e:
        print("Say that again........")
        return "None"
    return query


def sendmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('aishwaryaaji702@gmail.com','Aishtcs@64')
    server.sendmail('aishwaryaaji702@gmail.com',to,content)
    server.close()





if __name__ == "__main__":
    wishme()
    while True:
        ask=takecommand().lower()
        if 'wikipedia' in ask:
            ask=ask.replace('wikipedia',"")
            resul=wikipedia.summary(ask,sentences=2)
            print(resul)
            speak("According to wikipedia")
            speak(resul)
        elif 'open youtube' in ask:
            webbrowser.open("youtube.com")
        elif 'open google' in ask:
            webbrowser.open("google.com")
        elif 'open stack overfow' in ask:
            webbrowser.open("youtube.com")
        elif 'play music' in ask:
            music_dir='D:\Abhishek\'s Files\\Trackmai bajhavu\\My Tracklist Skulltech'
            list=os.listdir(music_dir)
            print(list)
            #os.startfile(os.path.join(music_dir,list[0]))
            os.startfile(os.path.join(music_dir,random.choice(list)))
        elif 'time' in ask:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)
        elif 'open code' in ask:
            codepth="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepth)
        elif 'email to Hari' in ask:
            try:
                speak("What to say..")
                content=takecommand()
                to="aishwaryaaji6@gmail.com"
                sendmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                speak("Sorry my fried. Mail is not sent.")






