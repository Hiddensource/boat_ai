from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def gmail(u,p):




    browser = webdriver.Chrome()
    browser.get((
                'https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'))

    username = browser.find_element_by_id('identifierId')
    username.send_keys(u)

    nextButton = browser.find_element_by_id('identifierNext')
    nextButton.click()

    time.sleep(2)
    password = browser.find_element_by_name('password')
    password.send_keys(p)

    signInButton = browser.find_element_by_id('passwordNext')
    signInButton.click()
    time.sleep(12200)


def fb(u,p):
    b=webdriver.Chrome()
    b.get('https://www.facebook.com/')
    uname=b.find_element_by_id('email')
    uname.send_keys(u)
    password=b.find_element_by_id('pass')
    password.send_keys(p)
    login=b.find_element_by_id('loginbutton')
    login.click()
    time.sleep(1200)

def facebook(u,p):
    b=webdriver.Chrome()
    b.get('https://www.facebook.com/')
    uname=b.find_element_by_id('email')
    uname.send_keys(u)
    password=b.find_element_by_id('pass')
    password.send_keys(p)
    login=b.find_element_by_id('loginbutton')
    login.click()
    time.sleep(1200)


def twitter(u,p):
    b = webdriver.Chrome()
    b.get('https://twitter.com/login')
    uname = b.find_element_by_class_name('js-username-field')
    uname.send_keys(u)
    password =b.find_element_by_class_name('js-password-field')
    password.send_keys(p)
    login = b.find_element_by_css_selector('.clearfix .submit')
    login.click()
    time.sleep(1200)


def linkedin(u,p):
    b=webdriver.Chrome()
    b.get('https://in.linkedin.com/')
    uname = b.find_element_by_id('login-email')
    uname.send_keys(u)
    password = b.find_element_by_id('login-password')
    password.send_keys(p)
    login = b.find_element_by_id('login-submit')
    login.click()
    time.sleep(1200)


def youtube(u,p):
    b=webdriver.Chrome()
    b.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fnext%3D%252F%26hl%3Den%26feature%3Dsign_in_button%26app%3Ddesktop%26action_handle_signin%3Dtrue&passive=true&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    username = b.find_element_by_id('identifierId')
    username.send_keys(u)

    nextButton = b.find_element_by_id('identifierNext')
    nextButton.click()

    time.sleep(1)
    password = b.find_element_by_name('password')
    password.send_keys(p)

    signInButton = b.find_element_by_id('passwordNext')
    signInButton.click()
    time.sleep(12200)


def gdrive(u,p):
    b=webdriver.Chrome()
    b.get('https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den_US&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&urp=https%3A%2F%2Fwww.google.co.in%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    username = b.find_element_by_id('identifierId')
    username.send_keys(u)

    nextButton = b.find_element_by_id('identifierNext')
    nextButton.click()

    time.sleep(1)
    password = b.find_element_by_name('password')
    password.send_keys(p)

    signInButton = b.find_element_by_id('passwordNext')
    signInButton.click()
    time.sleep(12200)

def googledrive(u,p):
    b=webdriver.Chrome()
    b.get('https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den_US&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&urp=https%3A%2F%2Fwww.google.co.in%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    username = b.find_element_by_id('identifierId')
    username.send_keys(u)

    nextButton = b.find_element_by_id('identifierNext')
    nextButton.click()

    time.sleep(1)
    password = b.find_element_by_name('password')
    password.send_keys(p)

    signInButton = b.find_element_by_id('passwordNext')
    signInButton.click()
    time.sleep(12200)


def odrive(u,p):
    b=webdriver.Chrome()
    b.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1499879009&rver=6.7.6631.0&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fonedrive.live.com%3Fgologin%3D1%26mkt%3Den-US&lc=1033&id=250206&cbcxt=sky&mkt=en-US&lw=1&fl=easi2')

    uname=b.find_element_by_id('i0116')
    uname.send_keys(u)
    nextb=b.find_element_by_id('idSIButton9')
    nextb.click()
    time.sleep(1)
    password=b.find_element_by_id('i0118')

    password.send_keys(p)
    s=b.find_element_by_id('idSIButton9')
    s.click()
    time.sleep(1200)

def onedrive(u,p):
    b=webdriver.Chrome()
    b.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1499879009&rver=6.7.6631.0&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fonedrive.live.com%3Fgologin%3D1%26mkt%3Den-US&lc=1033&id=250206&cbcxt=sky&mkt=en-US&lw=1&fl=easi2')

    uname=b.find_element_by_id('i0116')
    uname.send_keys(u)
    nextb=b.find_element_by_id('idSIButton9')
    nextb.click()
    time.sleep(1)
    password=b.find_element_by_id('i0118')

    password.send_keys(p)
    s=b.find_element_by_id('idSIButton9')
    s.click()
    time.sleep(1200)