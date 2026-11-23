students={}
def add_student():
    roll=input("Enter Roll no:")
    name=input("Enter Name:")
    dept=input("Enter Department")
    students[roll]={"name":name,"department":dept}
    print("student added successfully")
def view_student():
    if not students:
        print("no student records found")
        return
    print("\n--student records--")
    for roll,data in students.items():
        print("roll no:",roll,
        "|name:",data["name"],
        "|department:",data["department"])
def search_student():
    roll=input("enter roll no to search:")
    if roll in students:
        print(students[roll])
    else:
        print("students not found")
def delete_student():
    roll=input("enter roll no to delete")
    if roll in students:
        del students[roll]
        print("students deleted successfully")
    else:
        print("student not found")
while True:
    print("\n1.Add student")
    print("2.view students")
    print("3.search student")
    print("4.delete student")
    print("5.exit")
    choice=input("enter ypur choice")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_student()
    elif choice=="3":
        search_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        print("exiting...")
        break
    else:
        print("invalid choice")