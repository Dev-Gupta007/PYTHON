# Opening Files 

# <file_objectname > = open(<filename>, <mode>)
# <file_objectname> = open(<file_path>, <mode>)     raw_strings = r"C:\temp\data.txt"

f = open("D:\\DEV\\Programming\\PYTHON\\File_Handling\\sample.txt" , "r")

#-----------------------------------------------------------------------------------------------

# Modes
# Text File     Binary File 
# 'r'           'rb'            read only
# 'w'           'wb'
# 'a'           'ab'
# 'r+'          'r+b' | 'rb+'   
# 'w+'          'w+b' | 'wb+'
# 'a+'          'a+b' | 'ab+'

#-----------------------------------------------------------------------------------------------

file = f.read()

words = file.split()

print(f"Number of Words in Sample.txt {len(L1)}")

#-----------------------------------------------------------------------------------------------

# Closing Files 

# <File_Handle>.close()

f.close()

#-----------------------------------------------------------------------------------------------