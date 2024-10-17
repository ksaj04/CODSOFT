
def calculator():

    num1=float(input("Enter the first number to do operation :"))
    num2=float(input("Enter the second number to do operation :"))

    print("\nselect the operation :")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice=input("Enter the choice to do operation :")

    if choice == '1':
        result=num1+num2
        print(f"\nResult: {num1} + {num2} = {result}")

    elif choice == '2':
        result=num1-num2
        print(f"\nResult: {num1} - {num2} = {result}")

    elif choice == '3':
        result=num1*num2
        print(f"\nResult: {num1} * {num2} = {result}")

    elif choice == '4':
     if num2 !=0 :
        result=num1/num2
        print(f"\nResult: {num1} / {num2} = {result}")
     else :
         print(f"\n division by zero is not allowed")

    else :
        print("Invalid choice please enter valid choice !!")


calculator()




