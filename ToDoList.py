
try:
    dict = {}
    n = int(input("Enter number of tasks: "))
    for i in range(n):
        ID = input("Enter task ID: ")
        a = input("Enter task title: ")
        b = input("Enter task priority(High/Medium/Low): ")
        list = ["High","Medium","Low"]
        while b not in list:
            print("Invalid input.Please enter priority in the mentioned format.")
            b = input("Enter task priority(High/Medium/Low): ")
        else:
            print("Enter due date,")
            c1 = input("Enter year(eg. 2026): ")
            while not (c1.isdigit() and len(c1) == 4):
                print("Invalid input.Enter valid year in the mentioned format.")
                c1 = input("Enter year(eg. 2026): ")
            else:
                c2 = input("Enter month(eg. January): ")
                month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
                while c2 not in month:
                    print("Invalid input.Please enter correct month in the mentioned format.")
                    c2 = input("Enter month(eg. January): ")
                else:
                    c3 = int(input("Enter date(eg. 23): "))
                    days = {"January":32,"February":29,"March":32,"April":31,"May":32,"June":31,"July":32,"August":32,"September":31,"October":32,"November":31,"December":32}
                    while c3 not in range(1,days[c2]):                    
                        print("Invalid input.Please enter correct input.")
                        c3 = int(input("Enter date(eg. 23): "))
                    c = f"{c2} {c3},{c1}"
                    d = input("Enter task status(Completed/Pending): ")
                    status = ["Completed","Pending"]
                    while d not in status:
                        print("Inavalid input.Please enter status in the mentioned format.")
                        d = input("Enter task status(Completed/Pending): ")
                    dict[ID] = [a,b,c,d] 
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
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = int(input("Enter number of tasks: "))
        for i in range(n):
            ID = input("Enter task ID: ")
            a = input("Enter task title: ")
            b = input("Enter task priority(High/Medium/Low): ")
            list = ["High","Medium","Low"]
            while b not in list:
                print("Invalid input.Please enter priority in the mentioned format.")
                b = input("Enter task priority(High/Medium/Low): ")
            else:
                print("Enter due date,")
                c1 = input("Enter year(eg. 2026): ")
                while not (c1.isdigit and len(c1) == 4):
                    print("Invalid input.Enter valid year in the mentioned format.")
                    c1 = input("Enter year(eg. 2026): ")
                else:
                    c2 = input("Enter month(eg. January): ")
                    month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
                    while c2 not in month:
                        print("Invalid input.Please enter correct month in the mentioned format.")
                        c2 = input("Enter month(eg. January): ")
                    else:
                        c3 = int(input("Enter date(eg. 23): "))
                        days = {"January":32,"February":29,"March":32,"April":31,"May":32,"June":31,"July":32,"August":32,"September":31,"October":32,"November":31,"December":32}
                        while c3 not in range(1,days[c3]):                    
                            print("Invalid input.Please enter correct input.")
                            c3 = int(input("Enter date(eg. 23): "))
                        c = f"{c2} {c3},{c1}"
                        d = input("Enter task status(Completed/Pending): ")
                        status = ["Completed","Pending"]
                        while d not in status:
                            print("Inavalid input.Please enter status in the mentioned format.")
                            d = input("Enter task status(Completed/Pending): ")
                        dict[ID] = [a,b,c,d] 
        print("Task added successfully!")
    elif choice == 2:
        for key,value in dict.items():
            print(f"ID | Title | Priority | Due date | Status ")
            print(f"{key} | {value[0]} | {value[1]} | {value[2]}")
    elif choice == 3:
        key = input("Enter task ID to be updated: ")
        if key in dict:
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
                    a = input("Enter priority(High/Medium/Low): ")
                    list = ["High","Medium","Low"]
                    while a not in list:
                        print("Invalid input.Please enter priority in the mentioned format.")
                        a = input("Enter task priority(High/Medium/Low): ")
                    else:
                        dict[ID][1] = a
                print("Task updated successfully!")
            elif option == 3:
                n = int(input("Enter number of tasks: "))
                for i in range(n):
                    ID = input("Enter ID: ")
                    print("Enter due date,")
                    a1 = input("Enter year(eg. 2026): ")
                    while not (a1.isdigit() and len(a1) == 4):
                        print("Invalid input.Enter valid year in the mentioned format.")
                        a1 = input("Enter year(eg. 2026): ")
                    else:
                        a2 = input("Enter month(eg. January): ")
                        month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
                        while a2 not in month:
                            print("Invalid input.Please enter correct month in the mentioned format.")
                            a2 = input("Enter month(eg. January): ")
                        else:
                            a3 = int(input("Enter date(eg. 23): "))
                            days = {"January":32,"February":29,"March":32,"April":31,"May":32,"June":31,"July":32,"August":32,"September":31,"October":32,"November":31,"December":32}
                        while a3 not in range(1,days[a2]):                    
                            print("Invalid input.Please enter correct input.")
                            a3 = int(input("Enter date(eg. 23): "))
                        a = f"{a2} {a3},{a1}"
                        dict[ID][2] = a
                print("Task updated successfully!")
            elif option == 4:
                n = int(input("Enter number of tasks: "))
                for i in range(n):
                    ID = input("Enter ID: ")
                    a = input("Enter status(Completed/Pending): ")
                    status = ["Completed","Pending"]
                    while d not in status:
                        print("Inavalid input.Please enter status in the mentioned format.")
                        d = input("Enter task status(Completed/Pending): ")
                    else:
                        dict[ID][3] = a
                print("Task updated successfully!")
            else:
                print("Invalid choice.Please choose right option")
        else:
            print("ID doesn't exists.Please enter valid ID")
    elif choice == 4:
        n = int(input("Enter number of tasks: "))
        for i in range(n):
            task = input("Enter task ID to be deleted: ")
            keys = list(dict.keys())
            while task not in keys:
                print("Task ID not found.Please enter the valid ID.")
                task = input("Enter task ID to be deleted: ")
            else:
                del dict[task]
        print("Task deleted successfully!")
    elif choice == 5:
        for i,j in dict.items():
            if dict[j][3] == "Pending":
                print(f"{i} | {j[0]} | {j[1]} | {j[2]}")
    elif choice == 6:
        for i,j in dict.items():
            if dict[j][3] == "Completed":
                print(f"{i} | {j[0]} | {j[1]} | {j[2]}")
    elif choice == 7:
        n = int(input("Enter number of tasks: "))
        a = input("Enter task ID you want to search: ")
        for i in dict.keys():
            keys = list(dict.keys())
            while a not in keys:
                print("Task ID not found.Please enter the valid ID.")
                a = input("Enter task ID you want to search: ")
            else:
                print(dict[a])
    elif choice == 8:
        print("Exiting the program.Thank you!!!!")
    else:
        print("Invalid choice.Please choose correct option")
except ValueError as ve:
    print("Invalid input.Please enter integer value.")