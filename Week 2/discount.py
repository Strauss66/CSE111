from datetime import datetime
subtotal = float(input("Please enter your subtotal: "))
current_date = datetime.now()
weekday = current_date.weekday()
if subtotal >= 50 and (weekday == 2 or weekday == 1):
    discout = round(subtotal * 0.10,2)
    print(f"Discount is: {discout}")
    subtotal -= discout
tax = round(subtotal * .06,2)
print(f"Sales tax amount: {tax:.2f}")

total = round(subtotal + tax,2)
print (f"The total is: {total}")