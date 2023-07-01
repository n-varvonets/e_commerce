import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User

# 1.file name should start with test_%
# 2.def also should start with test%
# 3. in pytest.ini we can manage this names

# 4.mark - маркировка, selenium - метадата из pytest.ini. Маркировка позволяет отфильтровать выьзов тестов.
# Нужно что б различать запуск тестов.
# selenium - импользование фикстуры(то что вызывается ПЕРЕД а) с pytest.ini -> conftest -> test.selenium -> позволит нам не запускать драйвер
# @pytest.mark.selenium
# def test_create_new_admin_user(create_admin_user):
#     """
#     Когда запускаются тесты, то БД джанго не используется,
#     поэтому для этого модуля нужно создавать каждый раз новго ФЕЙКОВОГО админа
#     :param create_admin_user: функция в test.fixture которая создаст нового админа и сразу проверит его имя
#     :return:
#     """
#     assert create_admin_user.__str__() == "nick-admin"


@pytest.mark.selenium
def test_dashboard_admin_login(live_server, django_db_setup_fixture,  chrome_browser_instance):
    """

    :param live_server: встроенная фигня pytestь которая запускает сервер localhost в бекграунде
    :param create_admin_user: фикстурная функция в test.fixture которая создаст нового админа
    :param chrome_browser_instance: фикстурная функция в test.selenium которая создаст webdriver
    :return:
    """
    browser = chrome_browser_instance

    user_1 = User.objects.get(pk=1)
    print("pass- ", user_1.password)
    from django.contrib.auth.hashers import make_password
    make_password("111111")

    url = live_server.url  # live_server - метод из pytest имитрует живой сервер
    route = "/admin/login/"
    browser.get(f"{url}{route}")

    user_name = browser.find_element(By.NAME, "username")
    uer_password = browser.find_element(By.NAME, "password")
    submit_key = browser.find_element(By.XPATH, "//input[@value='Log in']")

    user_name.send_keys("nick-admin")
    uer_password.send_keys("111111")
    submit_key.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
