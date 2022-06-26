import time

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# z2
baseurl = "https://www.otomoto.pl/osobowe"
xpaths = {
    'offers': "//article[@class='ooa-rld5ij e1b25f6f18']",
    'cookies': "//button[@id='onetrust-accept-btn-handler']",
    'lastPage': "//a[@href='/osobowe']",
    'offer': "//li[@class='offer-params__item']",
}
vehicles = pd.DataFrame(
    columns=['seller type', 'make', 'model', 'year', 'mileage', 'fuel', 'horse power', 'transmission', 'drive train',
             'body type', 'seats', 'doors', 'color', 'country', 'accident free', 'seller name', 'location'])
myDriver = webdriver.Chrome()
myDriver.maximize_window()
myDriver.get(baseurl)
myDriver.find_element(by=By.XPATH, value=xpaths['cookies']).click()
# lastPageNumber = myDriver\
#     .find_element(by=By.XPATH, value=xpaths['lastPage'])\
#     .find_element(by=By.CSS_SELECTOR, value='span').get_property("value")
offers = myDriver.find_elements(by=By.CSS_SELECTOR, value="article")
delay = 3
print("1")
offers[1].click()
print("1.1")
myDriver.back()
print("2")
for offer in offers:
    tmp = offer
    try:
        print("1")
        tmp.click()
        print("2")
        myElem = WebDriverWait(myDriver, delay).until(EC.presence_of_element_located(tmp))
        print("3")
    except TimeoutException:
        print("Loading took too much time!")

    print("2")
    break
    # try:
    #     WebDriverWait(myDriver, delay).until(EC.presence_of_element_located(offer.click()))
    # except TimeoutException:
    #     print
    #     "Loading took too much time!"
    # print("1")
    # # offer.click()
    # print("2")

    # # print(offer.find_element(by=By.XPATH, value=xpaths['offer']).find_element(by=By.CSS_SELECTOR, value="div a")
    # #        .get_attribute("value"))
    # myDriver.back()

