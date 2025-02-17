import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    """
    Фикстура для инициализации браузера Chrome перед каждым тестом,
    и закрытия после выполнения теста.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук pytest: делает скриншот при фейле или успехе.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":  # Выполняется во время самого теста (не setup/teardown)
        driver = item.funcargs.get("browser")  # Получает браузер из фикстуры
        if driver:
            screenshot_path = f"allure-results/{item.name}.png"
            driver.save_screenshot(screenshot_path)  # Сохраняет скриншот

            # Добавляет скриншот в Allure-отчёт
            if report.failed:
                allure.attach.file(screenshot_path, name="Ошибка", attachment_type=allure.attachment_type.PNG)
            else:
                allure.attach.file(screenshot_path, name="Успех", attachment_type=allure.attachment_type.PNG)