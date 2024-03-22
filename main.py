class Category:
    total_categories = 0  # int
    all_products = 0  # int

    def __init__(self, cat_name, cat_description, products):

        cat_name: str
        cat_description: str
        products: list
        self.cat_name = cat_name
        self.cat_description = cat_description
        self.__products = products

        Category.total_categories += 1
        Category.all_products += len(products)

    def adding_products(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise ValueError("product should be from Class Product")

    @property  # getter for product
    def beautiful_product(self):
        return self.__products

    @beautiful_product.setter  # setter for product
    def beautiful_product(self, product):
        for prod in product:
            print(f'For {prod[0]}, {prod[1]} RUB. Stock: {prod[3]} pcs')


class Product:

    def __init__(self, prod_name, prod_description, price, quantity):
        prod_name: str
        prod_description: str
        price: float
        quantity: int
        self.prod_name = prod_name
        self.prod_description = prod_description
        self.price = float(price)
        self.quantity = quantity

    @classmethod  # make new object of product based on class Product
    def product_for_list(cls, prod_name, prod_description, price, quantity):
        list_of_products = []
        new_product = cls(prod_name, prod_description, price, quantity)
        return list_of_products.append(new_product)

