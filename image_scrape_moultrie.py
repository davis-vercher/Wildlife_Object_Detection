from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
import time
import requests

# Setup driver
driver = webdriver.Chrome()
driver.get("https://app.moultriemobile.com/login")
input("Please log in manually, then press Enter to continue...")

# Define and create save directory
save_dir = r"D:\Delta_County\Moultrie\All_Images"
os.makedirs(save_dir, exist_ok=True)

image_counter = 0
page_counter = 1

while page_counter <= 88:
    print(f"\nProcessing page {page_counter}...")
    time.sleep(5)

    images = driver.find_elements(By.CSS_SELECTOR, "img.full-width")
    print(f"Found {len(images)} images on page {page_counter}.")

    for img in images:
        src = img.get_attribute("src")
        if src:
            url = src.split('?')[0]
            try:
                response = requests.get(url, timeout=10)
                ext = url.split('.')[-1]
                filename = os.path.join(save_dir, f"image_{image_counter}.{ext}")
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {filename}")
                image_counter += 1
            except Exception as e:
                print(f"Error downloading {url}: {e}")

    # Try clicking the new "Next Page" button
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "a[title='Go to Next Page']")
        next_button.click()
        page_counter += 1
    except NoSuchElementException:
        print("Next page button not found. Stopping.")
        break
    except ElementClickInterceptedException:
        print("Next button click blocked. Retrying...")
        time.sleep(2)
        continue


driver.quit()