from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseTestUtil:
    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.base_url = base_url if base_url else ""

    def open(self, url=""):
        """
        Открыть URL (если передан относительный url — дополняет base_url).
        """
        if url.startswith("http"):
            full_url = url
        else:
            full_url = self.base_url + url
        self.driver.get(full_url)

    def wait_visible(self, locator, timeout=10):
        """
        Ожидание видимости элемента по локатору (By, locator_str).
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def find_element(self, locator, timeout=10):
        """
        Вернуть веб-элемент, дождавшись видимости.
        """
        return self.wait_visible(locator, timeout)

    def find_elements(self, locator, timeout=10):
        """
        Вернуть список веб-элементов, дождавшись видимости первого из списка.
        """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)