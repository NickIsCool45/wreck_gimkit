from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from xpaths import *
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chromedriver_location = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chromedriver_location, options=chrome_options)
wait = WebDriverWait(driver, 10)

def click(xpath):
    element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def type(keys, xpath):
    element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
    element.send_keys(keys)

def join(code,name):
    driver.get("https://www.gimkit.com/join")
    driver.implicitly_wait(3)

    type(code,game_code_input)
    click(join_game_button_1)

    sleep(3)

    type(name,name_input)
    click(join_game_button_2)
    print("Joined game.")

gamecode = input("Enter Game Code: ")
gamename = input("Enter Name: ")
join(gamecode,gamename)