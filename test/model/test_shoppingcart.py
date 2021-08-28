import unittest

from src.model.customer import Customer
from src.model.product import Product
from src.model.shoppingcart import ShoppingCart

CUSTOMER = Customer("test")
PRICE = 100
PRODUCT = "T"


class ShoppingCartTest(unittest.TestCase):
    def test_should_calculate_price_with_no_discount(self):
        products = [Product(PRICE, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(100.00, order.total)

    def test_should_calculate_loyalty_points_with_no_discount(self):
        products = [Product(PRICE, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(20, order.loyalty_points)

    def test_should_calculate_price_with_10_percent_discount(self):
        products = [Product(PRICE, "DIS_10_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(90.00, order.total)

    def test_should_calculate_loyalty_points_with_10_percent_discount(self):
        products = [Product(PRICE, "DIS_10_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(10, order.loyalty_points)

    def test_should_calculate_price_with_15_percent_discount(self):
        products = [Product(PRICE, "DIS_15_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(85.00, order.total)

    def test_should_calculate_loyalty_points_with_15_percent_discount(self):
        products = [Product(PRICE, "DIS_15_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(6, order.loyalty_points)

    def test_should_calculate_price_with_20_percent_discount(self):
        products = [Product(PRICE, "DIS_20_ABCD", PRODUCT, 2)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(160.00, order.total)

    def test_should_calculate_loyalty_points_with_20_percent_discount(self):
        products = [Product(PRICE, "DIS_20_ABCD", PRODUCT, 2)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(10, order.loyalty_points)

    def test_should_add_product(self):
        new_product = [Product(PRICE, "", PRODUCT)]
        products = [Product(PRICE, "DIS_10_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)
        cart.add_product(new_product)

        order = cart.checkout()

        self.assertEqual(30, order.loyalty_points)
        self.assertEqual(190, order.total)

    def test_should_delete_product(self):
        del_product = Product(PRICE, "", PRODUCT)
        products = [Product(PRICE, "DIS_10_ABCD", PRODUCT), Product(PRICE, "", PRODUCT),
                    Product(PRICE, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)
        order = cart.checkout()
        self.assertEqual(50, order.loyalty_points)
        self.assertEqual(290, order.total)

        cart.delete_product(del_product)

        order = cart.checkout()
        self.assertEqual(10, order.loyalty_points)
        self.assertEqual(90, order.total)

    def test_should_calculate_price_with_BUY_2_GET_1(self):
        products = [Product(PRICE, "BUY_2_GET_1_ABCD", PRODUCT, 3)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(200.00, order.total)


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
