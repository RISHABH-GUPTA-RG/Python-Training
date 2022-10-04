# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
# importing Py what kit
import pywhatkit as kit

# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
    return Query

# creating Speak() function to giving Speaking power to our voice assistant
def Speak(audio):# initializing pyttsx3 module
    engine = pyttsx3.init()# anything we pass inside engine.say(),will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()

# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        
        if command not in ('None','none',None):
            if "exit" in command:
                Speak("Sure sir! as your wish, bai")
                break
            elif "best model" in command:
                Speak("best model in universe is rishabh gupta ")
            elif "bye" in command:
                Speak("Sure sir! as your wish, bai")
                break
            else:
                Speak(command)
                Speak("Do you want to Search for it sir?")
                query=take_commands()
                if query in ("Yes","yes"):
                    if "search" in command:
                        command.replace("search",'')
                        kit.search(command)
                    else:
                        try:
                            Speak(kit.info(command))
                        except:
                            kit.search(command)