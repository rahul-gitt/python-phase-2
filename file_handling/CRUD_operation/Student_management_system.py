'''A simple Student Record Manager built with Python and File Handling. 
This project demonstrates CRUD (Create, Read, Update, Delete) operations using
 text files, along with functions, loops, exception handling, and user interaction.'''

def createstudent():
    name = input("Enter Student name You want to add : ")
    with open("file_handling/CRUD_operation/students.txt","a") as f:
        f.write(name+ "\n")
    print("Student Added successfully..")

def viewstudent():
    with open("file_handling/CRUD_operation/students.txt","r") as f:
        data = f.read()
        if data =="":
            print("No student found..")
        else:
            print(data)

def updatestudent():
    old_name = input("Enter the Name of the student you want to update : ")
    new_name = input("Enter the new name : ")

    try:
        with open("file_handling/CRUD_operation/students.txt","r") as f:
            students = f.readlines()
        with open("file_handling/CRUD_operation/students.txt","w") as f:
            for student in students:
                if(student.strip() != old_name):
                    f.write(student)
                else:
                    f.write(new_name+"\n")
        print("Student updated successfully..")
    except Exception as err:
        print(f"An error occured as {err}")


def deletestudent():
    name = input("Enter the name of the student you want to delete : ")

    try:
        with open("file_handling/CRUD_operation/students.txt","r") as f:
            students = f.readlines()
            with open("file_handling/CRUD_operation/students.txt","w") as f:
                for student in students:
                    if student.strip() != name:
                        f.write(student)

            print("Student Deleted successfully...")
    except Exception as err:
        print(f"An error occured as {err}")
print("\n-------Student Management System-------")
print("1.Add Student")
print("2.View Students")
print("3.Update a Student name")
print("4.Delete a Student name")
print("5.Exit")

while True:
    try:
        choice = int(input("Enter Your choice : "))

        if choice == 1:
            createstudent()
        elif choice == 2:
            viewstudent()
        elif choice == 3:
            updatestudent()
        elif choice == 4:
            deletestudent()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice..")
    except Exception as err:
        print(f"An error occured as {err}")
        