import pytest
from django.core.management import call_command  # this allows to execute some cmds(retiving data from test_db fixture)

# @pytest.fixture
# def create_admin_user(django_user_model):
#     """
#     УЖЕ НЕ НУЖНО Т.К. создали тектувую бд ниже django_db_setup
#     :param django_user_model:
#     :return:  admin_user
#     """
#     return django_user_model.objects.create_superuser("nick-admin", "a@a,com", "111111")


@pytest.fixture(scope="session")
def django_db_setup_fixture(django_db_setup, django_db_blocker):
    """
    Load DB data fixtures
    :param django_db_setup: гарантирует что тест_бд будет создана и доступна
    :param django_db_blocker: нужно что б заброкировать/разблокировать записть/чтение в бд
    :return:

    1. django_db_setup:
        - Предоставляет способ разрушения тестовых баз данных после завершения тестов.
        - отвечает за настройку тестовых баз данных в вашем проекте  (обрабатывает параметры настройки базы данных,
         такие как использование миграций, создание новой базы данных или сохранение существующей.)
    2.Фикстура django_db_setup_fixture - является более высокоуровневой фикстурой, построенной поверх django_db_setup.

    """
    with django_db_blocker.unblock():
        call_command("loaddata", "/Users/nick-v/PycharmProjects/e_commerce/dashboard/fixtures/db_admin_fixture.json")  # как в терминале запуск команды для загрузки хардкодной бд
        call_command("loaddata", "/Users/nick-v/PycharmProjects/e_commerce/inventory/fixtures/db_category_fixture.json")
        call_command("loaddata", "/Users/nick-v/PycharmProjects/e_commerce/inventory/fixtures/db_product_fixture.json")
        # порядок имеет значение
        call_command("loaddata", "/Users/nick-v/PycharmProjects/e_commerce/inventory/fixtures/db_brand_fixture.json")
        call_command("loaddata", "/Users/nick-v/PycharmProjects/e_commerce/inventory/fixtures/db_type_fixture.json")
        call_command("loaddata",
                     "/Users/nick-v/PycharmProjects/e_commerce/inventory/fixtures/db_product_inventory_fixture.json")

