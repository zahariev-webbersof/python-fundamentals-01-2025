### **🌟 Bank Account Management System 🌟**

![12291285_Startup-managers-presenting-and-analyzing-sales-growth-chart-1024x683](https://github.com/user-attachments/assets/e0329bcc-619e-4cc0-8ae8-e09d5e32da3d)

#### **🎯 Learning Goals**
1. **Understand Core Programming Concepts**: Functions, loops, conditional statements, and lists.
2. **Work with Python for Real-Life Applications**: Simulate a bank management system with real-world features.
3. **Learn Modular Programming**: Design reusable and well-structured code.
4. **Enhance Debugging Skills**: Test each function using various edge cases.
5. **Version Control and Collaboration**: Use GitHub for submission, version tracking, and feedback.
6. **Critical Thinking**: Implement a credit card type checker and integrate it with other features.

---

### **📁 Project Structure**

```plaintext
EnhancedBankSystem/
├── main.py                # Main program file
├── README.md              # Project documentation
├── test/                  # Folder for testing scripts
│   ├── test_main.py       # Unit tests for all functions
├── submission/            # Folder where students push GitHub URLs
│   ├── student1.txt       # URL of Student 1's GitHub repository
│   ├── student2.txt       # URL of Student 2's GitHub repository
└── .gitignore             # File to exclude unnecessary files from Git tracking
```

---

### **📜 Step-by-Step Instructions**

#### **1️⃣ Tasks and Features**
1. **Create a Bank Account**
   - Prompt user for account name.
   - Add account with `0` balance and initialize a loan amount to `0`.

2. **Deposit Money**
   - Verify the account exists.
   - Update the balance and log the transaction.

3. **Withdraw Money**
   - Ensure sufficient balance exists for the withdrawal.
   - Update the balance and log the transaction.

4. **Check Balance**
   - Display the account's current balance.

5. **List All Accounts**
   - List account holders with their balance and loan details.

6. **Transfer Funds**
   - Allow money transfers between accounts if sufficient balance exists.

7. **Transaction History**
   - View all past transactions for an account.

8. **Apply for a Loan**
   - Allow loan applications up to `MAX_LOAN_AMOUNT` and calculate interest.

9. **Repay a Loan**
   - Deduct loan amounts from balance upon repayment.

10. **Identify Credit Card Type**
    - Check if the card is Visa, Mastercard, or another type based on number prefixes.

11. **Exit the System**
    - Terminate the program gracefully.

---

#### **2️⃣ Credit Card Type Identification 💳**

Add a new functionality to identify credit card types based on the card number.
Rules for identifying credit card types:

Visa: Card number starts with 4 (e.g., 4123...).
MasterCard: Card number starts with numbers between 51 and 55 (e.g., 5123...).
American Express: Card number starts with 34 or 37 (e.g., 3712...).
Other: If the card number doesn’t match the above patterns.
📌 Implementation Steps:

Create a new function: identify_card_type().
Prompt the user to input their card number.
Use if and elif conditions to check the card prefix.
Print the card type to the user.

---
#### **3️⃣ Python Code Skeleton**

```python
# Enhanced Bank Account Management System

# 🏦 Data Structures to Store Information
account_holders = []  # Account names
balances = []         # Account balances
transaction_histories = []  # Account transaction logs
loans = []            # Account loan details

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03

def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")

def create_account():
    """Create a new account."""
    pass  # TODO: Add logic

def deposit():
    """Deposit money into an account."""
    pass  # TODO: Add logic

def withdraw():
    """Withdraw money from an account."""
    pass  # TODO: Add logic

def check_balance():
    """Check balance of an account."""
    pass  # TODO: Add logic

def list_accounts():
    """List all account holders and details."""
    pass  # TODO: Add logic

def transfer_funds():
    """Transfer funds between two accounts."""
    pass  # TODO: Add logic

def view_transaction_history():
    """View transactions for an account."""
    pass  # TODO: Add logic

def apply_for_loan():
    """Allow user to apply for a loan."""
    pass  # TODO: Add logic

def repay_loan():
    """Allow user to repay a loan."""
    pass  # TODO: Add logic

def identify_card_type():
    """Identify type of credit card."""
    pass  # TODO: Add logic

def main():
    """Run the banking system."""
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        # Map choices to functions
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            identify_card_type()
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
```

---

#### **3️⃣ Testing 🧪🧪🧪**

Test the system with multiple scenarios:
Create accounts and perform various transactions.
Use valid and invalid credit card numbers to test the card type identification.
Validate the error messages for incorrect inputs (e.g., negative deposits, invalid card numbers).

---

#### **4️⃣ Submission Process**

### **📱 Steps to Submit Your Code Using GitHub Mobile**



**Create a GitHub Repository ✅**  
- Open the **GitHub Mobile App** on your phone.  
- Tap the **+** icon (usually in the top-right corner).  
- Select **"Create Repository"**.  
- Name your repository: `EnhancedBankSystem`.  
- Optionally, add a description:  
  `"Enhanced Bank Account Management System with Loan Feature"`.  
- Choose **Public** or **Private** visibility based on your preference.  
- Tap **Create Repository**. 🎉


**Upload Your Code to the Repository ✅**  
- Navigate to your **project files** on your mobile device, where you’ve saved your Python code (e.g., using a file manager app).  
- **Open the GitHub Mobile App**.  
- Go to the repository you just created (`EnhancedBankSystem`).  
- Tap the **+** button to **add a new file**.  
- Choose the files to upload:  
  - Tap **"Add files"** and select all relevant project files (Python files, any additional text or resource files you’ve created).  
- Once you’ve selected the files, tap **"Commit changes"**.  
- **Commit message**: `"Initial commit with skeleton code"`. 📝  
- Tap **Commit Changes** to finalize. 🔄



**Add a Submission Link in a Text File ✅**  
- **Open the GitHub Mobile App**.  
- In the **EnhancedBankSystem repository**, create a new text file named `submission.txt`.  
- In the **submission.txt** file, add the following:  
  - A link to your GitHub repository:  
    `https://github.com/username/EnhancedBankSystem`  
  - Any additional details you want to add for submission.  
- **Commit message**: `"Added GitHub repository link in submission.txt"`. 📝  
- Tap **Commit Changes** to save. 📤


**Push Your Code to GitHub ✅**  
- Once you've added your code and the `submission.txt` file:  
  - Tap the **"Commit changes"** button in the GitHub Mobile App to commit the files to your repository.  
- Your changes will be automatically pushed to the **main branch** of the repository. 🔝


**Verify Your Submission ✅**  
- Open the repository in your web browser or within the GitHub Mobile App.  
- Check if all the project files, including the `submission.txt` file with your GitHub link, are present and correctly uploaded. ✔️


**Submit the Link ✅**  
- Ensure that your **submission.txt** file contains the link to your repository.  
- Your submission is complete when all the project files are uploaded and the link is added in the **submission.txt** file. 🎉

--- 

🎉 Congratulations on Completing the Project! 🎉
You’ve successfully built an Enhanced Bank Account Management System! 🎉 Your hard work has paid off, and you’ve not only created a useful real-world application but also gained valuable experience in Python programming, GitHub usage, and collaborative software development. 🚀

Keep up the great work! 💪
