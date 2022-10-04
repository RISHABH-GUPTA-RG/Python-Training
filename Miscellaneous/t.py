import pyttsx3
engine = pyttsx3.init()

engine.say("MADE BY RISHABH GUPTA")
engine.runAndWait()

while True:
    
    text = input("Enter the text : ")

    engine.say(text)

    engine.runAndWait()

    x=("Do you want to continue (y/n) :-> ")
    if x=='y':
        print("As your wish")
        engine.say("AS YOUR WISH")
        print()
    else:
        break
