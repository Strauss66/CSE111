# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2


def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # Print a blank line.
    print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)

    print()
    count_marriages(marriages_dict, people_dict)
def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print("Ages at death: ")
    for person_id in people_dict.items():
        person = person_id[1]
        age = person[DEATH_YEAR_INDEX] - person[BIRTH_YEAR_INDEX]
        print(f"{person[NAME_INDEX]} {age}")
        print(f"{person[DEATH_YEAR_INDEX]} > {person[BIRTH_YEAR_INDEX]}")


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    count_women = 0
    count_men = 0
    for person_id in people_dict.items():
        person = person_id[1]
        if person[GENDER_INDEX] == "F":
            count_women += 1
        else:
            count_men += 1
    print(f"Number of males {count_men} ")
    print(f"Number of females {count_women}")



def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print("Marriages: ")
    for couple_key, couple_list in marriages_dict.items():
        """
        Getting the wedding year and placing it inside of a variable,
        getiing the key of the husband and wife 
        """
        wedding_year = couple_list[WEDDING_YEAR_INDEX]
        husband_key = couple_list[HUSBAND_KEY_INDEX]
        wife_key = couple_list[WIFE_KEY_INDEX]
        """
        Husband Information
        """
        husband_info = people_dict[husband_key]
        husband_age_married = couple_list[WEDDING_YEAR_INDEX] - husband_info[BIRTH_YEAR_INDEX]
        husband_name = husband_info[NAME_INDEX]
        """
        Wife Information
        """
        wife_info = people_dict[wife_key]
        wife_age = couple_list[WEDDING_YEAR_INDEX] - wife_info[BIRTH_YEAR_INDEX]
        wife_name_married = wife_info[NAME_INDEX]
        print(f"{husband_name} {husband_age_married} > {wedding_year} > {wife_name_married} {wife_age}")
        
def count_marriages(marriages_dict, people_dict):
    marriage_counts = {}  # Dictionary to store the marriage counts for each person

    # Initialize the marriage counts for each person to 0
    for person_key in people_dict:
        marriage_counts[person_key] = 0

    # Count the number of marriages for each person
    for marriage_data in marriages_dict.values():
        husband_code = marriage_data[HUSBAND_KEY_INDEX]
        wife_code = marriage_data[WIFE_KEY_INDEX]

        # Increment the marriage counts for the husband and wife
        marriage_counts[husband_code] += 1
        marriage_counts[wife_code] += 1

    max_marriages = 0
    most_married_person = 0

    # Find the person who married the most times
    for person_key, count in marriage_counts.items():
        if count > max_marriages:
            max_marriages = count
            most_married_person = person_key

    print("Number of Marriages:")
    for person_key, count in marriage_counts.items():
        person_name = people_dict[person_key][NAME_INDEX]
        print(f"{person_name}: {count} marriages")

    most_married_person_name = people_dict[most_married_person][NAME_INDEX]
    print(f"\nThe person who married the most times: {most_married_person_name}")



# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()