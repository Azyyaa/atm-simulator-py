#
# def pause():
#     input("\nPress Enter to continue...")
# def clear():
#     print("\n" * 100)
def check_pin(pin_attempts=3):
    while pin_attempts>0:
        pin_input = input("Enter PIN: ")
        with open("pin.txt", "r") as file:
            correct_pin=file.readline().strip()
        if pin_input==correct_pin:
            return True
        else:
            pin_attempts-=1
            print("Incorrect PIN. Remaining attempts:", pin_attempts)
    print("Your card has been blocked.")
    exit()

def change_pin():
    pin_attempts=3
    while pin_attempts>0:
        if check_pin(pin_attempts):
            new_pin=input("Enter your PIN (4 digits): ")
            if len(new_pin)!=4 or not new_pin.isdigit():
                print("PIN must contain 4 digits.")
                return
            with open("pin.txt", "w") as file:
                file.write(new_pin)
            print("PIN successfully changed.")
            break
        else:
            pin_attempts-=1
    else:
        print("Your card has been blocked due to multiple incorrect PIN attempts.")
        exit()

def deposit():
    if check_pin():
        amount=float(input("Enter the amount to deposit: "))
        if amount<=0:
            print("Amount must be positive. ")
            return
        with open("balance.txt", "r+") as file:
            balance=float(file.readline())
            balance+=amount
            file.seek(0)
            file.write(str(balance))
        print("Deposit successful.")

def withdraw():
    if check_pin():
        with open("balance.txt", "r+") as file:
            balance = float(file.readline())
            amount = float(input("Enter the amount to withdraw: "))
            if amount<=0:
                print("Amount must be positive. ")
                return
            if amount>balance:
                print("Insufficient funds. ")
                return
            file.seek(0)
            file.write(str(balance - amount))
        print("Withdrawal successful.")

def check_balance():
    if check_pin():
        with open("balance.txt", "r") as file:
            balance = float(file.readline())
        print("Balance: ", balance)


def main_menu():
    while True:
        print("Menu:")
        print("1. Change PIN")
        print("2. Deposit funds")
        print("3. Withdraw funds")
        print("4. Check balance")
        choice = input("Select an option (1-4):")
        if choice=='1':
            change_pin()
        elif choice=='2':
            deposit()
        elif choice=='3':
            withdraw()
        elif choice=='4':
            check_balance()
        else:
            print("Invalid input. Please try again.")

try:
    with open("pin.txt", "x") as file:
        pin = input("Enter your PIN (4 digits1): ")
        if len(pin)!=4 or not pin.isdigit():
            print("PIN must contain 4 digits.")
            exit()
        file.write(pin)
except FileExistsError:
    pass

try:
    with open("balance.txt", "x") as file:
        file.write("15000.0")
except FileExistsError:
    pass

main_menu()