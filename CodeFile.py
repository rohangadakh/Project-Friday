import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import pywhatkit as kit
from playsound import playsound
from datetime import datetime
import wikipedia
import ChatBot

global query

'''
import pyttsx3 - this library is used to convert the text to speech.
This is not the built-in so it means that we have to import it for that use command : pip install pyttsx3 
'''

engine = pyttsx3.init('sapi5')
# Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft.
voices = engine.getProperty('voices')
engine.setProperty("rate", 165)  # This command is used to make slow the voice of sapi5
engine.setProperty('voice', voices[2].id)  # voices[0], voices[1], voices[2],


def wishMe():
    hour = int(datetime.now().hour)
    if 0 <= hour < 12:
        print("Good Morning \U0001F305")
        speak("Good Morning ! ")

    elif 12 <= hour < 18:
        print("Good Afternoon \U0001F929")
        speak("Good Afternoon !")

    else:
        print("Good Evening \U0001F303")
        speak("Good Evening !")
    print("Hello Admin, I am Friday what should I do for you ? ".title())
    speak("Hello Admin, I am Friday what should I do for you ? ")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening   - ")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=3)
    try:
        print("Recognising - ")
        query = r.recognize_google(audio, language='en-in')
        print("Admin : {}".format(query).capitalize())
    except:
        # print("Can you please say that again !")
        return "none"
    query = query.lower()
    return query


# The above three functions are compulsory ( wishMe(), speak(), takeCommand() )

def fridayExecution():  # The every method which is created will be added in this function and this function is called in the main function.

    while True:

        print()

        query = takeCommand()

        if "google.com" in query:  # To open a Google.com
            print(":     GOOGLE.COM      :")
            webbrowser.open("google.com")

        elif "send" in query:  # To send the whatsapp message
            print(":     WHATSAPP      :")
            speak("Tell me the contact name to send the message")
            print("Friday : Tell me the contact \U0001F4DE name to send the message".title())
            query = takeCommand()
            if "Contact_Name_1" in query:
                speak("sure")
                speak("Tell me the message send to Contact_Name_1")
                print("Friday : Tell me the message \U0001F4E7 send to Contact_Name_1".title())
                msg = takeCommand()
                print("Sending \U0001F4F2 message".title())
                speak("Sending message")
                kit.sendwhatmsg_instantly("Mobile No. With Country Code", msg)
            elif "Contact_Name_2" in query:
                speak("sure")
                print("Tell me the message send to Contact_Name_1".title())
                speak("Tell me the message \U0001F4E7 send to Contact_Name_1")
                msg = takeCommand()
                print("Sending \U0001F4F2 message".title())
                speak("Sending message")
                kit.sendwhatmsg_instantly("Mobile No. With Country Code", msg)
            else:
                print("Contact \U0001F4DE is not found : ", query)
                speak("Contact is not found")

        elif "youtube" in query:  # To play a YouTube video
            print(":     YOUTUBE      :")
            print("Which video \U0001F3A5 would you like to play ? ".title())
            speak("Which video would you like to play ? ")
            query = takeCommand()
            kit.playonyt(query)

        elif "game" in query:  # It opens the game
            print(":     GAME      :")
            print("Opening game \U0001F3AE ".title())
            webbrowser.open("https://doodlecricket.github.io/#/")
            
        elif "time" in query:  # Tells the time
            print(":     TIME      :")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time \U0001F552 : ", current_time)
            speak("The current time is ")
            speak(current_time)

        elif "wikipedia" in query:
            print(":     WIKIPEDIA      :")
            print("Tell me the topic on which you want the Information".title())
            speak("Tell me the topic on which you want the Information")
            query = takeCommand()
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "can" in query:  # This search the query
            print(":     Q & A      :")
            kit.search(query)
            return None
        
        elif "sleep" in query:
            print(":     SLEEP      :")
            print("Okie admin, I am going to sleep \U0001F634 now you can wake up me anytime".title())
            speak("Okie admin, i am going to sleep now you can wake up me anytime")
            break
        
        elif "exit" in query:
            print(":     EXIT      :")
            print("Exiting from the Friday Execution")
            print("Have greate day admin ! Good bye \U0001F44B".title())
            speak("Have greate day admin ! Good bye")
            quit()

       
if __name__ == '__main__':

    playsound("E:\\Friday\\FridayRingTone.wav")

    while True:

        permission = takeCommand()
        
        if "friday" in permission:
            print("In the Main")
            wishMe()
            fridayExecution()
        elif "exit" in permission:
            print("Exiting from the Main")
            speak("Have greate day admin, Good bye !")
            print("Have greate day admin, Good bye \U0001F44B".title())
            quit()
        elif 1 == 1:
            reply = ChatBot.chatingBot(permission)
            speak(reply)
            
