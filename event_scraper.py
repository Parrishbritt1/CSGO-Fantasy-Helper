from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import objects


driver = webdriver.Chrome(executable_path="C:/Users/Parri/CSGO-Fantasy-Helper/chromedriver.exe")
driver.get("https://www.hltv.org/fantasy/243/overview")
sleep(3)

# Uncheck Cookies
driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonPreferences").click()
driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonStatistics").click()
driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonMarketing").click()

# Accept Selection of Cookies
driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection").click()
sleep(3)

# Name of event
event_title_element = driver.find_element_by_xpath('//*[@id="fantasy"]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/h1/a')
print(event_title_element.text)
event_title_url = event_title_element.get_attribute("href")

event_num = ""
for char in event_title_url[event_title_url.index("events")+7:]:
    if char == "/":
        break
    event_num += char

print(event_num)

# results page
driver.get(f"https://www.hltv.org/results?event={event_num}")
sleep(1)

# Match buttons on event page
match_elements = driver.find_elements_by_class_name("result-con")
for match_ele in match_elements:
    match_ele.click()
    sleep(3)
    print(match_ele.find_elements_by_class_name("align-logo"))
    break
