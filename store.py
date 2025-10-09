"""store.py

This module defines the `Store` class, which manages a collection of `Product` objects.
It supports adding, removing, and listing products, calculating total quantity,
and processing customer orders interactively.

Author: Abhisakh Sarma
Date: 2025-10-09
"""


from typing import List, Tuple
from products import Product, RED, GREEN, YELLOW, RESET


class Store:
    """Manages a collection of products and handles customer orders."""
    def __init__(self, products: List[Product]) -> None:
        """
        Initialize the store with a list of Product instances.
        Args:
            products (List[Product]): List of products to add to the store.
        Raises:
            TypeError: If products is not a list or contains non-Product items.
        """
        if not isinstance(products, list):
            raise TypeError(f"{RED}Products must be provided as a list.{RESET}")
        if not all(isinstance(p, Product) for p in products):
            raise TypeError(f"{RED}All items in the list must be Product instances.{RESET}")

        self.products = products

    def add_product(self, product: Product) -> None:
        """
        Add a new product to the store.
        Args:
            product (Product): The product to add.
        Raises:
            TypeError: If product is not a Product instance.
        """
        if not isinstance(product, Product):
            raise TypeError(f"{RED}Only Product instances can be added.{RESET}")

        self.products.append(product)
        print(f"{GREEN}Added product: {product.name}{RESET}")

    def remove_product(self, product: Product) -> None:
        """
        Remove a product from the store.
        Args:
            product (Product): The product to remove.
        Raises:
            TypeError: If product is not a Product instance.
        """
        if not isinstance(product, Product):
            raise TypeError(f"{RED}Only Product instances can be removed.{RESET}")

        if product in self.products:
            self.products.remove(product)
            print(f"{YELLOW}Removed product: {product.name}{RESET}")

    def get_total_quantity(self) -> int:
        """
        Get total quantity of all products in the store.
        Returns:
            int: Total quantity available.
        """
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> List[Product]:
        """
        Get all active products in the store.
        Returns:
            List[Product]: List of active products.
        """
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Process an order given a shopping list of (Product, quantity) tuples.
        Args:
            shopping_list (List[Tuple[Product, int]]): List of items to buy.
        Returns:
            float: Total cost of the order.
        Raises:
            ValueError: If shopping list format is incorrect or quantities invalid.
            TypeError: If product in shopping list is not a Product instance.
        """
        total_cost = 0.0

        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError(
                    f"{RED}Each shopping list item must be (Product, quantity).{RESET}"
                )

            product, quantity = item

            if not isinstance(product, Product):
                raise TypeError(f"{RED}First element must be a Product.{RESET}")
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError(f"{RED}Quantity must be a positive integer.{RESET}")

            total_cost += product.buy(quantity)

        print(f"{GREEN}Order processed successfully!{RESET}")
        return total_cost


# --------------------------- TESTING BLOCK ---------------------------------
def main() -> None:
    """Test the Store class functionality with example data."""

    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
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
