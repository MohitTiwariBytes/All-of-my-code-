from openai import OpenAI
import pyttsx3
import random as r
import os 
import webbrowser

client = OpenAI(
    api_key= "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"
)

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)



def speak(audio):
      engine.say(audio)
      engine.runAndWait()

prompt = input("Hi, I am Genie! How can i help you today? : ")


exit_resp = ["Good Bye!", "Sayonara!", "See you soon !", "See ya!", "Have Great day!"]



loop = True
if prompt.lower() == "exit":
        print(r.choice(exit_resp))

        loop = False

while loop:

        


    if "vscode" in prompt.lower():
          os.startfile("C:\\Users\\Mohit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
          print("I just opened VScode for you, Sir!")
          speak("I just opened VScode for you, Sir!")
          
          prompt = input("Prompt : ")
          if prompt.lower() == "exit":
                print(r.choice(exit_resp))
                loop = False

    if "mohit" in prompt.lower():
          print("Mohit Tiwari, Who created me is a sixth class student and is currently studying in Shri Krishna Inter Collage, His father name is Sir Mantosh Tiwari. ")            
          speak("Mohit Tiwari, Who created me is a sixth class student and is currently studying in Shri Krishna Inter Collage, His father name is Sir Mantosh Tiwari. ")            
          
          prompt = input("Prompt : ")
          if prompt.lower() == "exit":
                print(r.choice(exit_resp))
                loop = False

    if "mantosh" in prompt.lower():
          print("Sir Mantosh Tiwari is father of Mohit Tiwari, and he is currently working with Kazo International Pvt Ltd. He is currently 40")
          speak("Sir Mantosh Tiwari is father of Mohit Tiwari, and he is currently working with Kazo International Private limited. He is currently 40")
          prompt = input("Prompt : ")
          if prompt.lower() == "exit":
                print(r.choice(exit_resp))
                loop = False

    if "patanjali" in prompt.lower(): 
          print("Mam Patanjali Tiwari is Mother of Mohit Tiwari, and he is a House Wife. He is currently 35")
          speak("Mam Patanjali Tiwari is Mother of Mohit Tiwari, and he is a House Wife. He is currently 35")
          prompt = input("Prompt : ")
          if prompt.lower() == "exit":
                print(r.choice(exit_resp))
                loop = False

    if "mandeep" in prompt.lower(): 
          print("Mandeep Tiwari is Brother of Mohit Tiwari, and he finds joy in Video Editing and he is learning how to edit videos. He is currently 14")
          speak("Mandeep Tiwari is Brother of Mohit Tiwari, and he finds joy in Video Editing and he is learning how to edit videos. He is currently 14")
          prompt = input("Prompt : ")
          if prompt.lower() == "exit":
                print(r.choice(exit_resp))
                loop = False

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant named Genie and you are created by Mohit Tiwari in 2024"},
            {"role": "user", "content": prompt}
        ]
        )

    speak(completion.choices[0].message.content)
    print(completion.choices[0].message.content)
    prompt = input("Prompt : ")   
    if prompt.lower() == "exit":
        print(r.choice(exit_resp))
        loop = False   

    