import random
import string
import urllib

import urllib3
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

# z1
# strona pozwala na web scrapping

# z2
baseurl = "https://www.pap.pl/"
xpaths = {
    'cookies': "//div[@class='ok closeButton']",
    'en': "//a[@href='http://www.pap.pl/en']",
    'business': "//a[@href='/en/business']",
    'list': "//ul[@class='newsList']",
    'lastPage': "//a[@title='Go to last page']",
    'element': 'news col-sm-6',

}
myDriver = webdriver.Chrome()
myDriver.get(baseurl)
# a
myDriver.find_element(by=By.XPATH, value=xpaths['cookies']).click()
# b
myDriver.maximize_window()
# c
myDriver.find_element(by=By.XPATH, value=xpaths['en']).click()
# d
myDriver.find_element(by=By.XPATH, value=xpaths['business']).click()
# e
titles = myDriver.find_elements(by=By.CSS_SELECTOR, value='div.newsList div div.textWrapper h1 a, '
                                                          'div.newsList div div.row ul li div.textWrapper h2 a')

imagePaths = myDriver.find_elements(by=By.CSS_SELECTOR, value='div.newsList div div.imageWrapper a img, '
                                                              'div.newsList div div.row ul li div.imageWrapper a img')
# f
for path in imagePaths:
    name = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(15))
    urlretrieve(path.get_attribute("src"), f"{name}.jpg")

# g
myDriver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# h

lastPage = myDriver.find_element(by=By.XPATH, value=xpaths['lastPage'])
lastPage.click()
# selenium.common.exceptions.ElementClickInterceptedException:
# Message: element click intercepted: Element <a href="?page=72"
# title="Go to last page" rel="last">...</a> is not clickable at point (602, 28).
# Other element would receive the click: <div class="navbar-collapse collapse" id="navbar">...</div>
#   (Session info: chrome=100.0.4896.127)
print(lastPage.get_attribute("href").split("=")[1])
