from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time 
import os

loginFile = 'created_accounts.txt'

#update with comment link or post link to upvote



def upvote_post():
    postLink = input("Insert Post link")
    profile = webdriver.FirefoxProfile()
    browser = webdriver.Firefox(firefox_profile=profile)

    #insert username
    browser.get("https://www.reddit.com/login/")
    browser.find_element_by_id('loginUsername').click()
    browser.find_element_by_id('loginUsername').send_keys("username")
    #insert password
    browser.find_element_by_id('loginPassword').click()
    browser.find_element_by_id('loginPassword').send_keys("WRITEYOURPASSWORDHERE")
    #login
    time.sleep(2)
    browser.find_element_by_css_selector('button.AnimatedForm__submitButton:nth-child(1)').click()
    time.sleep(3)
    #get link page
    browser.get(postLink)
    time.sleep(3)
    browser.find_element_by_css_selector('#upvote-button-t3_tviilo').click()

man = input("Post or comment?")
if man == "post":
    upvote_post()

elif man == "comment":
    input("Insert comment perma link")
    commentPermaLink = input


    

#def upvote_comment(browser, username, password, commentLink):
    #insert username
    #browser.find_element_by_name('user').click()
   # browser.find_element_by_name('user').send_keys(username)
    #insert password
   # browser.find_element_by_name('passwd').click()
    #browser.find_element_by_name('passwd').send_keys(password)
    ##login
   # browser.find_element_by_css_selector('.btn').click()
    #time.sleep(2)
    #get link page
    #browser.get(commentLink)
    #browser.find_element_by_css_selector('div.midcol:nth-child(2) > div:nth-child(1)').click()
    #logout
   # browser.find_element_by_css_selector('.logout > a:nth-child(4)').click()
   # time.sleep(2)
   # browser.get('http://www.reddit.com')

#def main():
   # browser = webdriver.Firefox()
    #browser.get('http://reddit.com')

    #comment out post or comment depending on what you'd like to upvote
    # creds = [cred.strip() for cred in open(loginFile).readlines()]
    # for cred in creds:
       # username, password = cred.split(':')
        # upvote_comment(browser, username,password,commentPermaLink)
        # upvote_post(browser, username, password, postLink)
#main()


