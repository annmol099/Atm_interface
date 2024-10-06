class Atm:

    def __init__(self):
        
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input(''' 
                          Hello, how can I help you?

                          1. Enter 1 to create_pin
                          2. Enter 2 to deposit
                          3. Enter 3 to withdraw
                          4. Enter 4 to check balance
                          5. Enter 5 to exit
            ''')
            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print('Thanks for using the ATM. Goodbye!')
                break
            else:
                print('Invalid input, please try again.')

    def create_pin(self):
        self.pin = input('Enter a new PIN: ')
        print('PIN set successfully.')

    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = float(input('Enter the amount to deposit: '))
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid PIN.")

    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = float(input('Enter the amount to withdraw: '))
            if amount <= self.balance:
                self.balance -= amount
                print('Withdrawal successful.')
            else:
                print("Insufficient balance.")
        else:
            print("Invalid PIN.")

    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            print(f'Your balance is: ${self.balance:.2f}')
        else:
            print("Invalid PIN.")

# To run the ATM
if __name__ == "__main__":
    Atm()
