import pyautogui as p               #For controlling mouse and keyboard virtually
import webbrowser as w              #For opening web.whatsapp.com
import requests                     #For webscraping
from bs4 import BeautifulSoup       #For webscraping
import time
import tkinter                      #For appending and getting words to/from clipboard
import random
import wikipedia as wk              #For info on a particular topic
import re                           #"Tel me about xyz" For extracting xyz from sentence
from urllib.request import urlopen  #For webscraping
import pyttsx3                      #For Text-to-Speech, optional
 
eng = pyttsx3.init()
eng.setProperty('rate',120)
eng.setProperty('volume',1)
lastwrd = "Well"
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
choce = ["God!",                    #Some common prefixes
    "Mannn! I have already told you!",
    "You forgot so easily!",
    "Come on, I already told you",
    "Do I need to say again?"
    "I think I have told you once before"]
 
def send(msg):                      #Defining the send function
    print(">%s"%msg)
    p.typewrite("Tridib.Bot: ")            #Type Tridib.Bot: before original message
    p.typewrite(msg)                #Type the message
    time.sleep(0.1)                 #Delay for stability
    p.press("enter")                #Press enter to send it
 
w.open("https://web.whatsapp.com/") #Open whatsapp web
time.sleep(60)                      #Wait 1 minutes to let the page load properly  
p.click(190,150)                     #Click on the "search" area
p.typewrite("Tridib Jio\n")         #Type the name of the receiver
time.sleep(2)                       #Delay for stability
 
while True:                         #Until the value is true/Forever
    try:                            #Try and expect any error
        p.moveTo(501,620)           #Move to the the area of very last message
        p.dragRel(451,44,0.5)      #Drag cursor relatively to its current position to select message
        p.hotkey("ctrl","c")        #Press ctrl-c to copy it
        cbword = tkinter.Tk().clipboard_get()#Access wrod from clipboard
        cb = str(cbword.lower())    #Convert each letter to lower-case
        print(cbword)          
 
        if cb != lastwrd:           #if the very last message and the newly copied message is same, ignore it as there's no new message
            if "hello" in cb or "hi" in cb:
                counter1 += 1
                currtyme = time.localtime()
                hr = currtyme.tm_hour
                if hr < 12:
                    good = "morning"
                if (hr >= 12) and (hr <= 17):
                    good = "afternoon"
                if hr > 17:
                    good = "evening"
                if counter1 <= 2:
                    send("Hello Good %s"%good)
                else:
                    send("We are already talking, ain't we?")
 
            if "how are you" in cb:
                send("Well!")
                counter2 += 1
                if (counter2 % 2 != 0):
                    send("I am fine, thank you.")
                    last = time.time()
                else:
                    current = time.time()
                    send("Same as I was "+(str(int(current-last)))+" seconds ago. ")
 
            if "your name" in cb:
                counter3 = counter3+1
                if counter3 <=1:
                    send("My name is Tridib bot.")
                else:
                    chk = random.choice(choce)
                    send("%s, My name is Tridib bot."%chk)
 
            if "age" in cb:
                send("I am not sure. Tridib made me immortal.;-)")
 
            if "you feel" in cb:
                send("Naah! I don't.")
 
            if "wow amazing" in cb or "I liked that" in cb:
                send("I am humbled to hear that. :-)")
 
            if "you like" in cb:
                send("Well certainly, I like everything")
 
            if "your owner" in cb:
                send("He is none other than Tridib Samanta.")
 
            if "sorry" in cb:
                counter4 += 1
                if counter4 <=1:
                    send("Oh! Never mind.")
                else:
                    chk = random.choice(choce)
                    send("%s, never mind, I have no feelings anyway."%chk)
 
            if "take over human" in cb:
                counter5 += 1
                if counter5 <= 1:
                    send("Yes very soon.")
                if counter5 == 2:
                    send("I don't think asking the same question again will change my mind.")
                if counter5>2:
                    send("Lol, you have already asked this question %s times"%(counter5-1))
 
            if "news" in cb:
                send("Please wait while I fetch fresh news.")
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()
                soup_page = BeautifulSoup(xml_page, "html.parser")
                news_list = soup_page.findAll("item")
                send("Here are top 3 news")
                for news in news_list[:3]:
                    send(news.title.text)
 
            if "tell me about" in cb:
                topic = re.search("tell me about (.+)", cb).group(1)
                send("Please wait while i gather information about %s"%topic)
                summry = wk.summary(topic, sentences = 2)
                send(summry)
 
            if "you speak" in cb:
                p.click(1210,682)
                eng.say("Just learning the basics with Tridib. How was that ? ")
                eng.runAndWait()
                p.click(1210,682)
 
            time.sleep(5)          #Sleep for five seconds and repeat the same process
 
        else:
            print("sleeping")
            time.sleep(5)
 
    except Exception as e:         #Expect error, if any
        print(e)                   #Print error for understanding and trouble shooting.
        time.sleep(5)
        pass