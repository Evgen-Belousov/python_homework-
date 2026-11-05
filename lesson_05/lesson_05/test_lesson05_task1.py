from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_navigation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://httpbin.qa-territory.online/")
    main_url = driver.current_url

    form_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "HTML Form")))
    form_link.click()

    wait.until(EC.url_contains("/forms/post"))
    assert "/forms/post" in driver.current_url

    driver.back()

    wait.until(EC.url_to_be(main_url))
    assert driver.current_url == main_url

    driver.quit()
