import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_create_new_admin_user(create_admin_user):
    assert create_admin_user.__str__() == "nick-admin"


@pytest.mark.selenium
def test_dashboard_admin_login(live_server, create_admin_user,  chrome_browser_instance):
    browser = chrome_browser_instance

    url = live_server.url # live_server - метод из pytest имитрует живой сервер
    route = "/admin/login/"
    browser.get(f"{url}{route}")

    user_name = browser.find_element(By.NAME, "username")
    uer_password = browser.find_element(By.NAME, "password")
    submit_key = browser.find_element(By.XPATH, "//input[@value='Log in']")

    user_name.send_keys("nick-admin")
    uer_password.send_keys("111111")
    submit_key.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
