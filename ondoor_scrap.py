from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

service = Service('C:/webdriver/chromedriver-win32/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://www.ondoor.com/category/fruits-vegetables/fruits')

while True:
    time.sleep(3)
    html_text = driver.page_source
    soup = BeautifulSoup(html_text, 'html.parser')
    all_items = soup.find_all('li')

    for item in all_items:
        fruits_img = item.find('div', class_='prod-thumb')
        fruits = item.find('div', class_='prod-name')
        cost = item.find('div', class_='prod-ratebox')
        img = fruits_img.find('img')['src'] if fruits_img and fruits_img.find('img') else 'None'
        fruit_name = fruits.find('a').text.strip() if fruits and fruits.find('a') else 'None'
        cost_value = cost.find('span').text.strip() if cost and cost.find('span') else 'None'

        if fruit_name != 'None' and cost_value != 'None':
            print(f'''
            Image: {img}
            Fruit Name: {fruit_name}
            Cost: {cost_value}''')
            print('')
    try:
        next_button = driver.find_element(By.LINK_TEXT, 'Next')
        next_button.click()
    except:
        print("No more pages to load.")
        break
driver.quit()