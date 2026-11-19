class Sneakers:
    def __init__(
        self,
        brand: str,
        size: float,
        color: str,
        price: float,
        quantity: int,
        material: str,
        numberOfSales: int,
    ):
        self._brand = brand
        self._size = size
        self._color = color
        self._price = price
        self._quantity = quantity
        self._material = material
        self._numberOfSales = numberOfSales
        print(f"Створено об'єкт кросівок: {self._brand} (розмір: {self._size})")

    def __del__(self):
        print(f"Видалено об'єкт кросівок: {self._brand}")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value

    @property
    def numberOfSales(self):
        return self._numberOfSales

    @numberOfSales.setter
    def numberOfSales(self, value):
        self._numberOfSales = value

    def __str__(self):
        return f"Бренд: {self._brand}, Розмір: {self._size}, Колір: {self._color}, " \
              f"Ціна: {self._price} грн, Кількість на складі: {self._quantity}, " \
              f"Матеріал: {self._material}, Продано пар: {self._numberOfSales}"


class SportShoesStore:
    def __init__(self, store_name: str):
        self._store_name = store_name
        self._assortment = []  
        print(f"Магазин спортивного взуття '{self._store_name}' відкрито.")

    def __del__(self):
        print(f"Магазин '{self._store_name}' закривається.")

    def add_sneakers(self, sneakers: Sneakers):
        self._assortment.append(sneakers)

    def display_assortment(self):
        print(f"\n--- Асортимент магазину '{self._store_name}' ---")
        if not self._assortment:
            print("Асортимент порожній.")
        for item in self._assortment:
            print(item)
        print("-" * 130)

    def sort_by_price(self, ascending=True):
        """Сортування взуття за ціною"""
        self._assortment.sort(key=lambda x: x.price, reverse=not ascending)

    def sort_by_quantity(self, ascending=True):
        """Сортування взуття за кількістю на складі"""
        self._assortment.sort(key=lambda x: x.quantity, reverse=not ascending)

    def get_top_popular(self, top_n=3):
        """Виведення топ найпопулярніших кросівок за кількістю продажів"""
        sorted_by_sales = sorted(self._assortment, key=lambda x: x.numberOfSales, reverse=True)
        print(f"\n--- ТОП-{top_n} найпопулярніших кросівок ---")

        for i, item in enumerate(sorted_by_sales[:top_n], 1):
            print(f"{i}. Бренд: {item.brand} | Продано: {item.numberOfSales} пар | Ціна: {item.price} грн")
        print("-" * 130)


def main():
    s1 = Sneakers("Nike", 42.5, "Чорний", 3500.0, 15, "Шкіра", 120)
    s2 = Sneakers("Adidas", 41.0, "Білий", 2800.0, 8, "Текстиль", 210)
    s3 = Sneakers("Puma", 43.0, "Синій", 2200.0, 25, "Штучна шкіра", 45)

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

