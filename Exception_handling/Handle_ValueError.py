#Handle value error.
try:
    num = int(input("Enter a numeber : "))
    print("Your number is : ",num)
except Exception as err:
    print(f"An error occured as {err}")