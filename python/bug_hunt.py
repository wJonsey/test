# Lakeside Leisure ticket calculator
# Under 5: free | 5 to 15: £6.50 | 65 and over: £7.00
# Student: £8.00 | Adult: £12.00 | Groups of 10 or more: 10% off
# Valid ages are 0 to 120. Show the total to 2 decimal places.
#
# TASK 2 PRACTICE: this program has 8 errors.
# 1. Write a test plan with EXPECTED results before running anything.
# 2. Run, find, fix and log each error: line, type (syntax/runtime/logic), fix, retest.
# Answers are in the "Bug hunt" section of your 14-day plan page. Don't peek early.

def get_age():
    age = input("Enter age: ")
    while not age.isdigit() or int(age) > 119:
        age = input("Invalid age. Enter 0 to 120: ")
    return int(age)

def ticket_price(age, student):
    if age < 5:
        return 0
    elif age <= 16:
        return 6.50
    elif age >= 65:
        return 7.00
    elif student == "y":
        return 8.00
    else:
        return 12.00

age = get_age()
student = input("Student? (y/n): ").upper()
quantity = input("How many tickets? ")
price = ticket_price(age, student)
total = price * quantity
if quantity > 10:
    total = total * 0.1
print("Total to pay: £", total)
