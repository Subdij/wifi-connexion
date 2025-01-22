from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
from selenium.common.exceptions import ElementNotInteractableException

# Load environment variables from .env file
load_dotenv()

def connect_to_wifi():
    # Get the URL, username, and password from environment variables
    url = os.getenv('WIFI_URL')
    username = os.getenv('WIFI_USERNAME')
    password = os.getenv('WIFI_PASSWORD')

    # Initialize the WebDriver with options to ignore SSL errors
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    try:
        # Retry logic to handle no initial internet connection
        max_retries = 5
        for attempt in range(max_retries):
            try:
                # Navigate to the URL
                driver.get(url)
                break
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(5)
        else:
            print("Failed to load the URL after several attempts")
            return

        # Function to continuously check the URL
        def check_url():
            while True:
                if "userinfo.html" in driver.current_url:
                    print("userinfo.html URL accessed, closing the browser")
                    driver.quit()
                    return
                time.sleep(1)

        # Start checking the URL in a separate thread
        import threading
        url_check_thread = threading.Thread(target=check_url)
        url_check_thread.start()

        # Wait for the username field to be present
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "n_uid")))
        except Exception as e:
            print("Error: Username field not found")
            raise e

        # Enter the username
        try:
            username_field = driver.find_element(By.ID, "n_uid")
            username_field.send_keys(username)
        except ElementNotInteractableException as e:
            print("Error: Username field not interactable")
            raise e

        # Wait for the password field to be present
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pswd")))
        except Exception as e:
            print("Error: Password field not found")
            raise e

        # Enter the password
        password_field = driver.find_element(By.ID, "pswd")
        password_field.send_keys(password)

        # Wait for the submit button to be present
        try:
            submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.btnred[type="submit"][value="OK"]')))
        except Exception as e:
            print("Error: Submit button not found")
            raise e

        # Click the submit button
        submit_button.click()

        # Wait for the conditions checkbox if it appears
        try:
            conditions_checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="checkbox"][name="read"][value="accepted"]')))
            conditions_checkbox.click()
            submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.btnred#accept_btn[name="action"][value="J\'accepte"]')))
            submit_button.click()
        except Exception as e:
            print("Error: Conditions checkbox or submit button not found")
            raise e

    finally:
        if driver.service.process:
            driver.quit()

if __name__ == "__main__":
    connect_to_wifi()
