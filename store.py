from typing import List
from products import Product, RED, GREEN, YELLOW, CYAN, RESET


class Store:
    def __init__(self, products: List[Product]):
        if not isinstance(products, list):
            raise TypeError(f"{RED}Products must be provided as a list.{RESET}")
        if not all(isinstance(p, Product) for p in products):
            raise TypeError(f"{RED}All items in the list must be Product instances.{RESET}")
        self.products = products

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError(f"{RED}Only Product instances can be added.{RESET}")
        self.products.append(product)
        print(f"{GREEN}Added product: {product.name}{RESET}")

    def remove_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError(f"{RED}Only Product instances can be removed.{RESET}")
        if product in self.products:
            self.products.remove(product)
            print(f"{YELLOW}Removed product: {product.name}{RESET}")

    def get_total_quantity(self) -> int:
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> List[Product]:
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        total_cost = 0.0
        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError(f"{RED}Each shopping list item must be (Product, quantity).{RESET}")

            product, quantity = item

            if not isinstance(product, Product):
                raise TypeError(f"{RED}First element must be a Product.{RESET}")
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError(f"{RED}Quantity must be a positive integer.{RESET}")

            total_cost += product.buy(quantity)

        print(f"{GREEN}Order processed successfully!{RESET}")
        return total_cost


#--------------------------- TESTING BLOCK ---------------------------------
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
