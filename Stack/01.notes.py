# ============================================================
#                         STACK
#                  CBSE CLASS 12 CS
# ============================================================

# A STACK is a linear data structure that follows:
#
#                 LIFO
#          Last In, First Out
#
# The element inserted LAST is removed FIRST.


# Example:
#
#       |  30  |  <- TOP
#       |  20  |
#       |  10  |
#       -------
#
# If we remove an element -> 30 is removed first.


# ============================================================
#                    BASIC STACK OPERATIONS
# ============================================================

# 1. PUSH
#    Insert an element into the stack.

# 2. POP
#    Remove an element from the top of the stack.

# 3. PEEK / TOP
#    View the top element without removing it.

# 4. DISPLAY
#    Display all elements of the stack.


# ============================================================
#                 STACK USING PYTHON LIST
# ============================================================

# A Python list can be used to implement a stack.

stack = []


# ------------------------------------------------------------
# 1. PUSH
# ------------------------------------------------------------

# append() is used to insert an element.

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Output:
# [10, 20, 30]


# The LAST element is the TOP.

# TOP = 30


# ------------------------------------------------------------
# 2. POP
# ------------------------------------------------------------

# pop() removes and returns the LAST element.

x = stack.pop()

print(x)

# Output:
# 30


# Stack is now:
# [10, 20]


# IMPORTANT:
# append() -> PUSH
# pop()    -> POP


# ============================================================
#                       PEEK
# ============================================================

# Peek means viewing the TOP element
# without removing it.

stack = [10, 20, 30]

top = stack[-1]

print(top)

# Output:
# 30

# stack remains:
# [10, 20, 30]


# ============================================================
#                      DISPLAY
# ============================================================

stack = [10, 20, 30]

for item in stack:
    print(item)


# ============================================================
#                  CHECK EMPTY STACK
# ============================================================

stack = []

if len(stack) == 0:
    print("Stack is empty")


# A simpler method:

if not stack:
    print("Stack is empty")


# ============================================================
#                     PUSH FUNCTION
# ============================================================

def Push(stack, item):
    stack.append(item)


stack = []

Push(stack, 10)
Push(stack, 20)
Push(stack, 30)

print(stack)


# ============================================================
#                      POP FUNCTION
# ============================================================

def Pop(stack):

    if len(stack) == 0:
        print("Stack Underflow")

    else:
        return stack.pop()


stack = [10, 20, 30]

print(Pop(stack))


# Output:
# 30


# ============================================================
#                 STACK UNDERFLOW
# ============================================================

# Underflow occurs when we try to POP
# from an empty stack.

stack = []

if len(stack) == 0:
    print("Stack Underflow")

else:
    print(stack.pop())


# IMPORTANT:
# POP from empty stack -> UNDERFLOW


# ============================================================
#                COMPLETE STACK PROGRAM
# ============================================================

stack = []

def Push():
    item = int(input("Enter element: "))
    stack.append(item)


def Pop():

    if len(stack) == 0:
        print("Stack Underflow")

    else:
        print("Deleted element:", stack.pop())


def Peek():

    if len(stack) == 0:
        print("Stack is empty")

    else:
        print("Top element:", stack[-1])


def Display():

    if len(stack) == 0:
        print("Stack is empty")

    else:
        print("Stack:", stack)


# ============================================================
#                    MENU-DRIVEN STACK
# ============================================================

stack = []

while True:

    print("\n1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY")
    print("5. EXIT")

    choice = int(input("Enter choice: "))

    if choice == 1:

        item = int(input("Enter element: "))
        stack.append(item)

    elif choice == 2:

        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped:", stack.pop())

    elif choice == 3:

        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top:", stack[-1])

    elif choice == 4:

        print(stack)

    elif choice == 5:
        break

    else:
        print("Invalid choice")


# ============================================================
#              STACK USING FUNCTIONS
# ============================================================

# A common CBSE question may give a list
# and ask you to perform stack operations.

def Push(S, item):

    S.append(item)


def Pop(S):

    if S == []:
        print("Underflow")

    else:
        return S.pop()


def Peek(S):

    if S == []:
        print("Empty Stack")

    else:
        return S[-1]


# ============================================================
#               IMPORTANT LIST METHODS
# ============================================================

# append()
# -> Adds an element at the END of the list.
# -> Used for PUSH.

stack.append(50)


# pop()
# -> Removes the LAST element.
# -> Used for POP.

stack.pop()


# stack[-1]
# -> Gives the LAST element.
# -> Used for PEEK.


# ============================================================
#              STACK VS NORMAL LIST ACCESS
# ============================================================

stack = [10, 20, 30]

stack.append(40)

# PUSH 40

# Stack:
# [10, 20, 30, 40]


stack.pop()

# POP 40

# Stack:
# [10, 20, 30]


# ============================================================
#                    STACK EXAMPLE
# ============================================================

stack = []

stack.append("A")
stack.append("B")
stack.append("C")

# Stack:
#
# C <- TOP
# B
# A


stack.pop()

# C removed

# Stack:
#
# B <- TOP
# A


stack.append("D")

# Stack:
#
# D <- TOP
# B
# A


# ============================================================
#                     KEY TERMS
# ============================================================

# STACK
# -> Linear data structure following LIFO.

# LIFO
# -> Last In, First Out.

# PUSH
# -> Insert an element at the TOP.

# POP
# -> Remove an element from the TOP.

# PEEK
# -> View the TOP element without removing it.

# TOP
# -> Position of the most recently inserted element.

# UNDERFLOW
# -> Trying to POP from an empty stack.


# ============================================================
#                     QUICK REVISION
# ============================================================

# PUSH:
# stack.append(item)

# POP:
# stack.pop()

# PEEK:
# stack[-1]

# EMPTY:
# len(stack) == 0
# OR
# not stack

# UNDERFLOW:
# POP when stack is empty


# ============================================================
#                     MOST IMPORTANT
# ============================================================

# STACK = LIFO
#
# PUSH  = append()
# POP   = pop()
# PEEK  = stack[-1]
#
# Empty stack + POP = Underflow