import pytest
from inventory import models

# mark - означает что я собираюсь разделить выполнение тестов
# и да, здесь я собираюсь построить фикстуру большую с бд
# для этого можно использовать разновидность фикстуры - parametrize

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (14, "trainers", "trainers", 0),
        (35, "football", "football", 1),
    ],
)  # нужно определить данные или таблицу
def test_inventory_category_dbfixture(
        db, django_db_setup_fixture, id, name, slug, is_active
):
    """
    Єто 1ий подход - использовать фикустуры данных, которые мы собираемся построить.
    :param db: даст доступ к Джанго бд
    :param django_db_setup_fixture: то, что мы уже создавали ранне - гаранитрует что тест бд будет создана и доступна +
    загрузить туда хардкорно юзера админа с json
    :param id, name, slug, is_active: our table columns
    :return:
    """
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "name, slug, is_active",
    [
        ("fashion", "fashion", 1),
        ("trainers", "trainers", 0),
        ("football", "football", 1),
    ],
)  # каждый из параметром это ОТДЕЛЬНЫЙ ТЕСТ
def test_inventory_category_insert_data(
        db, category_factory, name, slug, is_active
):
    """
    А 2ой подход - использовать favtory boy (дальше будет).
    т.к. мы используем инструмент django (factory boy), то id указывать ну нужно в параметрах
    :param db: даст доступ к Джанго бд
    :param category_factory: функция, которая позволит построить данные л
    :param name, slug, is_active: our table columns
    :return:
    """
    result = category_factory.create(name=name, slug=slug, is_active=is_active)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active



