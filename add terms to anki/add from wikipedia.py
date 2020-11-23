from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import pyperclip
import translators as ts

pyautogui.getActiveWindow().minimize()
time.sleep(0.5)

terms = []

pyautogui.click("add terms to anki/clicks/add.png")

options = Options()
# options.headless = True
driver = webdriver.Chrome(
    "add terms to anki\chromedriver.exe", options=options)
driver.get(wikipedia)


for term in terms:
    inputBox = driver.find_element_by_name("search")
    inputBox.send_keys(term)
    driver.find_element_by_name("go").click()
    paragraph_element = driver.find_elements_by_xpath(
        "/html/body/div[3]/div[3]/div[5]/div[1]/p")
    content = []
    text = ""

    for paragraph in paragraph_element:
        content.append(paragraph.text)
        text = "\n\n".join(content)

    pyautogui.hotkey("alt", "tab")
    pyperclip.copy(term)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("tab")
    pyperclip.copy(ts.bing(term, to_language="en"))
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("enter")
    pyperclip.copy(ts.bing(term, to_language="ja"))
    pyautogui.hotkey("ctrl", "v")
    pyperclip.copy("\n" + text)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("ctrl", "enter")
    pyautogui.hotkey("alt", "tab")

driver.quit()
pyautogui.hotkey("alt", "tab")
pyautogui.click("add terms to anki\clicks\close.png")
