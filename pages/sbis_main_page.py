import time
from selenium.webdriver.common.by import By
from pages.base_test_util import BaseTestUtil
from pages.urls_constants import URLConstants

class SbisMainPage(BaseTestUtil):
    BASE_URL = URLConstants.SBIS_URL

    CONTACTS_LINK = (By.CSS_SELECTOR, "div.sbisru-Header__menu-link")
    MORE_CONTACTS_MODAL_LINK = (By.CSS_SELECTOR, "a.sbisru-link:nth-child(5) > span:nth-child(1)")
    TENSOR_BANNER = (By.CSS_SELECTOR, ".sbisru-Contacts__border-left--border-xm > a:nth-child(1) > img:nth-child(1)")
    REGION_TITLE = (By.CSS_SELECTOR, "span.ml-16 > span:nth-child(1)")
    REGION_CHANGE_LINK = (By.CSS_SELECTOR, "span.ml-16 > span:nth-child(1)")
    REGION_SEARCH_INPUT = (By.CSS_SELECTOR, "div.controls-Render:nth-child(2) > div:nth-child(1) > div:nth-child(3) > input:nth-child(1)")
    REGION_ITEM = (By.CSS_SELECTOR, ".sbis_ru-Region-Panel__item > span:nth-child(1) > span:nth-child(1)")
    PARTNERS_LIST_CONTAINER = (By.CSS_SELECTOR, ".sbisru-Contacts-List__col")

    def open_main_page(self):
        self.open(self.BASE_URL)

    def go_to_contacts(self):
        self.find_element(self.CONTACTS_LINK).click()

    def go_to_more_contacts(self):
        self.find_element(self.MORE_CONTACTS_MODAL_LINK).click()

    def click_tensor_banner(self):
        self.find_element(self.TENSOR_BANNER).click()

    def get_region_title(self):
        return self.find_element(self.REGION_TITLE).text.strip()

    def get_partners_container_text(self):
        container = self.find_element(self.PARTNERS_LIST_CONTAINER, timeout=10)
        return container.text

    def is_partners_list_visible(self):
        try:
            container = self.find_element(self.PARTNERS_LIST_CONTAINER, timeout=5)
            return container.is_displayed()
        except:
            return False

    def change_region(self, region_name="Камчатский край"):
        self.find_element(self.REGION_CHANGE_LINK).click()
        input_el = self.find_element(self.REGION_SEARCH_INPUT)
        input_el.clear()
        input_el.send_keys(region_name)
        time.sleep(1)
        self.find_element(self.REGION_ITEM).click()
        time.sleep(1)

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title