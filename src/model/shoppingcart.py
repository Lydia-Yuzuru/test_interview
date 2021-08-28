from src.model.product import Product
from src.model.customer import Customer
from src.model.order import Order


class ShoppingCart:
    def __init__(self, customer=Customer, products=[]):
        self.products = products
        self.customer = customer

    def add_product(self, product):
        # self.products.append(product)  # product为Product类
        self.products.extend(product)  # product为List

    def delete_product(self, product):
        for p in self.products[::-1]:  # 正序删除到只剩一个，倒叙删除全部
            if p.product_code == product.product_code:
                self.products.remove(p)

    def checkout(self):
        total_price = 0.00
        loyalty_points_earned = 0.00
        for product in self.products:
            discount = 0.00
            if product.product_code.startswith("DIS_10"):
                loyalty_points_earned += product.count * (product.price / 10)
                discount = product.count * product.price * 0.1
            elif product.product_code.startswith("DIS_15"):
                loyalty_points_earned += product.count * (product.price / 15)
                discount = product.count * product.price * 0.15
            elif product.product_code.startswith("DIS_20"):
                loyalty_points_earned += product.count * (product.price / 20)
                discount = product.count * product.price * 0.2
            elif product.product_code.startswith("BUY_2_GET_1"):
                discount = (product.count // 3) * product.price
            else:
                loyalty_points_earned += product.count * (product.price / 5)
                discount = 0.00
            total_price += product.count * product.price - discount
        return Order(int(loyalty_points_earned), total_price)

    def __str__(self):
        product_list = "".join('%s' % product for product in self.products)
        return "Customer: %s \nBought: \n%s" % (self.customer, product_list)
