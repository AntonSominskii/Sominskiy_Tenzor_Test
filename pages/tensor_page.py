import time

from selenium.webdriver.common.by import By
from conftest import browser
from pages.base_test_util import BaseTestUtil
from pages.urls_constants import URLConstants

class TensorPage(BaseTestUtil):
    BASE_URL = URLConstants.TENSOR_URL

    SILA_V_LUDIACH_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content > p:nth-child(1)")
    MORE_DETAILS_LINK = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content > p:nth-child(4) > a:nth-child(1)")
    RABOTAEM_IMAGES = (By.CSS_SELECTOR, "div.s-Grid-container:nth-child(2)")
    RABOTAEM_BLOCK =(By.CSS_SELECTOR, "div.tensor_ru-container:nth-child(4)")

    def open_tensor_home(self):
        self.open(self.BASE_URL)

    def is_sila_v_ludiach_visible(self):
        block = self.find_element(self.SILA_V_LUDIACH_BLOCK, timeout=5)
        if block:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", block)
            block_text = block.text
            return "Сила в людях" in block_text
        return False

    def scroll_down_by(self, px=300):
        self.driver.execute_script(f"window.scrollBy(0, {px});")

    def go_to_more_details(self):
        self.find_element(self.MORE_DETAILS_LINK).click()

    def get_images_dimensions_in_rabotaem_section(self):
        """
        Возвращает список (width, height) для всех картинок в секции "Работаем",
        используя фактические размеры элемента (Selenium .size).
        """
        block = self.find_element(self.RABOTAEM_BLOCK, timeout=5)
        if block:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", block)
            block_text = block.text
            if "Работаем" not in block_text:
                raise Exception("Блок 'Работаем' найден, но в его тексте отсутствует слово 'Работаем'")
        else:
            raise Exception("Блок 'Работаем' не найден на странице")
    
        # Находит все <img> внутри блока
        images = self.find_elements(self.RABOTAEM_IMAGES)
        dimensions = []
        for img in images:
            size = img.size  # возвращает словарь, например {"width": 273, "height": 200}
            w = size["width"]
            h = size["height"]
            dimensions.append((w, h))
        return dimensions