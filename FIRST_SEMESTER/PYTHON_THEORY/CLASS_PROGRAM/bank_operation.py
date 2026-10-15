
# Bank operations using tuples inside a list
# Tuple format: (name, acc_no, pan, dob, email, contact, address, balance)

accounts = []

n = int(input("Enter number of bank accounts: "))

for i in range(n):
    print(f"\n--- Enter details for account {i + 1} ---")
    name    = input("Name: ")
    acc_no  = input("Account No: ")
    pan     = input("PAN Card: ")
    dob     = input("D-O-B (dd/mm/yyyy): ")
    email   = input("Email ID: ")
    contact = input("Contact Number: ")
    address = input("Address (place name only): ")
    balance = float(input("Current Balance: "))
    accounts.append((name, acc_no, pan, dob, email, contact, address, balance))


def find_account(acc_no):
    """Return index of the account in the list, or -1 if not found."""
    for index, acc in enumerate(accounts):
        if acc[1] == acc_no:
            return index
    return -1


while True:
    print("\n-----------bank----------")
    print("1. deposit   2. withdraw   3. check account   4. exit")
    choice = input("enter your choice: ")

    if choice == "4":
        print("Thank you for banking with us!")
        break

    if choice not in ("1", "2", "3"):
        print("Invalid choice, try again.")
        continue

    acc_no = input("Enter account number: ")
    idx = find_account(acc_no)

    if idx == -1:
        print("Account not found!")
        continue

    name, acc_no, pan, dob, email, contact, address, balance = accounts[idx]

    if choice == "1":                       # deposit
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount!")
        else:
            balance += amount
            accounts[idx] = (name, acc_no, pan, dob, email, contact, address, balance)  # new tuple
            print(f"Deposited {amount}. New balance: {balance}")

    elif choice == "2":                     # withdraw
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            accounts[idx] = (name, acc_no, pan, dob, email, contact, address, balance)  # new tuple
            print(f"Withdrawn {amount}. New balance: {balance}")

    elif choice == "3":                     # check account
        print("\n------ Account Details ------")
        print("Name           :", name)
        print("Account No     :", acc_no)
        print("PAN Card       :", pan)
        print("D-O-B          :", dob)
        print("Email ID       :", email)
        print("Contact Number :", contact)
        print("Address        :", address)
        print("Current Balance:", balance)




