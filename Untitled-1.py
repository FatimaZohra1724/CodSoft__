print("Welcome to the To_do_list")
List=[]
while True:
   print("1.To Create the list") 
   print("2.Update the list") 
   print("3.Track the list") 
   print("4.Exit from the To_do_list") 
   break
choices=print(int(input("choose your number\n")))



if choices == 1:
    Create()
elif choices == 2:
    Update() 
elif choices == 3:
    Track()
elif  choices == 4:
    print("Goodbye")
else:
    print("Invalid no.(wrong choice)")