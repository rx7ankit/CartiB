from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)

# Open the webpage

driver.get("https://blinkit.com/s/?q=Apple")
# Wait for page to load
time.sleep(5)

# Scroll the page 3 times
for _ in range(3):
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    time.sleep(2)  # Allow content to load after each scroll

# Locate all product divs
product_divs = driver.find_elements(
    By.CSS_SELECTOR, 'div.Product__UpdatedPlpProductContainer-sc-11dk8zk-0')

# Extract and print information
for product in product_divs:
    try:
        # Image Source
        img_src = product.find_element(
            By.CSS_SELECTOR, 'div.Imagestyles__ImageContainer-sc-1u3ccmn-0 img').get_attribute('src')
    except:
        img_src = "No image found"

    try:
        # Title
        title = product.find_element(
            By.CSS_SELECTOR, 'div.Product__UpdatedTitle-sc-11dk8zk-9').text
    except:
        title = "No title found"

    try:
        # Description/Weight
        description = product.find_element(
            By.CSS_SELECTOR, 'div.plp-product__quantity--box').text
    except:
        description = "No description found"

    try:
        # Price
        price = product.find_element(
            By.CSS_SELECTOR, 'div.Product__UpdatedPriceAndAtcContainer-sc-11dk8zk-10 div[style*="font-weight: 600"]').text
    except:
        price = "No price found"

    try:
        # Delivery Time
        delivery_time = product.find_element(
            By.CSS_SELECTOR, 'div.Product__UpdatedETAContainer-sc-11dk8zk-6 div[style*="text-transform: uppercase"]').text
    except:
        delivery_time = "No delivery time found"

    try:
        # Add Button Text
        add_button_text = product.find_element(
            By.CSS_SELECTOR, 'div.AddToCart__UpdatedButtonContainer-sc-17ig0e3-0').text
    except:
        add_button_text = "No Add button found"

    # Print the extracted information
    print(f"Image Source: {img_src}")
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Price: {price}")
    print("-" * 50)

# Close the browser
driver.quit()
