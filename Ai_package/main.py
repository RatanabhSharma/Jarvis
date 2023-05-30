from cmath import e
import datetime
import sys
import webbrowser
sys.path.append('.')
import os
import subprocess
from time import sleep
import pyautogui
from pyjokes import pyjokes
from sympy.physics.units import wb
from wikipedia import wikipedia
import cv2
# import controller as cnt


from Ai_package.Features.Play_songs import play_songs
from Ai_package.Features.base import date, open_chrome, speak, takeCommand, time, speak, wishme


if __name__ == "__main__":

    wishme()

    while True:
        
        query = takeCommand().lower()
        
        print(query)

        if "stop" in query:
            speak("Stopping")
            break

        if "time" in query:
            time()

        if "date" in query:
            date()
        
        # if "light on" in query:
        #      speak("light on")
        #      cnt.led(1)
        # elif "light off" in query:
        #      speak("light off")
        #      cnt.led(0)
        # elif "exit" in query:
        #     break
        # Open chrome/Website
        if "open chrome" in query:
            open_chrome()
        
        elif "who are you" in query:
            speak('My name is JARVIS and I am you Vitrual buddy')
    
        elif "who made you" in query:
            speak('I was created by Ratanabh Sharma')
        
        elif "why were you made" in query:
            speak('i was created to be good virtual friend of my master')
        
        elif 'jarvis stands for' in query:
            speak('JARVIS stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
        
        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'sleep' in query:
            sys.exit()
        

        # Wikipedia search
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                page = wikipedia.page(query)
                speak(f"Opening Wikipedia page for {query}")
                webbrowser.open_new_tab(page.url)
            except wikipedia.exceptions.DisambiguationError as e:
                options = e.options[:5]
                speak(f"Which one do you mean? {options}")
                ans = takeCommand().lower()
                for option in options:
                    if ans in option.lower():
                        try:
                            page = wikipedia.page(option)
                            speak(f"Opening Wikipedia page for {option}")
                            webbrowser.open_new_tab(page.url)
                            break
                        except wikipedia.exceptions.PageError:
                            speak(f"Sorry, I could not find any Wikipedia page for {option}")
                            break
                        except wikipedia.exceptions.PageError:
                            speak(f"Sorry, I could not find any Wikipedia page for {query}")



        # Chrome search
        elif "open" in query:
            speak("What should I open?")
            search = takeCommand().lower()
            if "youtube" in search:
                url = "https://www.youtube.com/"
                speak("Opening YouTube")
            elif "google" in search:
                url = "https://www.google.com/"
                speak("Opening Google")
            else:
                url = "https://www.google.com/search?q=" + search.replace(" ", "+")
                speak("Searching for " + search + " on Google")
            try:
                chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" # location
                browser = webbrowser.get(chromepath)
                browser.open_new_tab(url)
            except Exception as e:
                print(e)
                speak("Sorry, I was not able to open the website.")



        # Launch applications
        elif "notepad" in query:
            speak("opening notepad")
            location = "C:/WINDOWS/system32/notepad.exe"
            notepad = subprocess.Popen(location)

        
        # Random jokes
        elif "joke" in query:
            speak(pyjokes.get_jokes())

        # Logout / Shutdown / Restart
        elif "logout" in query:
            speak('logging out in 5 second')
            sleep(5)
            os.system("shutdown - l")

        elif "shutdown" in query:
            speak('shutting down in 5 second')
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak('initiating restart in 5 second')
            sleep(5)
            os.system("shutdown /r /t 1")

            # <-------------------------Pyautogui  Features--------------------->

        elif "hidden menu" in query:
            # Win+X: Open the hidden menu
            pyautogui.hotkey('winleft', 'x')

        elif "task manager" in query:
            # Ctrl+Shift+Esc: Open the Task Manager
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif "task view" in query:
            # Win+Tab: Open the Task view
            pyautogui.hotkey('winleft', 'tab')

        elif "take screenshot" in query:
            # win+prtscr
            pyautogui.hotkey('winleft', 'prtscr')
            speak("done")

            # Take screenshot save in Given location

            """elif "take screenshot" in query:
            img = pyautogui.screenshot()
            img.save("D:/screenshot_1.png")  # file mane and location
            speak("Done")"""


        elif "snip" in query:
            pyautogui.hotkey('winleft', 'shift', 's')

        elif "close this app" in query:
            # alt + f4: close this app
            pyautogui.hotkey('alt', 'f4')

        elif "setting" in query:
            # win+i = open setting
            pyautogui.hotkey('winleft', 'i')

        elif "new virtual desktop" in query:
            # Win+Ctrl+D: Add a new virtual desktop
            pyautogui.hotkey('winleft', 'ctrl', 'd')
        
        elif "play songs" in query:
            play_songs()
        
        # Recording a Video with Integrated Camera or a Default Camera
        elif 'record a video' in query:
            # Capture the video frame by frame and choosing the camera while changing digits in -> ()
            # cap = cv2.VideoCapture(1)
            cap = cv2.VideoCapture(0)

            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

            # detection -> detection of any face or any body
            detection = False
            
            detection_stopped_time = None
            timer_started = False

            SECONDS_TO_RECORD_AFTER_DETECTION = 3

            frame_size = (int(cap.get(3)), int(cap.get(4)))
            # fourcc -> 4 Character Code with defining the file format
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")

            while True:
                _, frame = cap.read()

                # faces & bodies will detect the face or a body if caught will the camera is in turned on mode.
                # gray -> It is used to make any color preference of your choice while detecting any face or a body
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

                # The condition gets true if any type of face or a body will be caught in front of camera
                if len(faces) + len(bodies) > 0:
                    # If nothing detects in front of camera then recording will not start ->
                    if detection:
                        timer_started = False
                    
                    # If something gets detected in front of camera like a face or a body it will start recording the video ->
                    else:
                        detection = True

                        # current_time = current format of date and time -> ("%d-%m-%Y-%H-%M-%S")
                        # out - it is a variable where current time stamp is used with file format to store a file in the current folder where the source code file is stored.
                        current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                        out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
                        
                        print("Started Recording!")
                        speak("Started Recording!")
                
                # If any interuption will be caused will recording the video ->
                elif detection:
                    # If nothing is getting detected by the camera then ->
                    if timer_started:
                        if time.time() -detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                            detection = False
                            timer_started = False
                            out.release()
                            print('Stopped Recording!')
                            speak('Stopped Recording!')
                    
                    # If any face or object get caught in between the SECONDS_TO_RECORD_AFTER_DETECTION then it will continue to record the video -> 
                    else:
                        timer_started = True
                        detection_stopped_time = time.time()

                # If a face or body again get caught in the camera then it will start recording ->
                if detection:
                    out.write(frame)

                for (x, y, width, height) in faces:
                    cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

                cv2.imshow("Video", frame)

                # the 'q' button is set as the quitting button you may use any desired button of your choice
                if cv2.waitKey(1) == ord('q'):
                    break

            # After the loop release the cap object
            out.release()
            cap.release()

            # Destroy all the windows
            cv2.destroyAllWindows()



        elif 'take a photo' in query:
            # Capture the photo frame by frame and choosing the camera while changing digits in -> ()
            # pic = cv2.VideoCapture(0)
            pic = cv2.VideoCapture(0)

            # # To set the resolution
            # pic.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            # pic.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

            # .read() function reads/gets the data from the camera in the resulting frame
            ret, frame = pic.read()
            if ret:
                # while(True):
                    
            
                # Display the resulting frame
                cv2.imshow('Photo', frame)

                # .imwrite() function saves the picture in the current directory folder
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                cv2.imwrite(f"{current_time}.png", frame)
                
                # the 'q' button is set as the quitting button you may use any desired button of your choice
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
                # After the loop release the cap object
                pic.release()
                
                # Destroy all the windows
                cv2.destroyAllWindows()

                print("Done sir.")
                speak("Done sir.")

            else :
                print("Could not open camera device for a picture")
                speak("Could not open camera device for a picture")
