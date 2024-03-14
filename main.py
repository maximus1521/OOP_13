
class Category:
    total_categories = 0
    num_of_products = 0

    def __init__(self, name, description, products):
        name: str
        description: str
        products: list
        self.name = name
        self.description = description
        self.products = products
        self.total_categories = 1

        Category.num_of_products += 1


class Product:
    num_of_products = 5

    def __init__(self, name, description, price, quantity):
        name: str
        description: str
        price: float
        quantity: int
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity
        Product.num_of_products += 1


prod1 = Product('Anchor', "goody", 1002.05, 5)
prod2 = Product('bollard', 'black', 200.33, 10)
prod3 = Product('line', 'long', 250.22, 8)

print(Product.num_of_products)