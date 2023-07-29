import pytest
from inventory import models

# mark - означает что я собираюсь разделить выполнение тестов
# и да, здесь я собираюсь построить фикстуру большую с бд
# для этого можно использовать разновидность фикстуры - parametrize

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 0),
        (18, "trainers", "trainers", 1),
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
    "slug, is_active",
    # "name, slug, is_active",
    # [
    #     ("fashion", "fashion", 0),
    #     ("trainers", "trainers", 1),
    #     ("football", "football", 1),
    # ],
    [
        ( "fashion", 0),
        ("trainers", 1),
        ( "football", 1),
    ],
)  # каждый из параметром это ОТДЕЛЬНЫЙ ТЕСТ
def test_inventory_category_insert_data(
        db, category_factory, slug, is_active
        # db, category_factory, name, slug, is_active
):
    """
    А 2ой подход - использовать favtory boy (дальше будет).
    т.к. мы используем инструмент django (factory boy), то id указывать ну нужно в параметрах
    :param db: даст доступ к Джанго бд
    :param category_factory: функция, которая позволит построить данные л
    :param name, slug, is_active: our table columns
    :return:
    """
    # result = category_factory.create(name=name, slug=slug, is_active=is_active)

    # in this case we not gonna to take name parameter,
    # cause of factories will create it auto
    result = category_factory.create(slug=slug, is_active=is_active)
    print(result.name)
    # assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active



