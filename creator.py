
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from random import randint
import time 
import os



userNamePasswordFile = 'redditNameList.txt'
createdUserNamePasswordFile = 'createdNames.txt'


def create_account():
    #set up profile for proxy
    profile = webdriver.FirefoxProfile()
    browser = webdriver.Firefox(firefox_profile=profile)

    #get reddit account creation page
    browser.set_window_size(683, 744)
    browser.get('http://reddit.com/account/register/')
    #insert username
    time.sleep(randint(1,2))
    browser.find_element_by_id('regEmail').click()
    browser.find_element_by_id('regEmail').send_keys("email@email.com")
    browser.find_element_by_css_selector('button.AnimatedForm__submitButton:nth-child(1)').click() 
    #clicks the submit button
    time.sleep(randint(1,5))

    random_name = browser.find_element_by_class_name('Onboarding__usernameSuggestion').text
    #now the account insertion
    with open("created_accounts.txt", "r+") as crack:
        crack.write(" " + random_name)

    browser.find_element_by_css_selector('a.Onboarding__usernameSuggestion:nth-child(1)').click() 
    #chooses the first random username
    #insert password
    time.sleep(randint(1,5))
    browser.find_element_by_id('regPassword').click()
    browser.find_element_by_id('regPassword').send_keys("WRITEYOURPASSWORDHERE")

    browser.find_element_by_css_selector('button.AnimatedForm__submitButton:nth-child(3)').click() #clicks signup to show captcha
    #pause to manually enter captcha
    input("[*] Solve captcha, create account, then press enter... enter 'r' as input if captcha doesn't appear to skip username" + '\n')
    if (input == 'r'):
        os.system('clear')
        browser.quit()
        return False
    else:
        browser.quit()
        return True



create_account()



#deleted main() func because uhhhhhhh