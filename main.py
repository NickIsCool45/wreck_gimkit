from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import uniform
from xpaths import *

driver = webdriver.Chrome()
def join(code,name):
    driver.get("https://www.gimkit.com/join")
    driver.find_element(by=By.NAME, value="Game Code").send_keys(code)
    driver.find_element(by=By.NAME, value="Join").click()
    sleep(3)
    driver.find_element(by=By.NAME, value="Your Name").send_keys(code)
    driver.find_element(by=By.NAME, value="Join").click()
    print("Joined game.")

join(input("Enter Game Code: "),input("Enter Name: "))