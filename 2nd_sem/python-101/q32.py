# Q32: Create a parent class Bonus with instance variables sales_id and sales_amount.
# Add get_bonus method that calculates a salesperson’s bonus using the formula bonus = sales * 0.05.
# Create a child class named PremiumBonus from Bonus. The child class’s get_premium_bonus() method should calculate the bonus using the formula bonus = sales * 0.05 + (sales – 2500) * 0.01.
# Now, create an object of PremiumBonus class and use this object to find both bonus and premium bonus.

class Bonus:
    def __init__(self, sales_id, sales_amount):
        self.sales_id = sales_id
        self.sales_amount = sales_amount

    def get_bonus(self):
        return self.sales_amount * 0.05

class PremiumBonus(Bonus):
    def get_premium_bonus(self):
        return self.sales_amount * 0.05 + max(0, self.sales_amount - 2500) * 0.01

sales_id = input("Enter sales ID: ")
sales_amount = float(input("Enter sales amount: "))
pb = PremiumBonus(sales_id, sales_amount)
print("Bonus:", pb.get_bonus())
print("Premium Bonus:", pb.get_premium_bonus())
