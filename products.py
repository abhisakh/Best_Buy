class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a Product instance with name, price, and quantity.
        Raises exceptions if inputs are invalid.
        """

        # Validate name
        if not isinstance(name, str) or not name.strip():
            raise Exception("Product name cannot be empty.")

        # Validate price
        if not isinstance(price, (int, float)):
            raise Exception("Price must be a number.")
        if price < 0:
            raise Exception("Price cannot be negative.")

        # Validate quantity
        if not isinstance(quantity, int):
            raise Exception("Quantity must be an integer.")
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")

        # Initialize attributes
        self.name = name.strip()
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current quantity."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Updates the quantity.
        If quantity reaches 0, deactivates the product.
        """
        if not isinstance(quantity, int):
            raise Exception("Quantity must be an integer.")
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Prints a readable string with product details."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price.
        Raises Exception if quantity is invalid or unavailable.
        """
        if not isinstance(quantity, int):
            raise Exception("Quantity must be an integer.")
        if quantity <= 0:
            raise Exception("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity available to buy.")

        total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)

        return total_price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))     # Should print 12500.0
    print(mac.buy(100))     # Should print 145000.0
    print(mac.is_active())  # Should print False (since quantity = 0)

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()

