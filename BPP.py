'''
Pattern Progs: 
    Triangle 
        right ang ico with numbers till user defined size and character
        right hand side right angle ico with numbers and user defined size and character
        two right angle ico making an equilateral triangle user defined size and character
        center equilateral triangle with user defined size and characters

    Box box box
        square
        rectangle
        diamond
    Circle
        simple circle
        semi circle
        spinning donut

'''

#-------------------------------------------------------------------------------------------------
#program vvv


import time



#-------------------------------------------------------------------------------------------------
#this is the pattern programs section vvv

def pattern_programs():
    print("You are in the Pattern Programs Menu")
    while True:
        print("Press 1 for Triangles \nPress 2 for Box Box Box \nPress 3 for Circle \nPress 4 to Exit")
        chc1=input("Enter your choice :")
        if chc1==1:
            triangle_menu()
        elif chc==2:
            box_menu()
        elif chc==3:
            circle_menu()


def triangle_menu():
    print("Triangle Menu :\n1. [Left Side]Right Angle Icosceles Triangle \n2. [Right Side]Right Angle Icosceles Triangle \n3. [Center]Equilateral Triangle \n4. [Left Side]Equilateral Triangle \n5. [Right Side]Equilateral Triangle ")

def box_menu():
    print("Box Menu :\n1. Square \n2. Rectangle \n3. Diamond")

def circle_menu():
    print("Circle Menu :\n1. Simple Circle \n2. Semi Circle \n3. Spinning Donut")


#-------------------------------------------------------------------------------------------------
#this is the basic maths program section vvv

def basic_math_prog():
    print("You are in the basic mathematics programs menu ")
    while True:
        print("Press 1 for Addition Programs \nPress 2 for Subtraction Programs \nPress 3 for Multiplication Programs \n Press 4 for Division Programs")
        chc2=input("Enter your choice :")
        if chc2==1:
            addition_programs()
        elif chc2==2:
            subtraction_programs()
        elif chc2==3:
            multiplication_progarm()
        elif chc2==4:
            division_programs()
        

def addition_programs():
    print("Hi! welcome to the Addition Section ")
    numbers_to_add=int(input("How many numbers do you want to add: "))
    counter=1
    sum=0
    if numbers_to_add>0:
        while numbers_to_add>=counter:
            value=float(input("Enter "+str(numbers_to_add)+" number(s) "))
            sum=sum+value
            numbers_to_add=numbers_to_add-1
        print("The total sum is:",sum)
        print("Here is the code for the above operation :")
        print('''
    numbers_to_add=int(input("How many numbers do you want to add: "))
    counter=1
    sum=0
    if numbers_to_add>0:
        while numbers_to_add>=counter:
            value=float(input("Enter "+str(numbers_to_add)+" number(s) "))
            sum=sum+value
            numbers_to_add=numbers_to_add-1
        print("The total sum is:",sum)
    else:
        print("How can you add "+str(numbers_to_add)+" numbers ")''')
        
    else:
        print("How can you add "+str(numbers_to_add)+" numbers ")

def subtraction_programs():
    print("Hi! welcome to the Subtraction Section ")
    sub1=float(input("Enter the first number: "))
    sub2=float(input("Enter the second number: "))
    sub=sub1-sub2
    print("The difference between the two is: ",sub)
    print("Here is the code for the above operation :")
    print('''
    sub1=float(input("Enter the first number: "))
    sub2=float(input("Enter the second number: ")) 
    sub=sub1-sub2 
    print("The difference between the two is: ",sub)''')

def multiplication_progarm():
    print("Hi! welcome to the Multiplication Section ")
    numbers_to_mult=int(input("How many numbers do you want to multiply: "))
    counter=1
    sum=1.0
    if numbers_to_mult>0:
        while numbers_to_mult>=counter:
            value=float(input("Enter "+str(numbers_to_mult)+" number(s) "))
            sum=sum*value
            numbers_to_mult=numbers_to_mult-1
        print("The total after multiplying everything is:",sum)
        print("Here is the code for the above operation :")
        print('''
    numbers_to_mult=int(input("How many numbers do you want to multiply: "))
    counter=1
    sum=1.0
    if numbers_to_mult>0:
        while numbers_to_mult>=counter:
            value=float(input("Enter "+str(numbers_to_mult)+" number(s) "))
            sum=sum*value
            numbers_to_mult=numbers_to_mult-1
        print("The total after multiplying everything is:",sum)
    else:
        print("How can you multiply "+str(numbers_to_mult)+" numbers ")
              ''')
    else:
        print("How can you multiply "+str(numbers_to_mult)+" numbers ")

