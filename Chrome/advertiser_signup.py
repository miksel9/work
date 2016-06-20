from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from CreditCards import creditcards
import random
import time


CURRENT_TIME = time.strftime('%m%d%H%M')
EMAIL_ADDRESS = "mikhail+ad{0}+stripe_test@mylikes.com".format(str(CURRENT_TIME))
LOGIN_NAME = "ad{0}".format(str(CURRENT_TIME))
LOGIN_PASSWORD = "password123"
FB_URL = "https://www.facebook.com/Mynewmagazine-1040802922639882"
CAMPAIGN_URL = "www.toyota.com"
PAGE_TITLE = "{0} test page".format(str(CURRENT_TIME))
CC_NMBR = random.choice(list(creditcards.values()))
CC_EXP_M = "04"
CC_EXP_YR = "2020"
CC_CVC = "123"

def signup():

    # launch Chrome webdriver

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 3)

    #navigate to mylikes.com and select 'Sign Up'

    driver.get("http://www.mylikes.com")

    assert "MyLikes" in driver.title

    driver.find_element_by_id('home_header_advertisers_link').click()

    driver.find_element_by_xpath('.//*[@id="advertiser_overlay"]/div[1]/a').click()

    #advertiser sign-up form page 1

    driver.find_element_by_name("email").send_keys(EMAIL_ADDRESS)
    driver.find_element_by_name("name").send_keys(LOGIN_NAME)
    driver.find_element_by_name("nickname").send_keys(LOGIN_NAME)
    driver.find_element_by_name("password").send_keys(LOGIN_PASSWORD)

    driver.find_element_by_xpath(".//*[@id='signup_publisher_form']/div[2]/input").click()

    #advertiser sign-up form page 2

    driver.find_element_by_name('ad_url').send_keys(CAMPAIGN_URL)

    driver.find_element_by_xpath(".//*[@id='main_loggedin_content_box']/div/div/div[2]/div/div/div[4]/input").click()

    #advertiser sign-up form page 3

    wait.until(EC.element_to_be_clickable((By.XPATH,
                                ".//*[@id='main_loggedin_content_box']/div/div/div[2]/div/div/div[8]/input"))).click()

    #advertiser sign-up form page 4

    wait.until(EC.element_to_be_clickable((By.XPATH,
                                ".//*[@id='main_loggedin_content_box']/div/div/div[2]/div/div/div[5]/input"))).click()

    #advertiser sign-up form page 5

    cc_form = wait.until(EC.element_to_be_clickable((By.ID, 'payment-form')))

    cc_form.find_element_by_id('card_number').send_keys(CC_NMBR)
    cc_form.find_element_by_id('expmonth').send_keys(CC_EXP_M)
    cc_form.find_element_by_id('expyear').send_keys(CC_EXP_YR)
    cc_form.find_element_by_id('card_code').send_keys(CC_CVC)

    wait.until(EC.element_to_be_clickable((By.ID, "stripe_cc_form_button"))).click()

    #advertiser sign-up form page 6; confirmation

    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), "Your campaign is pending review"))

    driver.quit()