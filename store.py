from typing import List
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        """
        Initialize the store with a list of Product instances.
        """
        if not isinstance(products, list):
            raise TypeError("Products must be provided as a list.")
        if not all(isinstance(p, Product) for p in products):
            raise TypeError("All items in the list must be Product instances.")

        self.products = products

    def add_product(self, product: Product):
        """
        Adds a new product to the store.
        """
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added.")
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store if it exists.
        """
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be removed.")
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns how many items (in total) are in the store.
        """
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> List[Product]:
        """
        Returns all products in the store that are active.
        """
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Accepts a list of (Product, quantity) tuples.
        Buys the products and returns the total price of the order.
        """
        total_cost = 0.0

        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each shopping list item must be a (Product, quantity) tuple.")

            product, quantity = item

            if not isinstance(product, Product):
                raise TypeError("First element of each tuple must be a Product.")
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Quantity must be a positive integer.")

            total_cost += product.buy(quantity)

        return total_cost


def main():
    import products

    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    all_products = best_buy.get_all_products()
    print(f"Total quantity in store: {best_buy.get_total_quantity()}")

    total_price = best_buy.order([
        (all_products[0], 1),
        (all_products[1], 2)
    ])

    print(f"Order cost: {total_price} dollars.")


if __name__ == "__main__":
    main()
