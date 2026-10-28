from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_form_submission():
    driver = webdriver.Chrome()
    
    driver.get("https://httpbin.qa-territory.online/forms/post")
    
   
    wait = WebDriverWait(driver, 10)
    element_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="custname"]'))
    )
    
   
    element_input.send_keys("Evgen")
    
    
    old_url = driver.current_url
    
    
    element_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    element_button.click()

    wait.until(EC.url_changes(old_url))
    
    assert driver.current_url != old_url
    
    driver.quit()
