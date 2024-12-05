from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)

# Open the webpage
driver.get("https://www.swiggy.com/instamart/search?custom_back=true&query=chips")
time.sleep(3)  # Allow the page to load completely

# Zoom out to 25%
driver.execute_script("document.body.style.zoom='25%'")
time.sleep(2)  # Allow time for the zoom effect

# Scroll until all products are loaded
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    time.sleep(2)  # Allow content to load after scrolling
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # Stop if no new content is loaded
        break
    last_height = new_height

# Locate product containers
product_containers = driver.find_elements(
    By.CSS_SELECTOR, "div[data-testid='default_container_ux4']")

# Extract information from each product container
for product in product_containers:
    try:
        discount = product.find_element(
            By.CSS_SELECTOR, "div[data-testid='item-offer-label-discount-text']").text
    except:
        discount = "No discount found"

    try:
        img_src = product.find_element(
            By.CSS_SELECTOR, "img[class='sc-dcJsrY ibghhT _1NxA5']").get_attribute("src")
    except:
        img_src = "No image found"

    try:
        title = product.find_element(By.CSS_SELECTOR, "div.novMV").text
    except:
        title = "No title found"

    try:
        description = product.find_element(
            By.CSS_SELECTOR, "div.sc-aXZVg.hwhxsS._1sPB0").text
    except:
        description = "No description found"

    try:
        weight = product.find_element(By.CSS_SELECTOR, "div[aria-label]").text
    except:
        weight = "No weight info found"

    try:
        price = product.find_element(
            By.CSS_SELECTOR, "div[data-testid='itemOfferPrice']").text
    except:
        price = "No price found"

    try:
        delivery_time = product.find_element(
            By.CSS_SELECTOR, "div.sc-aXZVg.giKYGQ.GOJ8s").text
    except:
        delivery_time = "No delivery time found"

    # Print extracted information
    print(f"Discount: {discount}")
    print(f"Image: {img_src}")
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Weight: {weight}")
    print(f"Price: {price}")
    print(f"Delivery Time: {delivery_time}")
    print("-" * 50)

# Close the browser
driver.quit()
