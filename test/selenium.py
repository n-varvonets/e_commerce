import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")  # fixture - прикрепить эту функцию к тесту ПЕРЕД ее выполнением
def chrome_browser_instance(request):
    """
    Provide a selenium webdriver instance BEFORE executing.

    Fixture в pytest - это специальная функция, которая позволяет настроить некоторые параметры или объекты перед выполнением тестов.
    Scope в этом контексте определяет, когда и как часто будет вызываться и уничтожаться фикстура.
    scope="module" означает, что фикстура будет создаваться один раз на весь модуль и уничтожаться после того, как все тесты в этом модуле будут выполнены.

    Вот краткое описание различных областей применения (scope) в pytest:
        "function" (по умолчанию): фикстура создается и уничтожается для каждого тестового случая.
        "class": фикстура создается и уничтожается для каждого класса тестов.
        "module": фикстура создается и уничтожается для каждого модуля тестов.
        "package": фикстура создается и уничтожается для каждого пакета тестов.
        "session": фикстура создается в начале выполнения тестовой сессии и уничтожается после завершения всех тестов.

    "Module" (модуль) в Python — это файл, содержащий код Python. Имя модуля совпадает с именем файла (без .py).
     Например, если у вас есть файл test_example.py, то он представляет собой один модуль.

    "Package" (пакет) в Python — это способ организации связанных модулей вместе внутри единого каталога.
     Пакет Python — это каталог, который содержит файл __init__.py и может включать в себя другие модули и пакеты.

    :param request:
    :return:
    """
    options = Options()
    # Добавьте этот аргумент только если вам нужен режим без головы:
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()

