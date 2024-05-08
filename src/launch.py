from selenium import webdriver
import time

def fill_form():
    # Set the path to your ChromeDriver executable
    # Replace "./chromedriver" with the actual path to your ChromeDriver executable
    driver = webdriver.Chrome("./chromedriver")

    # Open the website
    url = "https://example.com"  # Replace "https://example.com" with the desired website URL
    driver.get(url)

    # Wait for the page to load (You may need to adjust the sleep time based on the website loading time)
    time.sleep(3)

    # Find the fields by their names or other selectors and fill in the values
    input_field1 = driver.find_element_by_name("field1")  # Replace "field1" with the actual name or selector of the input field
    input_field1.send_keys("Value 1")  # Replace "Value 1" with the desired value for the input field

    input_field2 = driver.find_element_by_name("field2")  # Replace "field2" with the actual name or selector of the input field
    input_field2.send_keys("Value 2")  # Replace "Value 2" with the desired value for the input field

    # Perform any other actions as needed, such as clicking buttons, etc.
    # button = driver.find_element_by_id("button_id")
    # button.click()

    # Wait for a while to see the filled form (You can remove this sleep if you don't need it)
    time.sleep(5)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    fill_form()
