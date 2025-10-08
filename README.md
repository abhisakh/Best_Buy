# 🛍️✨ Store Inventory & Ordering System 🛒
<img width="613" height="449" alt="Screenshot 2025-10-08 at 22 33 50" src="https://github.com/user-attachments/assets/42a914a4-a7b4-4c4c-a529-22b7fde627f7" />

Welcome to the **Store Inventory & Ordering System**!  
This Python project simulates a simple store inventory management and ordering system with an interactive command-line interface. 
It’s designed to demonstrate object-oriented programming, exception handling, and user interaction in Python.

---

## Features

- Manage a catalog of products, including names, prices, and quantities.
- Add, remove, and update product stock.
- Track product availability and automatically deactivate sold-out items.
- Interactive CLI menu for:
  - Listing all active products with details.
  - Viewing total quantity of items in stock.
  - Placing orders with multiple products and quantities.
- Colorful terminal output using ANSI escape codes for better readability.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher installed on your system.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/store-inventory-system.git
    cd store-inventory-system
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Run the program:
    ```bash
    python main.py
    ```

---

## Usage

Once running, the program presents a menu:

---

## Project Structure
```bash
.
├── products.py # Product class with validation and purchase logic
├── store.py # Store class managing multiple products and orders
├── main.py # User interface and menu handling
└── README.md # This file
```
---

## Color Output

The terminal output uses ANSI colors for better readability:
```bash
| Color  | Meaning               |
|--------|-----------------------|
| Red    | Errors, warnings      |
| Green  | Success messages      |
| Yellow | User prompts          |
| Cyan   | Headers, separators   |
```
---
## 🙋‍♂️ Author
**Abhisakh Sarma**
GitHub: [https://github.com/abhisakh](https://github.com/abhisakh)
_Contributions and feedback are always welcome!_
# Happy coding and shopping! 🛍️✨
