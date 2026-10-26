from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestFormSubmission:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def test_form_submission(self):
        self.driver.get("https://httpbin.qa-territory.online/forms/post")
        element_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="custname"]'))
        )
        element_input.send_keys("Evgenie")
        old_url = self.driver.current_url
        element_button = self.driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        )
        element_button.click()
        print("URL после клика:", self.driver.current_url)
        self.wait.until(EC.url_changes(old_url))
        url_new = self.driver.current_url
        assert url_new != old_url, f"URL не изменился! Ожидали не {old_url}"

    def teardown_method(self):
        self.driver.quit()