def division_programs():
    print("Press 1 to perform a simple division between two numbers \nPress 2 to perform a reccuring division with each answer \nPress 3 to terminate")
    chc=("Enter your choice : ")
    while True:
        if chc==1:
            num1=float(input("Enter the number you want to divide"))
            num2=float(input("Enter the number you want to dive with"))
            val=num1/num2
            print("The quotient is : ",val)
            rem=num1%num2
            print("The remainder is : ",rem)
        elif chc==2:
            num1=float(input("Enter the number you want to start dividing with :"))
            decision=True
            while decision==True:
                num2=float(input("Enter the number you want to divide with"))
                #try to make the naswer come out and based on the users reply whather they want to conitnue dividing or not
                #take the input nad do it again 
                


#-------------------------------------------------------------------------------------------------
#this is the calculator programs section vvv 


def calculator_prog():       
    print("yooo")





#-------------------------------------------------------------------------------------------------
#this is the primary menu section vvv
def anima_print(text):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.003)





anima_print('''
    |\__/,|   (`)
  _.|o o  |_   ) )
-(((---(((-------------------------------------------------------------------------------------------------------------
  ____            _         ____                                             ____                                      
 | __ )  __ _ ___(_) ___   |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___  ___   |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___  
 |  _ \ / _` / __| |/ __|  | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \/ __|  | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \ 
 | |_) | (_| \__ \ | (__   |  __/| | | (_) | (_| | | | (_| | | | | | \__ \  |  __/| | | (_) | (_| | | | (_| | | | | | |
 |____/ \__,_|___/_|\___|  |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|___/  |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|
                                            |___/                                            |___/                     
                                                                                                ~ 𝗮𝘆𝘂𝘀𝗵𝗵𝗮𝗻𝗴
            

                        ~ 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚑𝚎 𝙱𝚊𝚜𝚒𝚌 𝙱𝚎𝚐𝚒𝚗𝚗𝚎𝚛 𝙿𝚛𝚘𝚐𝚛𝚊𝚖𝚜 𝙼𝚎𝚗𝚞 ~ \n\n<> 𝚈𝚘𝚞𝚛 𝚗𝚞𝚖𝚙𝚊𝚍 𝚠𝚒𝚕𝚕 𝚋𝚎 𝚝𝚑𝚎 𝚗𝚊𝚟𝚒𝚐𝚊𝚝𝚘𝚛 𝚝𝚑𝚛𝚘𝚞𝚐𝚑 𝚝𝚑𝚒𝚜 𝚙𝚛𝚘𝚐𝚛𝚊𝚖
<> 𝚃𝚑𝚒𝚜 𝚒𝚜 𝚊 𝚙𝚛𝚘𝚐𝚛𝚊𝚖 𝚝𝚑𝚊𝚝 𝚌𝚘𝚗𝚝𝚊𝚒𝚗𝚜 𝚊 𝚖𝚊𝚓𝚘𝚛𝚒𝚝𝚢 𝚘𝚏 𝚋𝚊𝚜𝚒𝚌 𝚙𝚛𝚘𝚐𝚛𝚊𝚖𝚜 𝚍𝚘𝚗𝚎 𝚒𝚗 𝚌𝚘𝚕𝚕𝚎𝚐𝚎 \n𝚊𝚗𝚍 s𝚌𝚑𝚘𝚘𝚕 𝚕𝚎𝚟𝚎𝚕, 𝚞𝚜𝚎 𝚒𝚝 𝚠𝚒𝚜𝚎𝚕𝚢 ''')
time.sleep(0.5)
print("\n\nEnter the serial numbers of the topics that interest you to access them")
while True:
    print("1. All Pattern Programs \n2. Basic Mathematics Programs \n3. Calculator Program \n4. \n5. Exit")
    chc=int(input("Enter your choice[1,2,3,4 or 5]:"))
    if(chc==1):
        pattern_programs()
    elif(chc==2):
        basic_math_prog()
    elif(chc==3):
        calculator_prog()
    elif(chc==4):
        ()
    elif(chc==5):
        print("Thank you.")
        break
    else:
        print("You must have made a wrong choice, you can always start again :) ")
