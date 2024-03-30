age = 0 
while True:
    try:
        age = int(input("How old are you?"))
        if (age > 0):
            break
    except ValueError:
        pass
    print("Please enter a valid age!")

if age < 25:
    print("Sorry you can not rent this car")
else:
    print("Here's your rental car!")