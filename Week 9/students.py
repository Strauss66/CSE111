import re
import csv

def main():
    STUDENT_NAME_INDEX = 1
    student_id = input("Enter your I-Number: ")
    information = read_dictionary("./students.csv")
    found = False
    while found != True:
        for key, info in information.items():
            if student_id == key:
                name = info[STUDENT_NAME_INDEX]
                print(f"Name: {name}")
                found = True
                break
        if not found:
            print("No such student")
            student_id = input("Enter your I-Number: ")
    if not re.match("^[0-9]{1,}$",""):
        print("Inavild I-Number")

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters:
        filename (str): the name of the CSV file to read.
        
    Returns:
        dict: a dictionary that contains the contents of the CSV file.
    """
    STUDENT_ID_INDEX = 0
    student_info = {}
    with open(filename) as students:
        reader = csv.reader(students)
        next(reader)
        for line in reader:
            student_info[line[STUDENT_ID_INDEX]] = line
    return student_info

if __name__ == "__main__":
    main()
