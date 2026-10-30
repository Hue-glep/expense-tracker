# Expense Tracker - Installment 5: The Menu Comes Alive
# Author: Sebastian Paul S. Carlos
# Installment 4 plus a working menu that repeats until the user picks Exit.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes")
print("=" * 40)

# setup is asked once, before the loop, so it never repeats
name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

# 0.0 so the totals print as 170.0 / 0.0 like the expected output
subtotal = 0.0
count = 0
# choice is text on purpose: "7" or "abc" can never crash a comparison
choice = ""

# the loop ends only when the user picks 4
while choice != "4":
    # the menu is written once here and shows again after every choice
    print("\nMAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        # size check lives only here, as an elif chain so one amount gets one message
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")
    elif choice == "3":
        # tax and total are redone each time, since subtotal keeps growing
        tax = subtotal * tax_percent / 100
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total
        # the tab puts every value in the same column
        print(f"  Expenses:\t{count}")
        print(f"  Subtotal:\t${subtotal}")
        print(f"  Tax ({tax_percent}%):\t${tax}")
        print(f"  Grand total:\t${total}")
        if over_budget:
            # left is negative here, so -left is the positive amount over
            print(f"  Over budget by ${-left}!")
        elif total > budget * 0.9:
            print(f"  Careful: only ${left} left.")
        else:
            print(f"  Within budget. ${left} left.")
    elif choice == "4":
        print(f"Goodbye, {name}!")
    else:
        print("  Please choose 1, 2, 3 or 4.")

print("-" * 40)
print("Made by: Sebastian Paul S. Carlos  |  Installment 5")
print("=" * 40)