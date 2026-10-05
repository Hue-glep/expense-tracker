# Expense Tracker - Installment 2: Talking to the User
# Author: Sebastian Paul S. Carlos
# Landing page from Installment 1, now it asks for a name and two expenses.

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

item1 = input("First expense? ")
# float() turns the typed text into a number, so 4.50 + 8.00 adds up to 12.5
# instead of being treated as text
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

# calculated from what the user typed, nothing hard-coded
total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
# the tab puts every value in the same column
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)
print("Made by: Sebastian Paul S. Carlos  |  Installment 2")