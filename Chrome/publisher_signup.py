
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

CURRENT_TIME = time.strftime('%m%d%H%M')
EMAIL_ADDRESS = "mikhail+pub{0}@mylikes.com".format(str(CURRENT_TIME))
LOGIN_NAME = "pub{0}".format(str(CURRENT_TIME))
LOGIN_PASSWORD = "password123"
FB_URL = "https://www.facebook.com/Mynewmagazine-1040802922639882"
PAGE_TITLE = "{0} test page".format(str(CURRENT_TIME))


def signup():

    #launch Chrome webdriver

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 3)

    #navigate to mylikes.com and select 'Sign Up'

    driver.get("http://www.mylikes.com")

    assert "MyLikes" in driver.title

    driver.find_element_by_xpath('.//*[@id="publisher_overlay"]/div/a').click()

    #publisher sign-up form page 1

    driver.switch_to.frame('likes_iframe_signup')

    driver.find_element_by_name("email").send_keys(EMAIL_ADDRESS)
    driver.find_element_by_name("name").send_keys(LOGIN_NAME)
    driver.find_element_by_name("password").send_keys(LOGIN_PASSWORD)

    driver.find_element_by_id('submit_signup_form').click()

    #publisher sign-up form page 2

    driver.switch_to.default_content()
    driver.switch_to.frame('likes_iframe_signup')

    driver.implicitly_wait(3)

    driver.find_element_by_name('ad_urls').send_keys(FB_URL)
    driver.find_element_by_name('site_title').send_keys(PAGE_TITLE)
    driver.find_element_by_id('submit_domain_form').click()

    #publisher sign-up form page 3

    driver.switch_to.default_content()
    driver.switch_to.frame('likes_iframe_signup')

    templates = wait.until(EC.el((By.CLASS_NAME, 'format_option')))
    random.choice(templates).click()


    color_schemes = driver.find_elements_by_class_name('palette_option')
    random.choice(color_schemes).click()

    driver.find_element_by_id('finish_button').click()

    #publisher main page

    alert = wait.until(EC.presence_of_element_located((By.ID, 'partner_login_form')))
    audience = wait.until(EC.presence_of_element_located((By.ID, 'gender_audience_wrapper')))

    wait.until(EC.element_located_to_be_selected((By.TAG_NAME, 'label'))).click()

    alert.find_element_by_id('save_partner_login_form').click()

    #driver.quit()



