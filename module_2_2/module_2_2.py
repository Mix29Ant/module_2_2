# Program "Is All Entered Numbers Equals?"

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
# Following string of code:
if type(first)==int and type(second)==int and type(third)==int :
    if first == second and second == third :
            print("3")
    elif first == second or second == third or first == third :
            print ("2")
    else :
        print("0")
# and following's two strings of can be omitted(these lines was added for reliability only)
else:
    print("Wrong type of args appeared")