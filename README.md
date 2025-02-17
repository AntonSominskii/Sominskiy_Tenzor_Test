# SominiskiyTenzorTest

Данный проект содержит автоматизированные тесты на **Python** для проверки функционала сайта [sbis.ru](https://sbis.ru/) (раздел «Контакты») и [tensor.ru](https://tensor.ru/), а также сценарий скачивания плагина **СБИС**.  
Тесты написаны с использованием **Selenium** (WebDriver 4), **pytest** и реализованы по паттерну **PageObject**.  

В рамках задания реализовано два **обязательных** сценария и один **дополнительный** (необязательный).

---

## Структура проекта

SominiskiyTenzorTest/
├── pages/
│   ├── base_test_util.py        # Базовые методы для работы с WebDriver (поиск элементов, ожидания и т.д.)
│   ├── sbis_main_page.py        # Страница sbis.ru (главная, контакты)
│   ├── sbis_download_page.py    # Страница загрузки локальных версий
│   ├── tensor_page.py           # Страница tensor.ru
│   └── urls_constants.py        # Класс для хранения URL-адресов (SBIS_URL, TENSOR_URL и т.д.)
├── tests/
│   ├── test_contacts.py         # Первый и второй сценарии (контакты, проверка региона, баннер Тензор)
│   ├── test_download_plugin.py  # Дополнительный сценарий (скачивание плагина)
├── conftest.py                  # Фикстура для инициализации браузера, Allure-хуки
├── pytest.ini                   # Дополнительные настройки Pytest (опционально)
├── requirements.txt             # Список зависимостей (pytest, selenium, allure-pytest и т.д.)
└── README.md                    # Документация (вы читаете его)


---

## Описание тестовых сценариев

### Первый сценарий

1. Перейти на [sbis.ru](https://sbis.ru/) в раздел «Контакты».  
2. Найти баннер **«Тензор»**, кликнуть по нему. Откроется [tensor.ru](https://tensor.ru/).  
3. Проверить, что на странице есть блок «Сила в людях».  
4. Перейти в этом блоке по ссылке «Подробнее» → `tensor.ru/about`.  
5. Проверить в разделе «Работаем», что у всех фотографий в хронологии одинаковые **ширина** и **высота**.

### Второй сценарий

1. Перейти на [sbis.ru](https://sbis.ru/) в раздел «Контакты».  
2. Проверить, что регион определяется автоматически (например, «Воронежская обл.») и есть список партнёров.  
3. Изменить регион на «Камчатский край».  
4. Проверить, что выбранный регион подставился, список партнёров изменился, а также что **URL** и **title** содержат информацию о новом регионе.

### Третий сценарий (дополнительный)

1. Перейти на [sbis.ru](https://sbis.ru/).  
2. В footer найти ссылку **«Скачать локальные версии»** и кликнуть.  
3. Скачать СБИС Плагин для Windows (веб-установщик).  
4. Убедиться, что файл скачался, а его размер в мегабайтах совпадает с указанным на сайте.

---

## Технологический стек

- **Python 3** — язык для автотестов
- **Pytest** — фреймворк для тестирования
- **Selenium WebDriver 4** — для управления браузером (Chrome)
- **PageObject** — паттерн проектирования для организации кода:
  - *SbisMainPage*: для действий на [sbis.ru](https://sbis.ru/)
  - *TensorPage*: для проверок на [tensor.ru](https://tensor.ru/)
  - *SbisDownloadPage*: для страницы скачивания локальных версий
  - *URLConstants*: хранит все основные ссылки (константы)
- **Allure** — для построения отчётов и прикрепления скриншотов
- **WebDriverManager** — автоматическая установка нужной версии ChromeDriver

---

## Автор: Соминский Антон