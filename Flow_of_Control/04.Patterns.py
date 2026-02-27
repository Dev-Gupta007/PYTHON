# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4

# for i in range(1 , 6):
#     for j in range(1 , i):
#         print(j , end = ' ')
#     print()


# # 1
# # 1 3
# # 1 3 5
# # 1 3 5 7

# for i in range(1 , 10 , 2):
#     for j in range(1 , i , 2):
#         print(j , end = ' ')
#     print()
# print()

# #    *
# #   * *
# #  * * *
# #   * *
# #    *

# n = 3  # number of stars in the middle row

# # Upper part (including middle row)
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")      # Print spaces
#     for k in range(i):
#         print("* ", end="")     # Print stars     
#     print()

# # Lower part
# for i in range(n - 1, 0, -1):
#     for j in range(n - i):  # Print spaces
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="") # Print stars
        
#     print()

# print()

# # *
# # * *
# # * * *
# # * *
# # *

# n = 3  # number of stars in the middle row

# # Top half including middle row
# for i in range(1 , n+1):
#     for j in range(1 , i+1):
#         print("*" , end = " ")
#     print()

# # Bottom half
# for i in range(n-1 , 1 , -1):
#     for j in range(i):
#         print("*" , end = " ")
#     print()
# print()

# #   *
# #  * *
# # *   *
# #  * *
# #   *

# n = 3  # middle row

# # Top half including middle
# for i in range(1, n + 1):
#     if i == 1:
#         print(" " * (n - i) + "*")
#     else:
#         front_spaces = " " * (n - i)
#         mid_spaces = " " * (2 * i - 3)
#         print(front_spaces + "*" + mid_spaces + "*")

# # Bottom half
# for i in range(n - 1, 0, -1):
#     if i == 1:
#         print(" " * (n - i) + "*")
#     else:
#         front_spaces = " " * (n - i)
#         mid_spaces = " " * (2 * i - 3)
#         print(front_spaces + "*" + mid_spaces + "*")




# # A
# # A B
# # A B C
# # A B C D
# # A B C D E
# # A B C D E F

# n = 6  # number of rows

# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(65 + j), end=" ") # chr(65) is 'A', chr(66) is 'B', etc.
#     print()  

#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4 
# 5 4 3 2 1 2 3 4 5 

spaces = 8

for i in range(1 , 6):
    print(" "*spaces , end = '')
    for j in range(i , 0 , -1):
        print(j , end = ' ')
    for k in range(2 , i+1):
        print(k , end = ' ')
    spaces = spaces-2
    print()
print()
