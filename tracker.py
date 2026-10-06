# Expense Tracker - Installment 3: The Tracker Does Math
# Author: Sebastian Paul S. Carlos
# Landing page and two expenses from Installment 2, now with subtotal, tax and budget.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes")
print("=" * 40)

print("\n\tMAIN MENU")
# tabs so the (coming soon) all line up
print("\t1. Add an expense\t(coming soon)")
print("\t2. View all expenses\t(coming soon)")
print("\t3. Show total spent\t(coming soon)")
print("\t4. Exit\t\t\t(coming soon)")

# input() always gives back text, so name and the items stay as strings
print()
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

# subtotal starts at 0 and grows right after each amount is read
subtotal = 0

item1 = input("First expense? ")
# float() turns the typed text into a number
amount1 = float(input("Amount? "))
# += names subtotal only once and adds one amount per statement
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

# average comes from the subtotal, not from re-adding the amounts
average = subtotal / 2

# the user types 12 for 12%, so the program divides by 100 itself
tax_percent = float(input("Tax rate %? "))
# multiply first, then divide, so 12.5 * 12 / 100 gives exactly 1.5
tax = subtotal * tax_percent / 100
total = subtotal + tax

budget = float(input("Your budget? "))
# a comparison gives True or False on its own, no typing it by hand
over_budget = total > budget
# stays negative when the total is over the budget (fixed in Module 3)
left = budget - total

print()
print("-" * 40)
print("SUMMARY")
# the tab puts every value in the same column
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)
print("Made by: Sebastian Paul S. Carlos  |  Installment 3")