import speech_recognition as sr
import webbrowser
import pyttsx3
print()
print("This program will open Linux command executer and can Launch the Docker Container for you")
print()
pyttsx3.speak("Hello I am Ron")
pyttsx3.speak("I am here to help you")
pyttsx3.speak("Please tell me the requirement") 
r=sr.Recognizer()
with sr.Microphone() as source:
  print("Listening....")
  audio=r.listen(source)
  print("Done")
p=r.recognize_google(audio)
print(p)

if (("run" in p) or ("launch" in p)) and (("docker" in p) or ("container" in p)):
  webbrowser.open("http://192.168.43.101/drun.html")
  pyttsx3.speak("working to launch Docker")
elif (("open" in p) and ("Linux" in p) or ("executer" in p)):
  webbrowser.open("http://192.168.43.101/webapp.html")
  pyttsx3.speak("opening Linux command executer")
else:
  print("Sorry, this is out of my reach")