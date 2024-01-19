# Lili Stevenson and Sierra Philbin
# 1/10/2024
# Mr Jaramillo
# 3rd Period
# To-Do List

# Initialize
print("Welcome to List Tracker Program.")
groceryList = ["bread", "milk", "eggs","pasta","carrots"]

# Functions
def list():
    print("Please choose an option: (Type in a number between 1-5)")
    print("1. Add a task to the to-do list \n2. View the current to-do list \n3. Mark a task as completed \n4. Remove a task from the to-do list \n5. Exit the program")
    option = int(input("Option: "))
    if option == 1:
        # Adds whatever item the user inputs to the end of the list and prints the list
        addTask = input("What item would you like to add to the grocery list?: ")
        groceryList.append(addTask)
        print(groceryList)
    elif option == 2:
        # Prints the list
        print(groceryList)
    elif option == 3:
        # Adds an x in front of the items the user chooses
        groceryList = ["bread", "milk", "eggs","pasta","carrots"]
        ans = input("What item on the list would you like to check off?")
        i = groceryList.index (ans)
        groceryList[i] = ans + " X"
        print(groceryList)
    elif option == 4:
        # Removes the item the user chooses from the list
        remove = int(input("Which item from the list would you like to remove(choose the number of the item starting from 0)?: "))
        groceryList.pop(remove)
        print(groceryList)
    elif option == 5:
        # Removes all of the items in the list
        groceryList.clear()
        print(groceryList)
    elif option == 6:
        # Sorts the list of items alphabetically
        groceryList.sort()
        print(groceryList)
    elif option == 7:
        # Prints the total number of items in the list
        print(len(list))
    elif option == 8:
        # Quits the program
        print("Thank you for using List Tracker. List will now shut down.")
        quit()
    list()


# Main
list()
