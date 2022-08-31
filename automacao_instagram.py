#Im creating an instagram bot with Python and Selenium w/ the folowing actions:

#Log In
#Follow an user
#Unfollow an user


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


class bot():
    def __init__(Self, browser, username, passwrd):
        Self.browser = webdriver.Chrome(executable_path=r'C:\Users\mayco\chromedriver_win32\chromedriver.exe')
        Self.username = username
        Self.passwrd = passwrd


    def login(Self):
        Self.browser.get('https://www.instagram.com/')
        usernameInput = Self.browser.find_element(By.XPATH, "//input[contains(@name , 'username')]" )
        password = Self.browser.find_element(By.XPATH, "//input[contains(@name , 'senha')]")

        usernameInput.send_keys(Self.username)
        password.send_keys(Self.passwrd)
        password.send_keys(Keys.ENTER)
    

    def followUsr(Self, username):
        Self.browser.get('https://www.instagram.com/' + username + '/')
        follow = Self.browser.find_element(By.XPATH)
        follow.click()

    
        






