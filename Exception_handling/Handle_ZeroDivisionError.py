try:
    num = int(input("Enter the number : "))
    print(10/num)
except Exception as err:
    print(f"An error occuurs as {err}")
#if user give 0 then the except part execute
