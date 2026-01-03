n = int(input("Enter number of tasks: "))
for i in range(n):
    a = input("Enter task title: ")
    b = input("Enter priority(High/Moderate/Low): ")
    c = input("Enter due date(DD-MM-YYYY): ")
    d = input("Enter status(Completed/Pending): ")
    dict[i+1] = [a,b,c,d] 
print("Task added successfully!")
print("""
      1. Add task
      2. View all tasks
      3. Update task
      4. Delete task
      5. View pending task
      6. View completed task
      7. Search task
      8. Exit
      """)
dict = {}
choice = int(input("Enter your choice: "))
if choice == 1:
    n = int(input("Enter number of tasks: "))
    for i in range(n):
        a = input("Enter task title: ")
        b = input("Enter priority(High/Moderate/Low): ")
        c = input("Enter due date(DD-MM-YYYY): ")
        d = input("Enter status(Completed/Pending): ")
        dict[i+1] = [a,b,c,d] 
    print("Task added successfully!")    
elif choice == 2:
    for key,value in dict.items():
        print(f"ID | Title | Priority | Due date | Status ")
        print(f"{key} | {value[0]} | {value[1]} | {value[2]}")
elif choice == 3:
    key = input("Enter task ID to be updated: ")
    print("""
          1. Change title
          2. Change priority
          3. Change date
          4. Change status
          """)
    option = int(input("Enter your choice: "))
    if option == 1:
        n = int(input("Enter number of tasks: "))
        for i in range(n):
            ID = input("Enter ID: ")
            a = input("Enter task title: ")
            dict[ID][0] = a
            print("Task updated successfully!")
    elif option == 2:
        n = int(input("Enter number of tasks: "))
        for i in range(n):
            ID = input("Enter ID: ")
            a = input("Enter priority: ")
            dict[ID][1] = a
            print("Task updated successfully!")
    elif option == 3:
        n = int(input("Enter number of tasks: "))
        for i in range(n):
            ID = input("Enter ID: ")
            a = input("Enter date: ")
            dict[ID][2] = a
            print("Task updated successfully!")
    elif choice == 4:
        n = int(input("Enter number of tasks: "))
        for i in range(n):
            ID = input("Enter ID: ")
            a = input("Enter status: ")
            dict[ID][3] = a
            print("Task updated successfully!")
    else:
        print("Invalid choice.Please choose right option")
elif choice == 4:
    n = int(input("Enter number of tasks: "))
    for i in range(n):
        task = input("Enter task ID to be deleted: ")
        del dict[task]
        print("Task deleted successfully!")
elif choice == 5:
    list = []
    for i,j in dict.items():
        if dict[i][3] == "Pending":
            list.append(f"{i} | {j[0]} | {j[1]} | {j[2]}")
    print(list +"\n")
elif choice == 6:
    list = []
    for i,j in dict.items():
        if dict[i][3] == "Completed":
            list.append(f"{i} | {j[0]} | {j[1]} | {j[2]}")
            print(list +"\n")
elif choice == 7:
    n = int(input("Enter number of tasks: "))
    a = input("Enter task ID you want to search: ")
    print(dict[a])
elif choice == 8:
    print("Exiting the program.Thank you!!!!")
else:
    print("Invalid choice.Please choose correct option")

        
            
            
            
                
            
    
    
            
        

        
    
    
n = int(input("Enter number of tasks: "))
for i in range(n):
    a = input("Enter task title: ")
    b = input("Enter priority(High/Moderate/Low): ")
    c = input("Enter due date(DD-MM-YYYY): ")
    d = input("Enter status(Completed/Pending): ")
    dict[i+1] = [a,b,c,d] 
print("Task added successfully!")
print("""
      1. Add task
      2. View all tasks
      3. Update task
      4. Delete task
      5. View pending task
      6. View completed task
      7. Search task
      8. Exit
      """)
dict = {}
choice = int(input("Enter your choice: "))
if choice == 1:
    n = int(input("Enter number of tasks: "))
    for i in range(n):
        a = input("Enter task title: ")
        b = input("Enter priority(High/Moderate/Low): ")
        c = input("Enter due date(DD-MM-YYYY): ")
        d = input("Enter status(Completed/Pending): ")
        dict[i+1] = [a,b,c,d] 
    print("Task added successfully!")    
elif choice == 2:
    for key,value in dict.items():
        print(f"ID | Title | Priority | Due date | Status ")
        print(f"{key} | {value[0]} | {value[1]} | {value[2]}")
elif choice == 3:
    key = input("Enter task ID to be updated: ")
    print("""
          1. Change title
          2. Change priority
          3. Change date
          4. Change status
          """)
    option = int(input("Enter your choice: "))
    if option == 1:
        n = int(input("Enter number of tasks: "))
        for i in range(n):
            ID = input("Enter ID: ")
            a = input("Enter task title: ")
            dict[ID][0] = a
            print("Task updated successfully!")
    elif option == 2:
        n = int(input("Enter number of tasks: "))
        for i in range(n):
            ID = input("Enter ID: ")
            a = input("Enter priority: ")
            dict[ID][1] = a
            print("Task updated successfully!")
    elif option == 3:
        n = int(input("Enter number of tasks: "))
        for i in range(n):
            ID = input("Enter ID: ")
            a = input("Enter date: ")
            dict[ID][2] = a
            print("Task updated successfully!")
    elif choice == 4:
        n = int(input("Enter number of tasks: "))
        for i in range(n):
            ID = input("Enter ID: ")
            a = input("Enter status: ")
            dict[ID][3] = a
            print("Task updated successfully!")
    else:
        print("Invalid choice.Please choose right option")
elif choice == 4:
    n = int(input("Enter number of tasks: "))
    for i in range(n):
        task = input("Enter task ID to be deleted: ")
        del dict[task]
        print("Task deleted successfully!")
elif choice == 5:
    list = []
    for i,j in dict.items():
        if dict[i][3] == "Pending":
            list.append(f"{i} | {j[0]} | {j[1]} | {j[2]}")
    print(list +"\n")
elif choice == 6:
    list = []
    for i,j in dict.items():
        if dict[i][3] == "Completed":
            list.append(f"{i} | {j[0]} | {j[1]} | {j[2]}")
            print(list +"\n")
elif choice == 7:
    n = int(input("Enter number of tasks: "))
    a = input("Enter task ID you want to search: ")
    print(dict[a])
elif choice == 8:
    print("Exiting the program.Thank you!!!!")
else:
    print("Invalid choice.Please choose correct option")