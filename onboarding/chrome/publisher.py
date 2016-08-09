from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from campaign_urls import campaign_urls
import random
import time

CURRENT_TIME = time.strftime('%m%d%H%M')
EMAIL_ADDRESS = "mikhail+pub{0}@mylikes.com".format(str(CURRENT_TIME))
LOGIN_NAME = "pub{0}".format(str(CURRENT_TIME))
LOGIN_PASSWORD = "password123"
FB_URL = "https://www.facebook.com/Super-Funny-Page-1648625298792756/"
CAMPAIGN_URL = random.choice(campaign_urls)
PAGE_TITLE = "{0} test page".format(str(CURRENT_TIME))

def signup():

    # launch Chrome webdriver

    global driver, wait

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 5)

    driver.get("http://www.mylikes.com")

    assert "MyLikes" in driver.title

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "signup_btn"))).click()

    assert "Sign up for MyLikes" in driver.title

    driver.switch_to.frame('likes_iframe_signup')

    form = driver.find_element_by_id('signup_form')

    form.find_element_by_name("email").send_keys(EMAIL_ADDRESS)
    form.find_element_by_name("name").send_keys(LOGIN_NAME)
    form.find_element_by_name("password").send_keys(LOGIN_PASSWORD)

    form.find_element_by_id('submit_signup_form').click()

    #layout selection

    '''
    print(driver.get_attribute('value'))

    layouts = driver.find_element_by_class_name('layout_selection')

    print(len(layouts))

    assert len(layouts) == 8

    random.choice(layouts).click()

    '''

    driver.find_element_by_class_name('next_button').click()


signup()