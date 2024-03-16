class Category:
    total_categories = 0
    all_products = 0

    def __init__(self, name, description, products):

        name: str
        description: str
        products: list
        self.name = name
        self.description = description
        self.products = products

        Category.total_categories += 1
        Category.all_products += len(products)


class Product:

    def __init__(self, name, description, price, quantity):
        name: str
        description: str
        price: float
        quantity: int
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity
