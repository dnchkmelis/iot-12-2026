"""Classes for managing a sports shoe store."""

import math
from typing import NamedTuple


class SneakerDetails(NamedTuple):
    """Details used to create a pair of sneakers."""

    brand: str
    size: float
    color: str
    price: float
    quantity: int
    material: str
    number_of_sales: int


class Sneakers:
    """Represent a pair of sneakers."""

    def __init__(self, details: SneakerDetails):
        """Initialize a pair of sneakers."""
        self._details = details
        self.price = details.price
        self.quantity = details.quantity
        self.number_of_sales = details.number_of_sales
        print(f"Створено об'єкт кросівок: {self.brand} (розмір: {self.size})")

    def __del__(self):
        """Report when the sneaker object is deleted."""
        print(f"Видалено об'єкт кросівок: {self.brand}")

    @property
    def brand(self):
        """Return the sneaker brand."""
        return self._details.brand

    @brand.setter
    def brand(self, value):
        """Set the sneaker brand."""
        self._details = self._details._replace(brand=value)

    @property
    def size(self):
        """Return the sneaker size."""
        return self._details.size

    @size.setter
    def size(self, value):
        """Set the sneaker size."""
        self._details = self._details._replace(size=value)

    @property
    def color(self):
        """Return the sneaker color."""
        return self._details.color

    @color.setter
    def color(self, value):
        """Set the sneaker color."""
        self._details = self._details._replace(color=value)

    @property
    def price(self):
        """Return the sneaker price."""
        return self._details.price

    @price.setter
    def price(self, value):
        """Set the sneaker price."""
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or isinstance(value, float) and not math.isfinite(value)
        ):
            raise ValueError("Ціна має бути коректним числом.")
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною.")
        self._details = self._details._replace(price=value)

    @property
    def quantity(self):
        """Return the quantity in stock."""
        return self._details.quantity

    @quantity.setter
    def quantity(self, value):
        """Set the quantity in stock."""
        if value < 0:
            raise ValueError("Кількість на складі не може бути від'ємною.")
        self._details = self._details._replace(quantity=value)

    @property
    def material(self):
        """Return the sneaker material."""
        return self._details.material

    @material.setter
    def material(self, value):
        """Set the sneaker material."""
        self._details = self._details._replace(material=value)

    @property
    def number_of_sales(self):
        """Return the number of sold pairs."""
        return self._details.number_of_sales

    @number_of_sales.setter
    def number_of_sales(self, value):
        """Set the number of sold pairs."""
        if value < 0:
            raise ValueError("Кількість продажів не може бути від'ємною.")
        self._details = self._details._replace(number_of_sales=value)

    def __str__(self):
        """Return a human-readable description of the sneakers."""
        return (
            f"Бренд: {self.brand}, Розмір: {self.size}, Колір: {self.color}, "
            f"Ціна: {self.price} грн, Кількість на складі: {self.quantity}, "
            f"Матеріал: {self.material}, Продано пар: {self.number_of_sales}"
        )


class SportShoesStore:
    """Manage a sports shoe store assortment."""

    def __init__(self, store_name: str):
        """Initialize the sports shoe store."""
        self._store_name = store_name
        self._assortment = []
        print(f"Магазин спортивного взуття '{self._store_name}' відкрито.")

    def __del__(self):
        """Report when the store object is deleted."""
        print(f"Магазин '{self._store_name}' закривається.")

    def add_sneakers(self, sneakers: Sneakers):
        """Add sneakers to the assortment."""
        self._assortment.append(sneakers)

    def display_assortment(self):
        """Print all sneakers in the assortment."""
        print(f"\n--- Асортимент магазину '{self._store_name}' ---")
        if not self._assortment:
            print("Асортимент порожній.")
        for item in self._assortment:
            print(item)
        print("-" * 130)

    def sort_by_price(self, ascending=True):
        """Sort sneakers by price."""
        self._assortment.sort(key=lambda x: x.price, reverse=not ascending)

    def sort_by_quantity(self, ascending=True):
        """Sort sneakers by stock quantity."""
        self._assortment.sort(key=lambda x: x.quantity, reverse=not ascending)

    def get_top_popular(self, top_n=3):
        """Print the most popular sneakers by number of sales."""
        sorted_by_sales = sorted(
            self._assortment, key=lambda x: x.number_of_sales, reverse=True
        )
        print(f"\n--- ТОП-{top_n} найпопулярніших кросівок ---")

        for i, item in enumerate(sorted_by_sales[:top_n], 1):
            print(
                f"{i}. Бренд: {item.brand} | Продано: "
                f"{item.number_of_sales} пар | Ціна: {item.price} грн"
            )
        print("-" * 130)


def main():
    """Run a demonstration of the store operations."""
    s1 = Sneakers(SneakerDetails("Nike", 42.5, "Чорний", 3500.0, 15, "Шкіра", 120))
    s2 = Sneakers(SneakerDetails("Adidas", 41.0, "Білий", 2800.0, 8, "Текстиль", 210))
    s3 = Sneakers(
        SneakerDetails("Puma", 43.0, "Синій", 2200.0, 25, "Штучна шкіра", 45)
    )

    store = SportShoesStore("TopStep")
    store.add_sneakers(s1)
    store.add_sneakers(s2)
    store.add_sneakers(s3)

    store.display_assortment()

    store.sort_by_price()
    print("\nПісля сортування за ціною:")
    store.display_assortment()

    store.sort_by_quantity()
    print("\nПісля сортування за кількістю на складі:")
    store.display_assortment()

    store.get_top_popular(top_n=2)


if __name__ == "__main__":
    main()
