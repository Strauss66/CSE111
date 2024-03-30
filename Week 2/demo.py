from datetime import datetime 
print("--------------------------------------")
timestamp = datetime.now()

with open("logs.txt","a") as file:
    file.write(f"{timestamp}\n")