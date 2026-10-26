from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestMultipleElements:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def test_from_submission(self):
        self.driver.get("https://httpbin.qa-territory.online/links/10")
        elements = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a"))
        )
        assert len(elements) == 9
        for element in elements:
            assert element.is_displayed()
        assert "1" in elements[0].text

    def teardown_method(self):
        self.driver.quit()
