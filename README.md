# 🛍️✨ Best Buy — Store Inventory & Ordering System 🛒

<img width="960" height="610" alt="Store Screenshot" src="https://github.com/user-attachments/assets/96012db0-0b05-4ba9-992e-2a7e650f7da8" />

Welcome to the **Best Buy Store Inventory & Ordering System**!  
This Python project simulates a **store management system** that allows you to browse products, manage stock, and place orders — all through a colorful, interactive **command-line interface**.  

> 🚀 This project demonstrates clean **Object-Oriented Programming (OOP)** principles, strong **error handling**, and an intuitive **user experience** in Python.

---

## 🌟 Features

✅ Manage a catalog of products — name, price, quantity, and active status.  
✅ Add, remove, and update products dynamically.  
✅ Automatic deactivation of out-of-stock products.  
✅ Interactive CLI menu for:
  - 🧾 Listing all active products.
  - 📦 Viewing total quantity in stock.
  - 🛒 Placing multi-item orders.
✅ Generates a **receipt summary** after every order.  
✅ Eye-friendly, colorful output using **ANSI color codes**.  

<img width="524" height="317" alt="CLI Screenshot" src="https://github.com/user-attachments/assets/45e0f1b3-fb4f-4530-9969-158325e2189f" />

---

## 🧰 Tech Stack

| Component | Description |
|------------|-------------|
| **Language** | Python 3.7+ |
| **Paradigm** | Object-Oriented Programming |
| **Interface** | Command-Line (CLI) |
| **Formatting** | ANSI Escape Colors |
| **Style Guide** | PEP8 Compliant |

---

## ⚙️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/abhisakh/Best_Buy.git
cd Best_Buy
```
### 2️⃣ (Optional) Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # For macOS/Linux
.venv\Scripts\activate      # For Windows
```
### 3️⃣ Install Dependencies (if any)
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the Program
```bash
python main.py
```
---

### 🖥️ Usage
When you run the application, you’ll see a welcoming menu:
```bash
==================================================
       🛒💫🌟  Welcome to Best Buy  🌟💫🛒
==================================================
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
--------------------------------------------------
```
👉 Choose an option by typing the corresponding number.
👉 While ordering, you can select multiple products and quantities.
👉 A receipt will be displayed after successful checkout.

---

### Project Structure
```bash
.
├── main.py         # CLI user interface and menu handling
├── store.py        # Store class - manages multiple products and orders
├── products.py     # Product class - validation, activation, purchase logic
├── requirements.txt# Python dependencies
├── LICENSE         # License file
└── README.md       # Project documentation

```
---

## 🎨 Color Codes in Terminal

The terminal output uses ANSI colors for better readability:
```bash
| Color         | Meaning              |
| ------------- | -------------------- |
| 🟥 **Red**    | Errors & warnings    |
| 🟩 **Green**  | Success messages     |
| 🟨 **Yellow** | User prompts         |
| 🟦 **Cyan**   | Headers & separators |
```
---

### 🧾 Example Receipt

```bash
----------------------------------------
           🧾 Best Buy Receipt
----------------------------------------
Google Pixel 7      x2  →  $1000.00
MacBook Air M2      x1  →  $1450.00
----------------------------------------
TOTAL:                     $2450.00
Thank you for shopping with us! 💙
----------------------------------------

```

## 🙋‍♂️ Author
**Abhisakh Sarma**
GitHub: [https://github.com/abhisakh](https://github.com/abhisakh)
_Contributions and feedback are always welcome!_
# Happy coding and shopping! 🛍️✨
