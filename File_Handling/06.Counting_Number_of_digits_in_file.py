f = open("D:\\DEV\\Programming\\PYTHON\\File_Handling\\sample.txt" , "r")

count = 0

for i in f.read():
    if i.isdigit() == True:
        count += 1

print("Number of Integers: " , count)