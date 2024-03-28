from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np


def write_to_file(filename, data, mode='w'):
    try:
        with open(filename, mode, encoding='utf-8') as file:
            if isinstance(data, str):
                file.write(data)
            else:
                file.writelines(data)
        print(f"Data written to '{filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def click_and_print_title(driver, span_element):
    span_element.click()
    try:
        wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for relevant content
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tith3")))
    except Exception:
        pass
    try:
        title_element = driver.find_element(By.CLASS_NAME, "tith3")
        title = title_element.text
        print(title)
    except Exception:
        pass  # Handle cases where the title structure might differ

    # Navigate back to the original page
    driver.back()


def click_spans(driver, target_element_id):
    """Clicks on all span elements within the target element identified by ID.

    Args:
        driver: The Selenium WebDriver instance.
        target_element_id: The ID of the element containing the spans to click.
    """

    # Find the target element
    target_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, target_element_id))
    )

    # Find all span elements within the target element
    span_elements = target_element.find_elements(By.TAG_NAME, "span")

    for i in range(min(2, len(span_elements))):
        try:
            span_element = span_elements[i]
            span_element.click()
            print(f"Clicked span: {span_element.text}")  # Print the text of the clicked span (optional)
        except Exception as e:
            print(f"Error clicking span: {e}")


def main():
    # Replace with the actual URL of your webpage
    url = "https://140online.com/products.aspx?key="

    # Initialize Chrome webdriver
    driver = webdriver.Chrome()

    # Load the webpage
    driver.get(url)

    file_name = "انشطة وخدمات.txt"
    names = np.array([])

    spans = driver.find_elements(By.CSS_SELECTOR, "span.tablecatgre2")[0]

    text = spans.text
    text = text.replace('\n\n', '\n')
    write_to_file(file_name, text)
    driver.quit()


if __name__ == "__main__":
    main()

# from datetime import datetime, timedelta
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
# import pywhatkit
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# url = "https://140online.com/products.aspx?key="
#
# driver.get(url)
#
#

#
#
#
# driver.quit()
