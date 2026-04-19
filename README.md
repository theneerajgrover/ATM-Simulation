**#🏦 ATM Simulation System (Python)**

A modular Command-Line ATM Simulation built using Python. This project replicates basic banking operations such as balance inquiry, deposit, withdrawal, and transaction history tracking using a structured multi-file architecture.

**📌 Features :**

💰 Display Balance – Check current account balance

💵 Deposit Money – Add funds with timestamp logging 

💸 Withdraw Money – Withdraw funds with balance validation

📄 Transaction History – View all past transactions

🔁 Menu-Driven Interface – Continuous user interaction loop

🧠 State Management – Shared data using a utility module

**🗂️ Project Structure**

ATM-Simulation/

│

├── main.py               # Entry point (menu-driven system)

├── deposit_money.py      # Deposit functionality

├── withdraw_money.py     # Withdraw functionality

├── display_balance.py    # Balance display

├── statement.py          # Transaction history

├── util.py               # Shared data (balance & history

└── README.md             # Project documentation

**⚙️ How It Works**

The system runs through main.py, which presents a menu.

Based on user input, it calls specific functions from different modules.

All modules interact with a shared file util.py:

balance → stores current account balance

history → stores transaction records

Each transaction (deposit/withdraw) is recorded with a timestamp using datetime.



**▶️ How to Run**

Step 1: Clone the Repository

git clone https://github.com/theneerajgrover/ATM-Simulation.git

cd ATM-Simulation

Step 2: Run the Program

python main.py

**🖥️ Sample Output**

1. Display Balance
   
2. Withdraw Money
 
3. Deposit Money

4. Bank Statement
 
5. Exit


ENTER YOUR CHOICE : 3

ENTER AMOUNT YOU WANT TO DEPOSIT : 500

You have credited 500 Rs in your account...

**🧩 Key Concepts Used
**
**Python Functions & Modular Programming

Conditional Statements (if-elif-else)

Loops (while True)

List Data Structure (for transaction history)

Global State Sharing (via module import)

Date & Time Handling (datetime)
**
**⚠️ Limitations**

No user authentication (PIN/Login not implemented)

Data is not persistent (resets after program ends)

Input validation is basic (no exception handling for invalid types)



**🚀 Future Enhancements**

🔐 Add PIN-based authentication

💾 Implement file/database storage for persistence

🖥️ Build GUI using Tkinter or PyQt

🌐 Convert into Web App (Flask/Django)

📊 Add transaction summaries & analytics


**
📚 Learning Outcome**

This project helps in understanding:

Real-world system simulation

Code modularity and separation of concerns

Handling shared state across multiple files

Building structured CLI applications

**
👨‍💻 Author**

Neeraj Grover

B.Tech Robotics & AI Student

**
⭐ Support**

If you found this project helpful:

Give it a ⭐ on GitHub

Share with others

Use it for learning or improvements

