import products
import store


# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = store.Store(product_list)


def list_products():
    """List all active products in the store."""
    print("\nAvailable products:")
    for product in best_buy.get_all_products():
        product.show()


def show_total():
    """Show total quantity of items in the store."""
    total = best_buy.get_total_quantity()
    print(f"\nTotal items in store: {total}")


def make_order():
    """Let user make an order interactively."""
    available = best_buy.get_all_products()
    shopping_list = []

    print("\nAvailable products:")
    for i, product in enumerate(available, start=1):
        print(f"{i}. {product.name} - ${product.price} (Qty: {product.quantity})")

    while True:
        choice = input("\nEnter product number to buy (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(available)):
            print("Invalid selection, try again.")
            continue

        product_index = int(choice) - 1
        quantity = input("Enter quantity: ")

        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid quantity.")
            continue

        shopping_list.append((available[product_index], int(quantity)))

    if shopping_list:
        try:
            total_price = best_buy.order(shopping_list)
            print(f"\nOrder placed successfully! Total cost: ${total_price}")
        except Exception as e:
            print(f"Error during order: {e}")
    else:
        print("No products selected.")


def quit_program():
    """Exit the program."""
    print("Thank you for shopping with us!")
    exit()


# Dispatcher maps menu numbers to functions
dispatcher = {
    1: list_products,
    2: show_total,
    3: make_order,
    4: quit_program,
}


list_of_commands = [
    'List all products in store',
    'Show total amount in store',
    'Make an order',
    'Quit'
]

def start(store):
    """Main menu loop."""
    while True:
        print("\n" + "-" * 30)
        print("       Welcome to Best Buy")
        print("-" * 30)

        # print menu dynamically
        for index, message in enumerate(list_of_commands, start=1):
            print(f"{index}. {message}")
        print("-" * 30)

        choice = input("Please choose a number: ")

        if not choice.isdigit():
            print("Invalid input, please enter a number.")
            continue

        choice = int(choice)
        if choice not in dispatcher:
            print("Invalid choice. Please try again.")
            continue

        # run selected option
        dispatcher[choice]()


if __name__ == "__main__":
    start(best_buy)
