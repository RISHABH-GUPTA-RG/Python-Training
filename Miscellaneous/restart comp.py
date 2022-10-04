# Import required modules
import pyttsx3
import time
import speech_recognition as sr
import os


# Creating class
class Main:

    # Method to give output commands
    def Speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

        # Method to take input voice commands

    def takeCommand(self):

        # This method is for taking
        # the commands and recognizing the command

        r = sr.Recognizer()
        # from the speech_Recognition module
        # we will use the recongizer method
        # for recognizing

        with sr.Microphone() as source:
            # from the speech_Recognition module
            # we will use the Microphone module for
            # listening the command

            print('Listening')
            # seconds of non-speaking audio
            # before a phrase is considered complete
            r.pause_threshold = 0.7
            audio = r.listen(source)

            try:
                print("Recognizing")
                Query = r.recognize_google(audio, language='en-in')

                # for listening the command
                # in indian english
                print("the query is printed='", Query, "'")

                # for printing the query or the
                # command that we give
            except Exception as e:

                # this method is for handling
                # the exception and so that
                # assistant can ask for telling
                # again the command
                print(e)

                print("Say that again sir")
                return "None"
            return Query

            # Method to restart PC

    def restart(self):
        self.Speak("do u want to switch off the computer sir")
        take = self.takeCommand()
        choice = take
        if choice == 'yes':
            print("Shutting down the computer")
            os.system("shutdown /s /t 30")
            self.Speak("Shutting the computer")
        if choice == 'no':
            print("Thank u sir")
            self.Speak("Thank u sir")

        # Driver Code


if __name__ == '__main__':
    Maam = Main()
    Maam.restart() 