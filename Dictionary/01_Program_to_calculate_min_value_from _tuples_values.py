my_points = {'a':(4,3),'b':(1,2),'c':(5,1)}
highest = [0,0]
init = 0
for i in range(2):
    for j in my_points.keys():
        init = my_points[j][i]
        if init > highest[i]:
            highest[i] = init
print("Highest Value at index 0 in tuple:" , highest[0])
print("Highest Value at index 1 in tuple:" , highest[1])