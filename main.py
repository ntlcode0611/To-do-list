
# Todo: Dynamic Menu
# Todo: Create add item 
# Todo: Display items
# Todo: Mark items
 
def Main_menu():
    print("Menu")
    print("1. Add Item")
    print("2. Display Item")
    print("3. Mark Item")
    print("0. Exit")

def view_Menu():
    print("Your To-do-list: ")
    
    for index in range(len(tasklist)):
        print(index + 1, tasklist[index])

def addItem():
    task = input("Add your task:")
    tasklist.append(task)
    file_path = "data.txt"

# Open the file in 'w' (write) mode, which overwrites existing content
    with open(file_path, 'w') as file:
        for task in tasklist:
            file.write(f"{task}\n")

def deleteItem():
    pick_delete = input("Pick the task you want to delete: ")
    tasklist.pop(int(pick_delete)-1)
    file_path = "data.txt"
    with open(file_path, 'w') as file:
        for task in tasklist:
            file.write(f"{task}\n")




def doneItem():
    print("You have done it!")
    input("Press any button to continue: ")



# tasklist = ["1.2", "2.3"]
tasklist = []
with open("data.txt", 'r') as file:
    
    # readlines() returns a list of lines, including the '\n'
    # Use strip() to remove leading/trailing whitespace, including '\n'
    tasklist = [line.strip() for line in file.readlines()]
    
while True:
    Main_menu()
    userinput = input("Please select your choice: ")
#Todo: press 1 for add item, 2 for display item , 3 for mark item, 0 for exit
    if userinput == "0":
        break
    if userinput == "1":
        print("1. Add Item")
        addItem()

        doneItem()


    elif userinput == "2":
        print("2. Display Item")
        view_Menu()
        doneItem()
        
    elif userinput == "3":
        print("3. Mark Item")
        deleteItem()

        doneItem()

#Todo: press 1 for add item, 2 for display item , 3 for mark item, 0 for exit


        




