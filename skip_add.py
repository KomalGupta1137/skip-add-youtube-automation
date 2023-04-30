#importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys

#selecting firefox as the browser
driver = webdriver.Firefox()

#url of website
url = "https://www.youtube.com/watch?v=bBhoLugUbIE"

#opening link in browser
driver.get(url)

#finding classname of skip button
skip_button = driver.find_element_by_xpath('//*[@id="ad-text:6"]').click()
skip_button.send_keys('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[27]/div[2]/div[1]/button')