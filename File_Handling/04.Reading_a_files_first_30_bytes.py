f = open(r"D:\DEV\Programming\PYTHON\File_Handling\sample.txt" , "r")

string1 = f.read(30)
string2 = f.read(30)    # Reads the next 30 bytes

print(string1)
print(string2)  

f.close()