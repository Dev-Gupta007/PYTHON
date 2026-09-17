# Question:

# A list containing records of products is given as:

# L = [("Laptop", 90000), ("Mobile", 30000), ("Pen", 50), ("Headphones", 1500)]

# Write the following user-defined functions to perform operations on a stack named Product:

# (i) Push_element() – To push an item containing the product name and 
# price of products costing more than 50 into the stack.

# (ii) Pop_element() – To pop the items from the stack and display them. 
# Also, display "Stack Empty" when there are no elements in the stack.

L = [("Laptop", 90000), ("Mobile", 30000),
     ("Pen", 50), ("Headphones", 1500)]

Product = []


def Push_element():

    for item in L:

        if item[1] > 50:
            Product.append(item)


def Pop_element():

    while len(Product) != 0:
        print(Product.pop())

    print("Stack Empty")


Push_element()
Pop_element()

# Write the following user-defined functions in Python:

# (i) push_trail(N, myStack):
#     Here N and myStack are lists, and myStack represents a stack.
#     The function should push the last 5 elements from the list N
#     onto the stack myStack.

#     For example, if the list N is:
#     [1, 2, 3, 4, 5, 6, 7]

#     then the function push_trail() should push the elements
#     3, 4, 5, 6, 7 onto the stack.

#     Therefore, the value of stack will be:
#     [3, 4, 5, 6, 7]

#     Assume that N contains at least 5 elements.

# (ii) pop_one(myStack):
#      The function should pop an element from the stack myStack
#      and return this element.

#      If the stack is empty, then the function should display the
#      message "Stack Underflow" and return None.

# (iii) display_all(myStack):
#       The function should display all the elements of the stack
#       myStack, without deleting them.

#       If the stack is empty, the function should display the
#       message "Empty Stack".


def push_trail(N, myStack):
    for i in range(-5, 0):
        myStack.append(N[i])


def pop_one(myStack):
    if len(myStack) == 0:
        print("Stack Underflow")
        return None
    else:
        return myStack.pop()


def display_all(myStack):
    if len(myStack) == 0:
        print("Empty Stack")
    else:
        for item in myStack:
            print(item)


# Example
N = [1, 2, 3, 4, 5, 6, 7]
myStack = []

push_trail(N, myStack)

print(myStack)

print(pop_one(myStack))

display_all(myStack)