import re

from selenium.webdriver.common.by import By
from pages.base_test_util import BaseTestUtil
from pages.urls_constants import URLConstants

class SbisDownloadPage(BaseTestUtil):
    BASE_URL = URLConstants.SABY_DOWNLOAD_URL

    FOOTER_DOWNLOAD_LOCAL_LINK = (By.CSS_SELECTOR, "li.pb-16:nth-child(9) > a:nth-child(1)")
    PLUGIN_DOWNLOAD_LINK_TEXT = (By.CSS_SELECTOR, ".sbis_ru-DownloadNew-block .sbis_ru-DownloadNew-flex__child.sbis_ru-DownloadNew-flex__child--width-1")
    PLUGIN_DOWNLOAD_LINK = (By.CSS_SELECTOR, ".sbis_ru-DownloadNew-block a[href*='.exe']")

    def open_download_page(self):
        self.open(self.BASE_URL)

    def get_plugin_download_href(self):
        link_el = self.find_element(self.PLUGIN_DOWNLOAD_LINK)
        return link_el.get_attribute("href")
    
    def click_footer_link(self):
        block = self.find_element(self.FOOTER_DOWNLOAD_LOCAL_LINK, timeout=5)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", block)
        block.click()


    def get_expected_plugin_size_mb(self):
        """
        Считывает размер, указанный на сайте (например, 'Скачать (Exe 10.42 МБ)'),
        и возвращает float(10.42).
        """
        size_el = self.find_element(self.PLUGIN_DOWNLOAD_LINK_TEXT)
        text = size_el.text
        print("Extracted text:", text)  # Для отладки

        # Ищет число, за которым следует "МБ"
        match = re.search(r'(\d+(?:\.\d+))\s*МБ', text)
        if match:
            # Берет группу с самим числом, например "10.42"
            size_str = match.group(1)
            # Заменяет запятую на точку (вдруг где-то встретиться) и приводит к float
            return float(size_str.replace(",", "."))
        else:
            raise ValueError(f"Не удалось найти число перед 'МБ' в строке: {text}")