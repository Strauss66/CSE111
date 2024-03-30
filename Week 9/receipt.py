import csv

def main():
    """
    This fucntion calls read_dictionary and assign it to a variable
    Opens the request file.
    Then uses a loop that reads and processes each row from the request.csv file.
    Within the body of the loop, your program must do the following for each row
    """
    #Index for the product dictionary
    KEY_INDEX = 0
    PRODCUT_NAME_INDEX = 1
    PRICE_INDEX = 2
    #Index for the request dictionary
    QUANTITY_INDEX = 1
    CODE_INDEX = 0   
    products_dict = read_dictionary("./products.csv",KEY_INDEX)

    with open ("./request.csv") as file:
        request_file = csv.reader(file)
        next(request_file)
        print(f"All products: \n {products_dict}")
        print()
    #For every for we are reading a line in the dictionary and the request file
        for line in request_file:
            for key, products in products_dict.items():
    #If the code in the request file is equal to the key in the dictionarty we will print the information.
                if line[CODE_INDEX] == key:
                    print(f"{products[PRODCUT_NAME_INDEX]}: {line[QUANTITY_INDEX]} @ \
{products[PRICE_INDEX]}")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
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