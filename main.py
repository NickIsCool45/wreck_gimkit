from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from xpaths import *
from time import sleep
from random import uniform
from loggedQuestion import loggedQuestion

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chromedriver_location = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chromedriver_location, options=chrome_options)
wait = WebDriverWait(driver, 10)

correct_answers = []
money = 0
streak_level = 1
next_streak_level_money = 20

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

def get_question():
  return(driver.find_element_by_xpath(question_text).text)

def get_answers():
  answers = []
  for i in range(4):
    answers.append(driver.find_element_by_xpath(answer_choice % (i+1)).text)
  return(answers)

def get_response():
  response = driver.find_element_by_xpath(response_text).text[0]
  if response == "+":
    return(True)
  elif response == "-":
    click(view_correct_answer)
    return(driver.find_element_by_xpath(correct_answer_text).text)

def get_money():
  money_string = driver.find_element_by_xpath(money_text).text
  return(int(money_string.replace("-", "").replace("$", "").replace(",", "")))  # don't remove negative sign

def add_question_answer(question, answer):
  correct_answers.append(loggedQuestion(question, answer))

def delay():
  sleep_time = uniform(0.2, 0.9)
  print(f"Sleeping for {str(round(sleep_time,3))}s")
  sleep(sleep_time)
  print("Resuming")

gamecode = input("Enter Game Code: ")
gamename = input("Enter Name: ")
join(gamecode,gamename)