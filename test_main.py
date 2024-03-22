import pytest
from main import Category, Product


@pytest.fixture()
def category_ships():
    return Category('ships', 'all kind of ships', ['ship', 'barge', 'boat'])


def test_init_category(category_ships):
    assert category_ships.cat_name == 'ships'
    assert category_ships.cat_description == 'all kind of ships'
    assert category_ships.products == ['ship', 'barge', 'boat']


def test_total_categories_count():
    assert Category.total_categories == 1

    Category('Anchor', "goody", ['prod1', 'prod2', 'prod3'])
    assert Category.total_categories == 2

    Category('bollard', 'black', ['prod4', 'prod5'])
    assert Category.total_categories == 3


def test_all_products_count():
    assert Category.all_products == 8

    Category('Anchor', 'goody', ['prod4', 'prod5'])
    assert Category.all_products == 10

    Category('bollard', 'black', ['prod6', 'prod7', 'prod8'])
    assert Category.all_products == 13


def test_adding_products():
    pass


@pytest.fixture()
def product1_anchor():
    return Product('anchor', 'deep lying anchor', 7000.25, 2)


def test_init_product(product1_anchor):
    assert product1_anchor.prod_name == 'anchor'
    assert product1_anchor.prod_description == 'deep lying anchor'
    assert product1_anchor.price == 7000.25
    assert product1_anchor.quantity == 2
    #assert product1_anchor.list_product == ['anchor']



    Product('bollard', 'black', 5000.15, 5)
    """
    Testing attribute of Class Product
    """
    assert Product.list_product == ['anchor', 'bollard']


