import sys
from time import time
import pyjokes
import pyttsx3
import requests 
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from requests import get
import pywhatkit as kit
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def news():
    #news at line 210
    m_url= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=be7eec3279ed428f96ff1115818e7f8f"
    m_page =requests.get(m_url).json()
    articles= m_page['articles']
    head = []
    day= ["first", "second" ,"third" ,"fourth","fifth","Sixth" ,"Seventh","Eighth","nineth","Tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is {head[i]}")    


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("what should i search on google")
            cd= takeCommand().lower()
            webbrowser.open("{cd}")

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com") 

        elif  'open amazon' in query:
            speak("opening amazon")
            webbrowser.open("amazon.com")  

        elif  'open flipkart' in query:
            speak("opening flipkart")
            webbrowser.open("flipkart.com")

        elif  'open faceboook' in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")

        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\user\\Music\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "F:\\vs code\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif ' open my file' in query:
            filepath="F:\\" 
            speak("opening")
            os.startfile(filepath)

        elif 'open photos' in query:
            picpath = "E:\\New folder"
            speak("opening")
            os.startfile(picpath) 

        elif ' show news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India')    
        
        elif 'who are you' in query or 'what can you do' in query:
            speak("I m Jarvis 1 point o. I m made by Ashu. I can open different websites like gooogle,youtube"
                   "Gmail,facebook and many more. I can also get data from wikipedia and also predict weather")
            print("I m Jarvis 1 point o. I m made by Ashu. I can open different websites like gooogle,youtube"
                   "Gmail,facebook and many more. I can also get data from wikipedia and also predict weather")

        elif 'who made you' in query or 'what is your master' in query or 'who created' in query: 
            speak("I am  made by ASHU")
            print("I am  made by ASHU ")  

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'open notepad' in query:
            path = "C:\\Windows\\system32\\notepad.exe"
            speak("opening")
            os.startfile(path) 

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'ip address' in query:
            ip=get('https://api.ipify.org').text 
            speak(f'Your Ip address is{ip}')   

        # elif 'send message' in query:
        #    kit.sendwhatmsg('+917854880996', 'sdhgdfkghghbfhhjhnlkfh', 12,37)

        elif 'shutdown' in query: 
            speak("Shutting down")
            os.system("shutdown /s /t 1")

        elif 'restart' in query:        
            speak("Restarting.....")
            os.system("shutdown /r /t 1") 

        elif 'no thanks' in query:
            sys.exit()
        
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'tell news' in query:
            speak("Please Wait,fetching the latest News")
            news()   


        speak("Sir Do you have any other work")


       