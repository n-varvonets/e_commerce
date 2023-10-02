import pytest
from django.db import IntegrityError

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
        ("fashion", 0),
        ("trainers", 1),
        ("football", 1),
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
    # print(result.name)
    # assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, created_at, updated_at",
    [
        (
                1,
                "45425810",
                "widstar running sneakers",
                "widstar-running-sneakers",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
                1,
                "2022-01-01 14:18:33",
                "2022-01-01 14:18:33",
        ),
        (
                8616,
                "45434425",
                "impact puse dance shoe",
                "impact-puse-dance-shoe",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
                1,
                "2022-01-01 14:18:33",
                "2022-01-01 14:18:33",
        ),
    ],
)
def test_inventory_db_product_dbfixture(
        db, django_db_setup_fixture, id, web_id, name, slug, description, is_active, created_at, updated_at
):
    result = models.Product.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_db_product_uniqueness_in_integrity(db, product_factory):
    """negative test on crush the web_id on uniqueness"""
    new_web_id = product_factory.create(web_id=123456789)  # here we created a one
    with pytest.raises(IntegrityError):
        product_factory.create(web_id=123456789)  # here we try to create more with same web_id - unique err


@pytest.mark.dbfixture
def test_inventory_db_product_insert_data(
        db, product_factory, category_factory
):
    """
    make M2M relation  (new_category&new_product,  )

    steps:
        - build new category and assign products to different categories;
        -
    """
    # new_category = category_factory.create()
    new_product = product_factory.create(
        category=(1, 11))  # передаем ids категорій к продукту с которым хотим заметчит его
    result_product_category = new_product.category.all()  # we find all categories associated with  new_product (1,36)
    print(result_product_category)  # <TreeQuerySet [<Category: fashion>, <Category: booties>]>
    assert "web_id_" in new_product.web_id
    assert result_product_category.count() == 2  # count работает
    # python manage.py load-fixtures


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, sale_price, weight, created_at, updated_at",
    [
        (
                1,
                "7633969397",
                "934093051374",
                1,
                1,
                1,
                1,
                97.00,
                92.00,
                46.00,
                987,
                "2021-09-04 22:14:18",
                "2021-09-04 22:14:18",
        ),
        (
                8616,
                "3880741573",
                "844935525855",
                1,
                8616,
                1253,
                1,
                89.00,
                84.00,
                42.00,
                929,
                "2021-09-04 22:14:18",
                "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_db_produt_inventory_dataset(
        db,
        django_db_setup_fixture,  # django_db_setup,
        id,
        sku,
        upc,
        product_type,
        product,
        brand,
        is_active,
        retail_price,
        store_price,
        sale_price,
        weight,
        created_at,
        updated_at
):  # just matching data with data in db
    result = models.ProductInventory.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.sku == sku
    assert result.upc == upc
    assert result.product_type.id == product_type
    assert result.product.id == product
    assert result.brand.id == brand
    assert result.is_active == is_active
    assert result.retail_price == retail_price
    assert result.store_price == store_price
    assert result.sale_price == sale_price
    assert result.weight == weight
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_db_product_inventory_insert_data(
        db, product_inventory_factory
):  # db here's for access to DB(required)
    new_product = product_inventory_factory.create(
        sku="123456789",  # put a new value(special for Product inventory)
        upc="123456789",  # put a new value(special for Product inventory)
        product_type__name="new_name",  # overwrite  (in new model product_type)
        product__web_id="123456789",  # overwrite (in new model product)
        brand__name="new_name",  # overwrite (in new model brand)
    )
    assert new_product.sku == "123456789"
    assert new_product.upc == "123456789"
    assert new_product.product_type.name == "new_name"
    assert new_product.product.web_id == "123456789"
    assert new_product.brand.name == "new_name"
    assert new_product.is_active == 1
    assert new_product.retail_price == 97.00  # static
    assert new_product.store_price == 92.00  # static
    assert new_product.sale_price == 46.00  # static
    assert new_product.weight == 987  # static


def test_inventory_db_producttype_insert_data(db, product_type_factory):

    new_type = product_type_factory.create(name="demo_type")
    assert new_type.name == "demo_type"


def test_inventory_db_producttype_uniqueness_integrity(
    db, product_type_factory
):
    product_type_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        product_type_factory.create(name="not_unique")


def test_inventory_db_brand_insert_data(db, brand_factory):

    new_brand = brand_factory.create(name="demo_brand")
    assert new_brand.name == "demo_brand"


def test_inventory_db_brand_uniqueness_integrity(db, brand_factory):
    brand_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        brand_factory.create(name="not_unique")
