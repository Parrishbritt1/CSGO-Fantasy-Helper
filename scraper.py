from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.hltv.org/fantasy/243/overview")
sleep(3)

# Uncheck Cookies
driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonPreferences").click()
driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonStatistics").click()
driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonMarketing").click()

# Accept Selection of Cookies
driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection").click()
sleep(1)

# Click onto HLTV x BitSkins League
driver.find_element_by_xpath('//*[@id="fantasy"]/div/div[2]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[1]').click()
sleep(1)

# Get number of team pages.
pages_ele = driver.find_element_by_class_name("standing-leaderboard-count")
num_pages = int(pages_ele.text[pages_ele.text.index("of")+3:])

# List of 10 elements of each team on page
team_elements = driver.find_elements_by_class_name("tr-wrapper")

# Need to get child elements of all "tr-wrapper" elements because "tr-wrapper" elements are unclickable.
clickable_team_elements = []
for team_ele in team_elements:
    clickable_team_elements.append(team_ele.find_element_by_xpath(".//*"))
# print("CLICKABLE ELEMENTS =", clickable_team_elements)

# Click on first team
clickable_team_elements[0].click()
sleep(1)

# TODO: Change this to get name of each player on team
print(driver.find_element_by_class_name("text-ellipsis").text)

# driver.close()