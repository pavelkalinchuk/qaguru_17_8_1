"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


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
        pass


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
