# ANSI color constants
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLACK = "\033[30m"
WHITE_BG = "\033[107m"
GREY_BG = "\033[100m"
RESET = "\033[0m"


class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Initialize a Product instance.
        Args:
            name (str): The name of the product. Must not be empty.
            price (float): The price of the product. Must be non-negative.
            quantity (int): The quantity available. Must be non-negative.
        Raises:
            Exception: If any of the arguments are invalid.
        """
        if not isinstance(name, str) or not name.strip():
            raise Exception(f"{RED}Product name cannot be empty.{RESET}")

        if not isinstance(price, (int, float)):
            raise Exception(f"{RED}Price must be a number.{RESET}")
        if price < 0:
            raise Exception(f"{RED}Price cannot be negative.{RESET}")

        if not isinstance(quantity, int):
            raise Exception(f"{RED}Quantity must be an integer.{RESET}")
        if quantity < 0:
            raise Exception(f"{RED}Quantity cannot be negative.{RESET}")

        self.name = name.strip()
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Get the current quantity of the product.
        Returns:
            int: The quantity available.
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Set the quantity of the product.
        If the quantity is zero, the product is deactivated.
        Args:
            quantity (int): New quantity. Must be non-negative.
        Raises:
            Exception: If quantity is invalid.
        """
        if not isinstance(quantity, int):
            raise Exception(f"{RED}Quantity must be an integer.{RESET}")
        if quantity < 0:
            raise Exception(f"{RED}Quantity cannot be negative.{RESET}")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Check if the product is active.
        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self) -> None:
        """Activate the product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivate the product."""
        self.active = False

    def show(self) -> None:
        """Print the product details with colors."""
        print(
            f"{CYAN}{self.name}{RESET}, Price: {YELLOW}${self.price}{RESET}, "
            f"Quantity: {GREEN}{self.quantity}{RESET}"
        )

    def buy(self, quantity: int) -> float:
        """
        Purchase a given quantity of the product.
        Args:
            quantity (int): Number of items to buy. Must be positive and less than or
                equal to available quantity.
        Returns:
            float: Total price of the purchased quantity.
        Raises:
            Exception: If quantity is invalid or exceeds available stock.
        """
        if not isinstance(quantity, int):
            raise Exception(f"{RED}Quantity must be an integer.{RESET}")
        if quantity <= 0:
            raise Exception(f"{RED}Quantity must be greater than zero.{RESET}")
        if quantity > self.quantity:
            raise Exception(f"{RED}Not enough quantity available to buy.{RESET}")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price

#-------------------------- TEST BLOCK ----------------------------------
def main() -> None:
    """Test the Product class functionality."""
    bose = Product("Bose QuietComfort Earbuds", 250, 500)
    mac = Product("MacBook Air M2", 1450, 100)

    try:
        print(bose.buy(501))
    except Exception as e:
        print(e)

    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
