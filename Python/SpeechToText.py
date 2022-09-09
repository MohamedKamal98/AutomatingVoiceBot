import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone as src:
    print("say something")
    audio = r.listen(src)
#try:
    #t =  r.recognize_google(audio,language='ar-AR')
    #print(t)
