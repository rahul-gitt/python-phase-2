try:
    age = int(input("Enter Your age : "))
    if age <10 or age>18:
        raise ValueError("Age must be between 10 and 18")
    else:
        print("Welcome to the club.")
except Exception as err:
    print(f"An error occurs as {err}")
print("Club will start soon")