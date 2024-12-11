"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product
from homework.models import Cart


@pytest.fixture
def book():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def notebook():
    return Product("notebook", price=35.50, description="White Notebook", quantity=300)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, book):
        # TODO напишите проверки на метод check_quantity
        assert book.check_quantity(book.quantity)  # 1000 == (1000) models.check_quantity -> True
        assert book.check_quantity(50)  # 1000 > (50) models.check_quantity -> True
        assert not book.check_quantity(2000)  # 1000 < (2000)  models.check_quantity -> False; for True used 'not'

    def test_product_buy(self, book):
        # TODO напишите проверки на метод buy
        quantity_in_stock = book.quantity  # Начальное количество товара на складе
        required_quantity = 1000  # Запрашиваемое количество товара (при > 1000 - ValueError: "Товара не хватает!!!")
        book.buy(required_quantity)  # Покупка товара с проверкаой на наличие запрашиваемого количества
        assert book.quantity == quantity_in_stock - required_quantity  # Проверяем остаток на складе на соответствие

    def test_product_buy_more_than_available(self, book):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            book.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_in_cart(self, cart, book):
        """
        Добавляем продукт в корзину.
        Проверяем что продукт добавился в корзину и в верном количесвте
        """
        cart.add_product(book, 10)
        assert cart.products[book] == 10
        assert book in cart.products.keys()

    def test_add_product_in_cart_more(self, cart, book):
        """
        Добавляем продукт в корзину
        Увеличиваем его количество
        Проверяем что продукт добавился в корзину и увеличился в количестве при повторном обращении
        """
        cart.add_product(book, 10)
        cart.add_product(book, 10)
        assert cart.products[book] == 20
        assert book in cart.products.keys()

    def test_remove_product_all(self, cart, book, notebook):
        """
        Добавляем продукты в корзину
        Проверяем что продукты добавились в корзину
        Удаляем все продукты полностью из карзины
        Проверяем, что в корзине не осталось ничего
        """
        cart.add_product(notebook, 10)
        cart.add_product(book, 30)
        assert book, notebook in cart.products.keys()
        cart.remove_product(notebook)
        cart.remove_product(book)
        assert notebook, book not in cart.products.keys()

    def test_remove_product_partially(self, cart, book, notebook):
        """
        Добавляем продукты в корзину
        Проверяем что продукты добавились в корзину
        Удаляем часть продуктов из карзины
        Проверяем, что осталось в корзине
        """
        cart.add_product(notebook, 10)
        cart.add_product(book, 30)
        assert book, notebook in cart.products.keys()
        cart.remove_product(notebook, 5)
        cart.remove_product(book, 10)
        assert cart.products[notebook] == 5
        assert cart.products[book] == 20

    def test_remove_product_partially_2(self, cart, book, notebook):
        """
        Добавляем продукты в корзину
        Проверяем что продукты добавились в корзину
        Удаляем полностью один продукт путём превышения количества в корзине
        Второй оставляем нетронутым
        Проверяем, что осталось в корзине
        """
        cart.add_product(notebook, 50)
        cart.add_product(book, 300)
        assert book, notebook in cart.products.keys()
        cart.remove_product(notebook, 100)
        assert notebook not in cart.products.keys()
        assert cart.products[book] == 300

    def test_clear_cart(self, cart, book, notebook):
        cart.add_product(book, 30)
        cart.add_product(notebook, 30)
        cart.clear()
        assert not cart.products
