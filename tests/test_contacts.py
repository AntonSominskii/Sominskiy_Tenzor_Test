import pytest
import allure

from pages.sbis_main_page import SbisMainPage
from pages.tensor_page import TensorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Контакты / Первый сценарий")
def test_tensor_banner_and_images(browser):
    """
    1) Перейти на https://sbis.ru/ в раздел "Контакты"
    2) Найти баннер Тензор, кликнуть
    3) Открывается новая вкладка https://tensor.ru/
    4) Проверить, что есть блок "Сила в людях"
    5) Перейти в "Подробнее" -> https://tensor.ru/about
    6) Найти раздел "Работаем" и проверить, что у всех фотографий одинаковые (height) и (width)
    """

    # 1) Открывает главную страницу sbis.ru, переходит в "Контакты"
    sbis_page = SbisMainPage(browser)
    sbis_page.open_main_page()
    sbis_page.go_to_contacts()
    sbis_page.go_to_more_contacts()

    # Сохраняет список вкладок ДО клика
    old_handles = browser.window_handles

    # 2) Кликает на баннер "Тензор"
    sbis_page.click_tensor_banner()

    # Находит новую вкладку/окно и переключается
    new_handles = browser.window_handles
    for handle in new_handles:
        if handle not in old_handles:
            browser.switch_to.window(handle)
            break

    # Теперь тест в контексте вкладки, где открыт https://tensor.ru/
    # Создаёт объект TensorPage
    tensor_page = TensorPage(browser)

    # 4) Проверяет, что блок "Сила в людях" присутствует
    assert tensor_page.is_sila_v_ludiach_visible(), "Блок 'Сила в людях' не найден"

    # 5) Кликает в "Подробнее" → должен перейти на https://tensor.ru/about
    tensor_page.go_to_more_details()

    current_url = browser.current_url
    assert "tensor.ru/about" in current_url, f"Не перешли на /about. Текущий URL: {current_url}"

    # 6) Проверяет картинки в блоке "Работаем"
    dimensions = tensor_page.get_images_dimensions_in_rabotaem_section()
    assert len(dimensions) > 0, "Не найдено ни одной картинки в секции 'Работаем'"

    first_width, first_height = dimensions[0]
    for (w, h) in dimensions:
        assert w == first_width and h == first_height, (
            f"Размер картинки ({w}x{h}) отличается от первой ({first_width}x{first_height})"
        )


@allure.feature("Контакты / Второй сценарий")
def test_region_partners(browser):
    """
    1) Перейти на https://sbis.ru/ в раздел "Контакты"
    2) Проверить, что определился ваш регион (ожидается "Воронежская обл./область") и есть список партнеров
    3) Изменить регион на 'Камчатский край'
    4) Проверить, что подставился выбранный регион, список партнеров изменился,
       а url и title содержат информацию выбранного региона
    """

    # 1) Открывает главную страницу sbis.ru, переходит в "Контакты"
    sbis_page = SbisMainPage(browser)
    sbis_page.open_main_page()
    sbis_page.go_to_contacts()
    sbis_page.go_to_more_contacts()

    # 2) Проверяет текущий регион
    old_region = sbis_page.get_region_title().strip()  # Убирает лишние пробелы
    old_partners_text = sbis_page.get_partners_container_text()

    # Разрешает оба возможных варианта записи региона
    expected_regions = ["Воронежская обл.", "Воронежская область"]
    assert old_region in expected_regions, f"Ожидаемый регион 'Воронежская область', но определился: {old_region}"

    assert old_partners_text, "Список партнёров (контейнер) пуст!"

    # 3) Меняет регион
    sbis_page.change_region("Камчатский край")
    new_region = sbis_page.get_region_title()
    new_partners_text = sbis_page.get_partners_container_text()

    # 4) Проверяет, что регион сменился
    assert new_region == "Камчатский край", f"Регион не сменился, сейчас: {new_region}"

    # Проверяет, что текст контейнера партнёров изменился
    assert new_partners_text != old_partners_text, "Список партнёров не изменился!"

    current_url = sbis_page.get_current_url()
    page_title = sbis_page.get_title()
    assert "kamchatskij-kraj" in current_url or "Камчатский край" in current_url, \
        f"URL не содержит информации о Камчатском крае: {current_url}"
    assert "Камчатский край" in page_title, \
        f"Title не содержит 'Камчатский край': {page_title}"