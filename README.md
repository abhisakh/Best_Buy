# 🛍️✨ Store Inventory & Ordering System 🛒
<img width="960" height="610" alt="Screenshot 2025-10-09 at 09 33 44" src="https://github.com/user-attachments/assets/96012db0-0b05-4ba9-992e-2a7e650f7da8" />

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
- Receipt generation.
- <img width="524" height="317" alt="Screenshot 2025-10-09 at 09 58 38" src="https://github.com/user-attachments/assets/45e0f1b3-fb4f-4530-9969-158325e2189f" />


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
