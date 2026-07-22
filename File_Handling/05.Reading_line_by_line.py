f = open("D:\\DEV\\Programming\\PYTHON\\File_Handling\\sample.txt" , "r")
str = " "

while str:
    str = f.readline()
    print(str , end = " ")

f.close()