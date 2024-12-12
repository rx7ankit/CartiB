from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


def blinkit_data(product_name: str, location: str):
    # Setup the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1920, 1080)

    product_data = []  # List to store product information

    try:
        # Open the Blinkit homepage
        driver.get("https://blinkit.com/")

        # Step 1: Set the location
        try:
            location_input = driver.find_element(By.NAME, "select-locality")
            location_input.click()

            # Type delivery location into the input field
            location_input.send_keys(location)
            time.sleep(1)

            # Press the space key to trigger suggestions
            location_input.send_keys(Keys.SPACE)
            time.sleep(1)  # Wait for suggestions to load

            # Select the first suggestion
            first_suggestion = driver.find_element(
                By.CSS_SELECTOR, "div.LocationSearchList__LocationLabel-sc-93rfr7-2.FUlwF"
            )
            first_suggestion.click()
            time.sleep(2)  # Wait for location to be set
        except Exception as e:
            print("Error selecting location:", e)
            driver.quit()
            return product_data  # Return empty list on failure

        # Step 2: Navigate to the product search page
        driver.get(f"https://blinkit.com/s/?q={product_name}")
        time.sleep(2)  # Allow the page to load

        # Zoom out for better visibility
        driver.execute_script("document.body.style.zoom='50%'")
        time.sleep(2)

        # Step 3: Verify you are on the correct page
        if product_name in driver.current_url:
            print("On the correct page for scraping.")

            # Locate all product divs
            product_divs = driver.find_elements(
                By.CSS_SELECTOR, 'div.Product__UpdatedPlpProductContainer-sc-11dk8zk-0')

            # Extract and store information
            for product in product_divs:
                try:
                    img_src = product.find_element(
                        By.CSS_SELECTOR, 'div.Imagestyles__ImageContainer-sc-1u3ccmn-0 img').get_attribute('src')
                except:
                    img_src = "No image found"

                try:
                    title = "(Blinkit) " + product.find_element(
                        By.CSS_SELECTOR, 'div.Product__UpdatedTitle-sc-11dk8zk-9').text
                except:
                    title = "No title found"

                try:
                    description = product.find_element(
                        By.CSS_SELECTOR, 'div.plp-product__quantity--box').text
                except:
                    try:
                        # If the first is not found, attempt to fetch the second
                        description = product.find_element(
                            By.CSS_SELECTOR, 'span.bff_variant_text_only.plp-product__quantity--box').text
                    except:
                        # If neither is found, default to a fallback message
                        description = "Description not found"

                try:
                    price = product.find_element(
                        By.CSS_SELECTOR, 'div.Product__UpdatedPriceAndAtcContainer-sc-11dk8zk-10 div[style*="font-weight: 600"]').text
                except:
                    price = "No price found"

                # Append product data to the list
                product_data.append({
                    "image": img_src,
                    "title": title,
                    "description": description,
                    "price": price
                })
                print(title)
                print(price)
                print(description)
                print("-" * 20)

        else:
            print("Not on the expected page. Exiting.")
    finally:
        # Close the browser
        driver.quit()

    return product_data