from cmath import e
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

        # Open chrome/Website
        if "open chrome" in query:
            open_chrome()

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
                                browser.open_new_tab(page.url)
                                break
                            except wikipedia.exceptions.PageError:
                                speak(f"Sorry, I could not find any Wikipedia page for {query}")
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

                chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" # location
                browser = webbrowser.get(chromepath)
                browser.open_new_tab(url)
        

        # Launch applications
        elif "open notepad" in query:  # if open notepad in statement
            speak("opening notepad")  # speak
            location = "C:/WINDOWS/system32/notepad.exe"  # location
            notepad = subprocess.Popen(location)  # location of a software you want tot open

        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()  # terminate


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