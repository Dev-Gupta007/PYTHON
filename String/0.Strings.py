#           01234
# negetive  54321  
a =        "hello"
b =        "world"
c = a + " " + b
print(f"Hello {b} ")  # f string

print(c)  # concatenation

print(a*3)  # repitition

print("llo" in a) #True
# Indexing
# Forward

print(a[0:4:2])  #[start : end : step value]---->end = exclusive, start = inclusive
                 #[0:0:1] ----> auto taken values

print(a[::3])   #[0:0:3]

print(a[::-1])   #[0:0:-1]----> Backward String

# Backward

print(a[-1:-5:-1])

