import pytest
from main import Category, Product


@pytest.fixture()
def category_ships():
    return Category('ships', 'all kind of ships', ['ship', 'barge', 'boat'])


def test_init_category(category_ships):
    assert category_ships.name == 'ships'
    assert category_ships.description == 'all kind of ships'
    assert category_ships.products == ['ship', 'barge', 'boat']


def test_total_categories_count():
    assert Category.total_categories == 1

    Category('Anchor', "goody", ['prod1', 'prod2', 'prod3'])
    assert Category.total_categories == 2

    Category('bollard', 'black', ['prod4', 'prod5'])
    assert Category.total_categories == 3


def test_all_products_count():
    assert Category.all_products == 8

    Category('Anchor', 'goody', ["prod1", "prod2", "prod3"])
    assert Category.all_products == 11

    Category('bollard', 'black', ['prod4', 'prod5', 'prod6'])
    assert Category.all_products == 14


@pytest.fixture()
def product1_anchor():
    return Product('anchor', 'deep lying anchor', 7000.25, 2)


def test_init_product(product1_anchor):
    assert product1_anchor.name == 'anchor'
    assert product1_anchor.description == 'deep lying anchor'
    assert product1_anchor.price == 7000.25
    assert product1_anchor.quantity == 2

