import config
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless =True
driver = webdriver.Chrome('E:\Ratanabh\COLLEGE1\Projects\Jarvis python\Spotify Automation\chromedriver.exe')


url = 'https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F'
#load link

def login(Email, Password):
    driver.get(url)
    driver.maximize_window()

    # WITH XPATH

    driver.find_element(By.XPATH, '//*[@id="login-username"]').send_keys(Email)
    driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys(Password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]/div[1]/p').click()

    sleep(2)  # we wait for page to load /-OR else we see !ERROR(only some times)


login(config.username, config.password)