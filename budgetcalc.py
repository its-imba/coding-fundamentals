class Budget:
    def __init__(self, category, balance=0):
        self.category = category
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} in {self.category} budget")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds in {self.category} budget")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.category} budget")

    def transfer(self, amount, to_category):
        if self.balance < amount:
            print(f"Insufficient funds in {self.category} budget")
        else:
            self.balance -= amount
            to_category.balance += amount
            print(f"Transferred {amount} from {self.category} budget to {to_category.category} budget")

    def balance_category(self):
        return f"{self.category} balance: {self.balance}"

    def __repr__(self):
        return f"{self.category} budget"


# Example usage:
food_budget = Budget("Food", 100)
clothing_budget = Budget("Clothing", 50)
entertainment_budget = Budget("Entertainment", 25)

# Deposit some money into each budget
food_budget.deposit(50)
clothing_budget.deposit(25)
entertainment_budget.deposit(10)

# Withdraw some money from each budget
food_budget.withdraw(20)
clothing_budget.withdraw(15)
entertainment_budget.withdraw(5)

# Transfer some money between budgets
food_budget.transfer(10, clothing_budget)

# Print out the current balance of each budget
print(food_budget.balance_category())
print(clothing_budget.balance_category())
print(entertainment_budget.balance_category())

# Compute and print out the percentage of total expenses spent on each budget category
total_budget = food_budget.balance + clothing_budget.balance + entertainment_budget.balance
food_percent = (food_budget.balance / total_budget) * 100
clothing_percent = (clothing_budget.balance / total_budget) * 100
entertainment_percent = (entertainment_budget.balance / total_budget) * 100
print(f"Food budget: {food_percent:.2f}% of total expenses")
print(f"Clothing budget: {clothing_percent:.2f}% of total expenses")
print(f"Entertainment budget: {entertainment_percent:.2f}% of total expenses")