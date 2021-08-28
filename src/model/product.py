class Product:
    def __init__(self, price, product_code, name, count):
        self.price = price
        self.product_code = product_code
        self.name = name
        self.count = count

    def __str__(self):
        return " Name: %s \n Price: %s \n Count: %s \n" % (self.name, self.price, self.count)
