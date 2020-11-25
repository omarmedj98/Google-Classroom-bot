from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import speech_recognition as sr
import pickle
import os.path
from get_api import start_name,start_time,start_url,end_time
import smtplib



keyboard = Controller()
#firfox profile to get around google auth
fp = webdriver.FirefoxProfile("C:\\Users\\ELITEBOOK G6\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\wh04balb.default-release")
#define your profile you want use and the driver with firefox we use geckdriver and for chrome we use chromedriver
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", firefox_profile=fp)
driver.maximize_window()

def press_and_release(key):
    keyboard.press(key)
    keyboard.release(key)

def open_discu():
        elem = driver.switch_to.active_element
        classe_name = elem.get_attribute("class")
        if "uArJ5e UQuaGc kCyAyd" in classe_name:
            press_and_release(Key.enter)

def say_hello():
    send_email()
    time.sleep(2)
    open_discu()
    time.sleep(2)
    keyboard.type('Im here sir')
    time.sleep(2)
    press_and_release(Key.enter)
    time.sleep(1)
    press_and_release(Key.esc)
def send_email():
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    server.login("your email",
                 'mdp of your email')

    server.sendmail('from',
                    'to',
                    "message")

    server.quit()
def open_meet():
    #you put meeting url
    driver.get(start_url)
    #driver.get("https://meet.google.com/********")

   # print("shit he we go again you have ", start_name)
    time.sleep(10)
    press_and_release(Key.tab)
    time.sleep(2)
    # DISABLE CAMERA AND MIC AND ENTER ROOM
    with keyboard.pressed(Key.ctrl):
        press_and_release('d')

        press_and_release('e')

    time.sleep(2)
    for i in range(0,5):
        press_and_release(Key.tab)
    elem = driver.switch_to.active_element
    class_name = elem.get_attribute("class")
    if "uArJ5e UQuaGc Y5sE8d" in class_name:
        time.sleep(2)
        press_and_release(Key.enter)
def detect_name():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)


        try:
            text = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + text)
            if (text == "hello"):
                time.sleep(1)
                say_hello()

            now = datetime.now()
            date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
            if (date_time == end_time[0:19]):
                break
            time.sleep(2)

        except:
            print("problem")
        #text need to equal your name so put instead of hello your name


         
    close_meet()

def close_meet():
    press_and_release(Key.tab)
    press_and_release(Key.tab)
    press_and_release(Key.tab)
    press_and_release(Key.tab)
    press_and_release(Key.enter)
    print('byby')

def check_time():
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
    if(date_time==start_time[0:19]):
      print("its time to work lol")
      open_meet()
      time.sleep(4)
      press_and_release(Key.tab)
      press_and_release(Key.tab)
      detect_name()

while True: check_time()
