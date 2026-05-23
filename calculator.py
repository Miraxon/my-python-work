a=float(input("Type the first number:  "))
b=float(input("Type the second number:  "))
operation=input("Choose the operation(add,subtract,multiply or divide): ").lower()
def calculator(a,b,operation):
    if operation=="add":
        result=a+b
    if operation=="subtract":
        result= a-b
    if operation=="multiply":
        result= a*b
    if operation=="divide":
        result= a/b
    print(result)

calculator(a,b,operation)
