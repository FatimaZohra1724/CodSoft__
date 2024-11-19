print("Welcome to Calculator")
def Add(User_choice_1,User_choice_2):    
    result= User_choice_1+User_choice_2
    print(f"your Add is:\n{result}")
    return result
def Sub(User_choice_1,User_choice_2):
    result= User_choice_1-User_choice_2
    print(f"your subtract is:\n{result}")
    return result
def Mul(User_choice_1,User_choice_2):
    result= User_choice_1*User_choice_2
    print(f"your Multiply is:\n{result}")
    return result
def Divi(User_choice_1,User_choice_2):
    if User_choice_2 == 0:
        print("It is (undefined)")
        return None
    else:
        result= User_choice_1/User_choice_2
        print(f"your Divide is:\n{result}")
        return result
    
while True:
    print("1.Add(+)")
    print("2.Subtract(-)")
    print("3.Multiply(*)")
    print("4.Divison(/)")
    print("5.Exit")
    try:
        choices=int(input("What operation did you want to perform-\n"))
        if choices in[1,2,3,4]:
                User_choice_1=float(input("What is your 1st number\n"))
                User_choice_2=float(input("What is your 2nd number\n"))

                if choices == 1:
                    result= Add(User_choice_1,User_choice_2)
                elif choices == 2:
                    result= Sub(User_choice_1,User_choice_2)
                elif choices == 3:
                    result= Mul(User_choice_1,User_choice_2)
                elif choices == 4:
                    result= Divi(User_choice_1,User_choice_2)
        elif choices == 5:   
            print("Goodbye!Use me Again.")
            break
        else:
            print("Wrong no. is choosen try again.")
    except ValueError:
        print("Invalid Input! choose wisely")