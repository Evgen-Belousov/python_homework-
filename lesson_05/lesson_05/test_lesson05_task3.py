from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_links():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://httpbin.qa-territory.online/links/10")

    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a")))

    assert len(elements) == 9

    for element in elements:
        assert element.is_displayed()

    assert "1" in elements[0].text

    driver.quit()
