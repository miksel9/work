from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from CreditCards import creditcards
from campaign_urls import campaign_urls
import random
import time


CURRENT_TIME = time.strftime('%m%d%H%M')
EMAIL_ADDRESS = "mikhail+ad{0}+stripe_test@mylikes.com".format(str(CURRENT_TIME))
LOGIN_NAME = "ad{0}".format(str(CURRENT_TIME))
LOGIN_PASSWORD = "password123"
FB_URL = "https://www.facebook.com/Super-Funny-Page-1648625298792756/"
CAMPAIGN_URL = random.choice(campaign_urls)
PAGE_TITLE = "{0} test page".format(str(CURRENT_TIME))
CC_NMBR = random.choice(list(creditcards.values()))
CC_EXP_M = "04"
CC_EXP_YR = "2020"
CC_CVC = "123"
CC_NAME = "Mister Tester"
CC_ADDRESS = "123 Main St"
CC_CITY = "SF"
CC_STATE = "CA"
CC_ZIP = "94321"

def signup():

    # launch Chrome webdriver

    global driver, wait

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 5)

    driver.get("http://www.mylikes.com")

    assert "MyLikes" in driver.title

    driver.find_element_by_id('home_header_advertisers_link').click()

    #wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'signup_btn')))

    driver.find_element_by_xpath('//*[@id="advertiser_overlay"]/div[1]/a').click()

    #advertiser sign-up form page 1

    driver.find_element_by_id("email").send_keys(EMAIL_ADDRESS)
    driver.find_element_by_id("name").send_keys(LOGIN_NAME)
    driver.find_element_by_id("nickname").send_keys(LOGIN_NAME)
    driver.find_element_by_id("password").send_keys(LOGIN_PASSWORD)

    driver.find_element_by_xpath(".//*[@id='signup_publisher_form']/div[2]/input").click()

    #advertiser sign-up form page 2

    wait.until(EC.visibility_of_element_located((By.ID, 'ad_url'))).send_keys(CAMPAIGN_URL)

    driver.find_element_by_class_name('button').click()

    #advertiser sign-up form page 3

    wait.until(EC.element_to_be_clickable((By.XPATH,
                                           '//*[@id="main_loggedin_content_box"]/div/div/div[2]/div/div/div[8]/input'))).click()

    #advertiser sign-up form page 4

    wait.until(EC.element_to_be_clickable((By.XPATH,
                                           '//*[@id="main_loggedin_content_box"]/div/div/div[2]/div/div/div[5]/input'))).click()

    #advertiser sign-up form page 5

    cc_form = wait.until(EC.visibility_of_element_located((By.ID, "ccform")))

    cc_form.find_element_by_id('card_number').send_keys(CC_NMBR)
    cc_form.find_element_by_id('expmonth').send_keys(CC_EXP_M)
    cc_form.find_element_by_id('expyear').send_keys(CC_EXP_YR)
    cc_form.find_element_by_id('card_code').send_keys(CC_CVC)
    cc_form.find_element_by_id('full_name').send_keys(CC_NAME)
    cc_form.find_element_by_id('address').send_keys(CC_ADDRESS)
    cc_form.find_element_by_id('city').send_keys(CC_CITY)
    cc_form.find_element_by_id('state').send_keys(CC_STATE)
    cc_form.find_element_by_id('zip').send_keys(CC_ZIP)

    wait.until(EC.element_to_be_clickable((By.ID, "cc_form_button"))).click()

    #advertiser sign-up form page 6; confirmation

    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), "Your campaign is pending review"))

    driver.find_element_by_class_name('nav_link').click()

    #docusign

    time.sleep(3)

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "agreement_button"))).click()

    assert "DocuSign" in driver.title

    wait.until(EC.visibility_of_element_located((By.ID, "disclosureAccepted"))).click()

    wait.until(EC.element_to_be_clickable((By.ID, "action-bar-btn-continue"))).click()

    driver.find_element_by_class_name("tab-button").click()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="adopt-dialog"]/div/div[3]/button[1]'))).click()

    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "action-bar-helpful-message"), "Done! Select Finish to send the completed document."))

    time.sleep(3)

    wait.until(EC.element_to_be_clickable((By.ID, "action-bar-btn-finish"))).click()

    time.sleep(3)

    #delete account

    deleteAdvertiser()

    driver.quit()

def deleteAdvertiser():

    menu = driver.find_element_by_class_name("account_link")
    settings = driver.find_element_by_xpath('//*[@id="loggedin_header"]/div/div/div/div/div/div[2]/a[1]')

    ActionChains(driver).move_to_element(menu).click(settings).perform()

    wait.until(EC.element_to_be_clickable((By.ID, "cancel_account_button"))).click()

    alert = driver.switch_to.alert()
    alert.accept()
