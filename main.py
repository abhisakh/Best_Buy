import products
import store
from products import RED, GREEN, YELLOW, CYAN, RESET


# Setup inventory
product_list = [
    products.Product("MacBook Air M2", 1450, 100),
    products.Product("Bose QuietComfort Earbuds", 250, 500),
    products.Product("Google Pixel 7", 500, 250),
]
best_buy = store.Store(product_list)


def list_products():
    print(f"{CYAN}{'_' * 50}{RESET}")
    print(f"\n{CYAN}Available Products:{RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")
    for product in best_buy.get_all_products():
        product.show()


def show_total():
    total = best_buy.get_total_quantity()
    print(f"{YELLOW}Total items in store:{RESET} {GREEN}{total}{RESET}")


def make_order():
    available = best_buy.get_all_products()
    shopping_list = []

    print(f"\n{CYAN}Available Products:{RESET}")
    for i, product in enumerate(available, start=1):
        print(f"{i}. {product.name} - ${product.price} (Qty: {product.quantity})")

    while True:
        choice = input(f"{YELLOW}\nEnter product number (or 'done' to finish): {RESET}")
        if choice.lower() == 'done':
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(available)):
            print(f"{RED}Invalid selection, try again.{RESET}")
            continue

        product_index = int(choice) - 1
        quantity = input(f"{YELLOW}Enter quantity: {RESET}")

        if not quantity.isdigit() or int(quantity) <= 0:
            print(f"{RED}Invalid quantity.{RESET}")
            continue

        shopping_list.append((available[product_index], int(quantity)))

    if shopping_list:
        try:
            total_price = best_buy.order(shopping_list)
            print(f"{GREEN}\nOrder placed successfully! Total cost: ${total_price}{RESET}")
        except Exception as e:
            print(f"{RED}Error during order: {e}{RESET}")
    else:
        print(f"{YELLOW}No products selected.{RESET}")


def quit_program():
    print(f"{CYAN}Thank you for shopping with us! Come again soon!{RESET}")
    exit()


dispatcher = {
    1: list_products,
    2: show_total,
    3: make_order,
    4: quit_program,
}

list_of_commands = [
    "List all products in store",
    "Show total amount in store",
    "Make an order",
    "Quit"
]


def start(store):
    """Main menu loop."""
    while True:
        # Decorative header
        print(f"\n{CYAN}{'=' * 50}")
        print(f"{'🌟 Welcome to Best Buy 🌟':^50}")
        print(f"{'=' * 50}{RESET}")

        # Menu
        for index, message in enumerate(list_of_commands, start=1):
            print(f"{YELLOW}{index}. {message}{RESET}")
        print(f"{CYAN}{'-' * 50}{RESET}")

        choice = input(f"{CYAN}Please choose a number: {RESET}")

        if not choice.isdigit():
            print(f"{RED}Invalid input, please enter a number.{RESET}")
            continue

        choice = int(choice)
        if choice not in dispatcher:
            print(f"{RED}Invalid choice. Please try again.{RESET}")
            continue

        dispatcher[choice]()


if __name__ == "__main__":
    start(best_buy)
