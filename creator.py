
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from random import randint
import time 
import os
import random
import polling2 as polli
from selenium.webdriver.common.proxy import Proxy, ProxyType

firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
def proxy_change():
    line = open('proxy.txt').read().splitlines()
    proxy = random.choice(line)
    print("now using " + proxy)
    firefox_capabilities['proxy'] = {
    "proxyType": "MANUAL",
    "sslProxy": proxy
    }
proxy_change()
browser = webdriver.Firefox(capabilities=firefox_capabilities)


def test(): #polls until it finds something, essential for account detection process
    if browser.find_element_by_css_selector('.SubredditPicker__subreddits').is_displayed():
        browser.quit()
        time.sleep(randint(1,2))
        print("Starting new instance")
        proxy_change()
        create_account()
    else:
        print("Waiting for captcha to be solved")

    
def create_account():
    #get reddit account creation page
    browser.set_window_size(683, 744)
    browser.get('http://reddit.com/account/register/')
    #insert username
    time.sleep(randint(1,2))
    browser.find_element_by_id('regEmail').click()
    browser.find_element_by_id('regEmail').send_keys("email@email.com")
    browser.find_element_by_css_selector('button.AnimatedForm__submitButton:nth-child(1)').click() 
    #clicks the submit button
    time.sleep(randint(1,2))
    #now the account insertion into the .txt file
    with open('created_accounts.txt','a') as file:
        file.write(browser.find_element_by_class_name('Onboarding__usernameSuggestion').text + "\n")
        file.close()

    browser.find_element_by_css_selector('a.Onboarding__usernameSuggestion:nth-child(1)').click() 
    #chooses the first random username
    #insert password
    time.sleep(randint(1,2))
    browser.find_element_by_id('regPassword').click()
    browser.find_element_by_id('regPassword').send_keys("WRITEYOURPASSWORDHERE")

    browser.find_element_by_css_selector('button.AnimatedForm__submitButton:nth-child(3)' ).click() #clicks signup to show captcha
    #pause to manually enter captcha
    print("Enter Captcha")
    #account creation detection
    polli.poll(lambda: test(),step=1, timeout=120)
    


create_account()


