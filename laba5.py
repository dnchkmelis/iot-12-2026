"""Classes for managing a sports shoe store."""

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
        self._brand = details.brand
        self._size = details.size
        self._color = details.color
        self.price = details.price
        self.quantity = details.quantity
        self._material = details.material
        self._number_of_sales = details.number_of_sales
        print(f"Створено об'єкт кросівок: {self._brand} (розмір: {self._size})")

    def __del__(self):
        """Report when the sneaker object is deleted."""
        print(f"Видалено об'єкт кросівок: {self._brand}")

    @property
    def brand(self):
        """Return the sneaker brand."""
        return self._brand

    @brand.setter
    def brand(self, value):
        """Set the sneaker brand."""
        self._brand = value

    @property
    def size(self):
        """Return the sneaker size."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the sneaker size."""
        self._size = value

    @property
    def color(self):
        """Return the sneaker color."""
        return self._color

    @color.setter
    def color(self, value):
        """Set the sneaker color."""
        self._color = value

    @property
    def price(self):
        """Return the sneaker price."""
        return self._price

    @price.setter
    def price(self, value):
        """Set the sneaker price."""
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною.")
        self._price = value

    @property
    def quantity(self):
        """Return the quantity in stock."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Set the quantity in stock."""
        if value < 0:
            raise ValueError("Кількість на складі не може бути від'ємною.")
        self._quantity = value

    @property
    def material(self):
        """Return the sneaker material."""
        return self._material

    @material.setter
    def material(self, value):
        """Set the sneaker material."""
        self._material = value

    @property
    def number_of_sales(self):
        """Return the number of sold pairs."""
        return self._number_of_sales

    @number_of_sales.setter
    def number_of_sales(self, value):
        """Set the number of sold pairs."""
        self._number_of_sales = value

    def __str__(self):
        """Return a human-readable description of the sneakers."""
        return (
            f"Бренд: {self._brand}, Розмір: {self._size}, Колір: {self._color}, "
            f"Ціна: {self._price} грн, Кількість на складі: {self._quantity}, "
            f"Матеріал: {self._material}, Продано пар: {self._number_of_sales}"
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
