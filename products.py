# ANSI color constants
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a Product instance."""
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
        return self.quantity

    def set_quantity(self, quantity: int):
        if not isinstance(quantity, int):
            raise Exception(f"{RED}Quantity must be an integer.{RESET}")
        if quantity < 0:
            raise Exception(f"{RED}Quantity cannot be negative.{RESET}")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{CYAN}{self.name}{RESET}, Price: {YELLOW}${self.price}{RESET}, Quantity: {GREEN}{self.quantity}{RESET}")

    def buy(self, quantity: int) -> float:
        if not isinstance(quantity, int):
            raise Exception(f"{RED}Quantity must be an integer.{RESET}")
        if quantity <= 0:
            raise Exception(f"{RED}Quantity must be greater than zero.{RESET}")
        if quantity > self.quantity:
            raise Exception(f"{RED}Not enough quantity available to buy.{RESET}")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


# --------------------------- TESTING BLOCK ---------------------------------
def main():
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
