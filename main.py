"""
main.py

This module provides a command-line interface for the Best Buy Store application.
It allows users to view available products, check total stock, and place orders
interactively through a text-based menu system.

Author: Abhisakh
Date: 2025-10-09
"""


import sys
from typing import NoReturn
from datetime import datetime
import products
import store
from products import RED, GREEN, YELLOW, RESET


# Setup inventory
product_list = [
    products.Product("MacBook Air M2", 1450, 100),
    products.Product("Bose QuietComfort Earbuds", 250, 500),
    products.Product("Google Pixel 7", 500, 250),
]
best_buy = store.Store(product_list)


def list_products() -> None:
    """List all active products in the store."""
    print(f"{CYAN}{'_' * 50}{RESET}")
    print(f"\n{CYAN}Available Products:{RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")
    for product in best_buy.get_all_products():
        product.show()


def show_total() -> None:
    """Display total quantity of items in the store."""
    total = best_buy.get_total_quantity()
    print(f"{YELLOW}Total items in store:{RESET} {GREEN}{total}{RESET}")


def print_receipt(order_items: list[tuple], total_price: float) -> None:
    """Display a formatted receipt after a successful order."""
    print(f"\n{CYAN}{'=' * 60}")
    print(f"{'🧾  BEST BUY RECEIPT  🧾':^60}")
    print(f"{'=' * 60}{RESET}")
    print(f"{YELLOW}Date:{RESET} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    print(f"{CYAN}{'Item':<25}{'Qty':<10}{'Price':<10}{'Subtotal':<10}{RESET}")
    print(f"{'-' * 60}")

    for product, quantity in order_items:
        subtotal = product.price * quantity
        print(f"{product.name:<25}{quantity:<10}{product.price:<10.2f}{subtotal:<10.2f}")

    print(f"{'-' * 60}")
    print(f"{GREEN}{'TOTAL:':<45}${total_price:.2f}{RESET}")
    print(f"{CYAN}{'=' * 60}")
    print(f"{'Thank you for shopping with Best Buy! 💙':^60}")
    print(f"{'=' * 60}{RESET}\n")


def make_order() -> None:
    """Allow user to interactively create an order."""
    available = best_buy.get_all_products()
    shopping_list = []

    print(f"\n{CYAN}Available Products:{RESET}")
    for i, product in enumerate(available, start=1):
        print(f"{i}. {product.name} - ${product.price} (Qty: {product.quantity})")

    while True:
        choice = input(f"{YELLOW}\nEnter product number (or 'done' to finish): {RESET}")
        if choice.lower() == 'done':
            break
        if not choice.isdigit() or not 1 <= int(choice) <= len(available):
            print(f"{RED}Product selection should be from the products"
                  f"which are available at our store, try again.{RESET}")
            continue

        product_index = int(choice) - 1
        quantity = input(f"{YELLOW}Enter quantity: {RESET}")

        if not quantity.isdigit() or int(quantity) <= 0:
            print(f"{RED}Invalid quantity.{RESET}")
            continue

        if int(quantity) > available[product_index].quantity:
            print(f"{RED}Only {available[product_index].quantity} items available in stock.{RESET}")
            continue
        # Check if product already in shopping_list — merge quantities
        selected_product = available[product_index]
        quantity_int = int(quantity)

        # Find existing entry
        for i, (p, q) in enumerate(shopping_list):
            if p == selected_product:
                new_total = q + quantity_int
                if new_total > p.quantity:
                    print(f"{RED}You cannot order more than {p.quantity} units in total.{RESET}")
                    break
                shopping_list[i] = (p, new_total)
                print(f"{YELLOW}Updated {p.name} to {new_total} units in your order.{RESET}")
                break
        else:
            # If not found, add new entry
            if quantity_int > selected_product.quantity:
                print(f"{RED}Only {selected_product.quantity} items available in stock.{RESET}")
                continue
            shopping_list.append((selected_product, quantity_int))

    if shopping_list:
        try:
            total_price = best_buy.order(shopping_list)
            print(f"{GREEN}\nOrder placed successfully! Total cost: ${total_price}{RESET}")
            print_receipt(shopping_list, total_price)
        except (ValueError, TypeError) as e:
            print(f"{RED}Error during order: {e}{RESET}")
    else:
        print(f"{YELLOW}No products selected.{RESET}")


def quit_program() -> NoReturn:
    """Exit the program."""
    print(f"{CYAN}Thank you for shopping with us! Come again soon!{RESET}")
    sys.exit(0)


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


def start() -> None:
    """Main menu loop to interact with the store."""
    while True:
        # Decorative header
        print(f"\n{CYAN}{'=' * 50}{RESET}")
        banner_text = " 🛍️✨ 🌟  Welcome to Best Buy  🌟 🛍️✨ "
        print(f"{GREEN}{banner_text:^47}{RESET}")
        print(f"{CYAN}{'=' * 50}{RESET}")

        # Menu display
        for index, message in enumerate(list_of_commands, start=1):
            print(f"{YELLOW}{index}. {message}{RESET}")
        print(f"{CYAN}{'-' * 50}{RESET}")

        choice = input(f"{CYAN}Please choose a number: {RESET}")

        if not choice.isdigit():
            print(f"{RED}Invalid input, please enter a number.{RESET}")
            continue

        choice_int = int(choice)
        if choice_int not in dispatcher:
            print(f"{RED}Invalid choice. Please try again.{RESET}")
            continue

        dispatcher[choice_int]()


if __name__ == "__main__":
    print(f"{GREEN}Starting Best Buy Store CLI...{RESET}")
    start()

