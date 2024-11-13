print("Welcome to the To_do_list")
User_List=[]
def Create():
        Work = input("which work you want to create on your list\n")
        User_List.append(Work)
        print(f"Your current Work_list  is\n:{Work}")
def Update():
    if len(User_List) == 0:
        print(f"your work list is empty\n{User_List}")
    else:
        Task=input("Please tell the work you want to updated\n")
        New_Task=input("Please name the new task you want to add\n")
        if Task in User_List:
            ind=User_List.index(Task)
            User_List[ind]=New_Task
            print(f"Updated {Task} are\n:{User_List}")
        else:
            print(f"Your '{Task}' is not in User_List\n{User_List}")
def Track():
    if len(User_List)==0:
        print(f"Your Work_list is empty\n{User_List}")
    else:
        for i in User_List:
            print(f"{User_List.index(i)+1}. {i}")
while True:
    print("1.To Create the list") 
    print("2.Update the list") 
    print("3.Track the list") 
    print("4.Exit from the To_do_list")
    choices=(int(input("choose your number\n")))    
    if choices ==1:
        Create()
    elif choices ==2:
        Update()   
    elif choices ==3:
        Track()   
    elif choices ==4:   
        print("Goodbye")
        break
    else:
        print("Invalid no.(wrong choice)")
