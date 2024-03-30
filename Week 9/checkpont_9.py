def main():
    provinces = read_txt_list("./provinces.txt")

    print(provinces)
    provinces.pop(0)
    provinces.pop()

    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"
    alberta_count =  provinces.count("Alberta")
    print(provinces)
    print(f"Number of 'Alberta' elements: '{alberta_count}' ")

def read_txt_list(file_to_read):
    provinces = []
    with open(file_to_read, "rt") as file:
        for line in file:
            provinces.append(line.strip())

    return provinces

if __name__ == "__main__":
    main()