class BankOfAmerica:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= amount
            print(f"Withdrawal successful! New balance: ${self.balance:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Invalid input. Please enter a valid amount.")


class User:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank

    def make_withdrawal(self):
        while True:
            amt = input(f"{self.name}, enter withdrawal amount ($) or 'q' to quit: ")
            if amt.lower() == 'q':
                print("Thank you for using Bank of America!")
                break
            self.bank.withdraw(amt)


name = input("Enter your name: ")
while True:
    try:
        initial_balance = float(input("Enter your initial balance: "))
        if initial_balance < 0:
            raise ValueError("Balance cannot be negative.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid positive amount.")

boa_account = BankOfAmerica(initial_balance)
user = User(name, boa_account)
user.make_withdrawal()