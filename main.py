import speech_recognition as sr
def command():
    r = sr.Recognizer() #create an instance of the speech recognizer class
    with sr.Microphone() as source:
        print("Cher: listening...")
        audio=r.listen(source) #listens to the microphone as the audio source
        try:
            query=r.recognize_google(audio)
            print(f"master:{query}")
            return query
        except:
            print("Try again!")

print(command())