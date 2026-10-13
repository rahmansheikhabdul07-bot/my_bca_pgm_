# Menu-driven program for a single bank account
# Options: Deposit, Withdraw, Display Account Details, Exit

# Account details
account_holder = input("Enter account holder name: ")
account_number = input("Enter account number: ")
balance = 0.0

# Menu repeats until the user chooses Exit
while True:
    print("\n========== BANK MENU ==========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Account Details")
    print("4. Exit")
    print("===============================")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        # Deposit
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Error: Amount must be greater than zero!")
        else:
            balance = balance + amount
            print("Rs.", amount, "deposited successfully.")

    elif choice == 2:
        # Withdraw
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Error: Amount must be greater than zero!")
        elif amount > balance:
            print("Error: Insufficient balance!")
        else:
            balance = balance - amount
            print("Rs.", amount, "withdrawn successfully.")

    elif choice == 3:
        # Display account details
        print("\n------- ACCOUNT DETAILS -------")
        print("Account Holder  :", account_holder)
        print("Account Number  :", account_number)
        print("Current Balance : Rs.", balance)

    elif choice == 4:
        # Exit
        print("Thank you for using our bank. Goodbye!")
        break

    else:
        print("Error: Invalid choice! Please enter a number between 1 and 4.")