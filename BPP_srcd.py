


def rec_multi_src():
        print('''
    number1=float(input("Enter the 1st number you want to multiply : "))

    while True:
        number2=float(input("Enter the number you want to multiply : "))
        total=number1*number2
        print("The answer is : ",total)
        choice=input("Do you wish to multiply further (y/n) ?")
        if choice == "y" or choice =="Y":
            print(f"Currently the total is at : {total} \n")
            number1=total
            number2=1.0
        
        else :
            sleep()
            print(f"Final Answer : {total} \n")
              ''')
    