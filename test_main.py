import pytest
from main import Category, Product


@pytest.fixture()
def category_ship():
    return Category('Vega', 'container ship', ['ships', 'barges', 'boats'])


def test_init_category(category_ship):
    assert category_ship.name == 'Vega'
    assert category_ship.description == 'container ship'
    assert category_ship.products == ['ships', 'barges', 'boats']
    assert category_ship.total_categories == 1


@pytest.fixture()
def product1_anchor():
    return Product('anchor', 'deep lying anchor', 7000.25, 2)


def test_init_product(product1_anchor):
    assert product1_anchor.name == 'anchor'
    assert product1_anchor.description == 'deep lying anchor'
    assert product1_anchor.price == 7000.25
    assert product1_anchor.quantity == 2


@pytest.fixture()
def total_categories_count():
    return Category('Vega', 'container ship', ['ships', 'barges', 'boats'])


def test_categories_count(total_categories_count):
    assert total_categories_count.total_categories == 1
    assert total_categories_count.num_of_products == 1
