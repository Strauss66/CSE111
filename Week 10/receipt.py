import csv
from datetime import datetime

current_date_and_time = datetime.now().strftime("%a %b %d %H:%M:%S %Y")

def main():
    KEY_INDEX = 0
    PRODCUT_NAME_INDEX = 1
    PRICE_INDEX = 2
    QUANTITY_INDEX = 1
    CODE_INDEX = 0

    print("Inkom Emporium")
    print()
    try:
        products_dict = read_dictionary("./products.csv", KEY_INDEX)
        subtotal = 0
        quantity = 0
        items = 0
        with open("./request.csv") as file:
            request_file = csv.reader(file)
            next(request_file)
            for line in request_file:
                for key, products in products_dict.items():
                    if line[CODE_INDEX] == key:
                        price = float(products[PRICE_INDEX])
                        if datetime.now().strftime("%A") in ["Tuesday", "Wednesday"]:
                            price *= 0.9  # Apply 10% discount
                        print(f"Product: {products[PRODCUT_NAME_INDEX]} - Quantity: {line[QUANTITY_INDEX]} @ {price:.2f}")
                        items += int(line[QUANTITY_INDEX])
                        quantity = int(line[QUANTITY_INDEX])
                        subtotal += quantity * price
            print()
            print(f"Number of items: {items}")
            print(f"Subtotal: {subtotal:.2f}")
            sales_tax = subtotal * 0.06
            print(f"Sales tax: {sales_tax:.2f}")
            total = sales_tax + subtotal
            print(f"Total: {total:.2f}")
            print()
            print("Thank you for shopping at the Inkom Emporium.")
            print(current_date_and_time)
    except FileNotFoundError as file_error:
        print(f"File not found error: {file_error}")
    except PermissionError as permission_error:
        print(f"Permission error: {permission_error}")
    except KeyError as key_error:
        print(f"Key error: {key_error}")

def read_dictionary(filename, key_column_index):
    products_dict = {}
    with open(filename) as file:
        products = csv.reader(file)
        next(products)
        for line in products:
            if len(line) != 0:
                key = line[key_column_index]
                products_dict[key] = line
    return products_dict

if __name__ == "__main__":
    main()