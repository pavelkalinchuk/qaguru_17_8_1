"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product
from homework.models import Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity)  # 1000 == (1000) models.check_quantity -> True
        assert product.check_quantity(50)  # 1000 > (50) models.check_quantity -> True
        assert not product.check_quantity(2000)  # 1000 < (2000)  models.check_quantity -> False; for True used 'not'

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        quantity_in_stock = product.quantity  # Начальное количество товара на складе
        required_quantity = 1000  # Запрашиваемое количество товара (при > 1000 - ValueError: "Товара не хватает!!!")
        product.buy(required_quantity)  # Покупка товара с проверкаой на наличие запрашиваемого количества
        assert product.quantity == quantity_in_stock - required_quantity  # Проверяем остаток на складе на соответствие

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_in_cart(self, cart, product):
        """
        Добавляем продукт в корзину.
        Проверяем что продукт добавился в корзину и в верном количесвте
        """
        cart.add_product(product, 10)
        print(product)
        assert cart.products[product] == 10
        assert product in cart.products.keys()

    def test_add_product_in_cart_more(self, cart, product):
        """
        Добавляем продукт в корзину
        Увеличиваем его количество
        Проверяем что продукт добавился в корзину и увеличился в количестве при повторном обращении
        С учётом того, что при каждом запуске метода, идентификатор продукта меняется, то пришлось завести
        переменную product_2, скинуть идентификатор полученный при первом вызове и использовать его при
        повторном вызове что бы в карзине выполнилось требования по увеличению количества уже имеющегося продукта
        """
        cart.add_product(product, 10)
        product_2 = product
        cart.add_product(product_2, 10)
        assert cart.products[product] == 20
        assert product in cart.products.keys()