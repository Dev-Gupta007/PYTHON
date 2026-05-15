Name = input("Enter the name of your file (Ex. Notes.txt):  ")

print("""1.Read Notes \n 2.Write Notes \n 3.Exit""")

Choice = int(input("Enter your choice: "))

while Choice != 3:
        if Choice == 1:
                try:
                        Note = open(Name , 'r' )
                        str = " "
                        while str:
                                str = Note.readline()
                                print(str , end = '\n')
                        Note.close()
                        Choice = int(input("Enter your choice: "))
                except:
                        FileNotFoundError
                        Note = open(Name , 'w+')
                        str = " "
                        while str:
                                str = Note.readline()
                                print(str , end = '\n')
                        Note.close()
                        Choice = int(input("Enter your choice: "))
        elif Choice == 2:
                Note  = open(Name , 'w')
                Note1 = input("Enter the Note: ")
                Note.write(Note1)
                Note.close()
                Choice = int(input("Enter your choice: "))
        else:
                print("Invalid Input")
                Choice = int(input("Enter your choice: "))

print("Thank You for using our App")