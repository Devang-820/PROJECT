
print("*" * 30)
print("WELCOME")
print("MAKE A 4-DIGIT PIN FOR ACCESSING THE BANK MENU")
print("*" * 30)

# PIN creation
while True:
    pin = input("Make a PIN of 4 digits: ")

    if len(pin) == 4 and pin.isdigit():
        print("PIN created successfully!")
        break
    else:
        print("Invalid PIN! Please enter exactly 4 digits.")


# Account login
attempts = 0
max_attempts = 3
account_num = "5"
access_granted = False

while attempts < max_attempts:

    entered_account_num = input("Enter your account number: ")
    entered_pin = input("Enter your PIN: ")

    if entered_account_num == account_num and entered_pin == pin:
        print("Login successful!")
        access_granted = True
        break

    else:
        attempts += 1
        print("Incorrect account number or PIN!")
        print(f"Attempts remaining: {max_attempts - attempts}")


# Banking functions
balance = 0
transactions = []


def show_balance():
    print(f"Your balance is ${balance:.2f}")


def deposit():
    try:
     deposit_money = float(input("Enter the deposit amount: "))
    except ValueError:
        print("Please enter a valid number!")
        return 0
    if deposit_money <= 0:
        print("That is not a valid amount.")
        return 0

    return deposit_money


def withdraw():
    try:
     withdraw_money = float(input("Enter the withdrawal amount: "))
    except ValueError:
     print("Please enter a valid number!")
     return 0
    if withdraw_money <= 0:
        print("That is not a valid amount.")
        return 0

    elif withdraw_money > balance:
        print("Insufficient balance in account.")
        return 0

    return withdraw_money


# Banking menu
if access_granted:

    print("\nWelcome to your banking menu!")

    is_running = True

    while is_running:

        print("\n" + "*" * 30)
        print("BANKING PROGRAM")
        print("*" * 30)

        print("1: Show Balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Transaction History")
        print("5: Exit")
        print("*" * 30)
        choice = input("Enter your choice (1-5): ")
        print("*" * 30)
        if choice == '1':
            show_balance()

        elif choice == '2':
            amount = deposit()
            balance += amount

            if amount > 0:
                transactions.append(f"Deposited: ${amount:.2f}")

        elif choice == '3':
            amount = withdraw()
            balance -= amount

            if amount > 0:
                transactions.append(f"Withdrawn: ${amount:.2f}")

        elif choice == '4':
            print("\nTransaction History:")

            if not transactions:
                print("No transactions yet.")

            for transaction in transactions:
                print(transaction)

        elif choice == '5':
            is_running = False

        else:
            print("That is not a valid choice.")

else:
    print("Too many incorrect attempts. Access denied.")

print("*" * 30)
print("\nThank you for banking with us!")
