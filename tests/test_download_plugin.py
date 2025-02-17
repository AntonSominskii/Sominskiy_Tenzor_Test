import os
import requests
import allure
from pages.sbis_download_page import SbisDownloadPage
from pages.sbis_main_page import SbisMainPage

@allure.feature("Скачивание плагина (третий сценарий)")
def test_download_sbis_plugin(browser):
    """
    1) Перейти на https://sbis.ru/
    2) В Footer найти "Скачать локальные версии"
    3) Скачать СБИС Плагин для Windows (web-установщик) в папку G:\SominskiyTenzorTest\tests
    4) Убедиться, что файл скачался
    5) Сравнить размер файла с указанным (например, 3.64 МБ)
    """
    # 1) Открывает главную страницу sbis.ru
    sbis_page = SbisMainPage(browser)
    sbis_page.open_main_page()

    # 2) Переходит на страницу скачивания (нажимает "Скачать локальные версии")
    download_page = SbisDownloadPage(browser)
    download_page.click_footer_link()
    
    # 3) Получает ссылку на плагин и ожидаемый размер
    plugin_href = download_page.get_plugin_download_href()
    expected_size_mb = download_page.get_expected_plugin_size_mb()

    # 4) Скачивает файл через requests
    response = requests.get(plugin_href, stream=True)
    filename = plugin_href.split("/")[-1] or "sbis_plugin.exe"
    
    # Определяет путь к папке с текущим тестом
    download_dir = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.join(download_dir, filename)
    print("Файл будет сохранён в:", download_path)

    with open(download_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    # 5) Проверяет, что файл скачался и его размер соответствует ожидаемому
    file_size_bytes = os.path.getsize(download_path)
    file_size_mb = file_size_bytes / (1024 * 1024)
    file_size_mb_rounded = round(file_size_mb, 2)
    expected_size_mb_rounded = round(expected_size_mb, 2)

    assert os.path.exists(download_path), "Файл не скачался!"
    assert file_size_mb_rounded == expected_size_mb_rounded, (
        f"Размер скачанного файла {file_size_mb_rounded} МБ != ожидаемому {expected_size_mb_rounded} МБ"
    )