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
#importing libraries in the program vvv

import time


#-------------------------------------------------------------------------------------------------
#this is the pattern programs section vvv

def pattern_programs():
    print("\nYou are in the Pattern Programs Menu")
    print("Press 1 for Triangles \nPress 2 for Box Box Box \nPress 3 for Circle \nPress 4 to go back to the Main Menu \n")
    chc1=input("Enter your choice :")
    if chc1=="1":
        triangle_menu()
    elif chc1=="2":
        box_menu()
    elif chc1=="3":
        circle_menu()
    elif chc1=="4":
        print("You will be transfered to the main menu :) ")
        time.sleep(0.5)
        main_menu()
    else:
        print("There must have been some error")
        time.sleep(0.5)
        pattern_programs()



def triangle_menu():
    print("\nTriangle Menu :\n1. [Left Side]Right Angle Icosceles Triangle \n2. [Right Side]Right Angle Icosceles Triangle \n3. [Left Side]Upside Down Right Angle Icosceles Triangle \n4. [Right Side]Upside Down Right Angle Icosceles Triangle\n5. [Center]Equilateral Triangle \n6. [Left Side]Equilateral Triangle \n7. [Right Side]Equilateral Triangle \n8. Go back to the Pattern Programs Menu")
    chc=input("Enter your choice: ")
    if chc=="1": #[Left Side]Right Angle Icosceles Triangle
        size=int(input("Enter the number of lines you want the triangle to cover : "))
        character=input("Enter the character you want to use in the Triangle")
        for i in range (1,size):
            for j in range(1,i):
                print(character , end=" ")
            print()
        time.sleep(1) #time delay so that everything doesnt happen in a flash
        print("Here is the code for the above operation :")
        print('''
        for i in range (1,size):
            for j in range(1,i):
                print(character , end=" ")
            print()''')
        time.sleep(0.5)
        triangle_menu()
        
    elif chc=="2": #[Right Side]Right Angle Icosceles Triangle
        size=int(input("Enter the number of lines you want the triangle to cover : "))
        character=input("Enter the character you want to use in the Triangle")
        for i in range (size,1,-1):
            for j in range(1,i):
                print(character , end=" ")
            print()
        time.sleep(1) #time delay so that everything doesnt happen in a flash
        print("Here is the code for the above operation :")
        print('''
        for i in range (size, 1,-1):
            for j in range(1,i):
                print(character , end=" ")
            print()''')
        time.sleep(0.5)
        triangle_menu()

    
    elif chc=="3":
        size=int(input("Enter the number of lines you want the triangle to cover : "))
        character=input("Enter the character you want to use in the Triangle")
        for i in range (size,1,-1):
            for j in range(1,i):
                print(character , end=" ")
            print()
        time.sleep(1) #time delay so that everything doesnt happen in a flash
        print("Here is the code for the above operation :")
        print('''
        for i in range (size, 1,-1):
            for j in range(1,i):
                print(character , end=" ")
            print()''')
        time.sleep(0.5)
        triangle_menu()

    elif chc=="4":

    elif chc=="5":


    elif chc=="8":
        print("You will be returned back to the Pattern Programs Menu")
        time.sleep(0.5)
        pattern_programs()
    
    else:
        print("There must have been some error")
        time.sleep(0.5)
        triangle_menu()
    


def box_menu():
    print("\nBox Menu :\n1. Square \n2. Rectangle \n3. Diamond")

def circle_menu():
    print("\nCircle Menu :\n1. Simple Circle \n2. Semi Circle \n3. Spinning Donut")


#-------------------------------------------------------------------------------------------------
#this is the basic maths program section vvv

def basic_math_prog():
    print("\nYou are in the basic mathematics programs menu ")
    print("\nPress 1 for Addition Programs \nPress 2 for Subtraction Programs \nPress 3 for Multiplication Programs \nPress 4 for Division Programs \nPress 5 to Go back to the Main Menu \n")
    chc2=input("Enter your choice :")
    if chc2=="1":
        addition_programs()
    elif chc2=="2":
        subtraction_programs()
    elif chc2=="3":
        multiplication_progarm()
    elif chc2=="4":
        division_programs()
    elif chc2=="5":
        print("You will be transfered to the main menu :) ")
        time.sleep(0.5) #time delay so that everything doesnt happen in a flash (keep it at 0.5)
        main_menu()
    else:
        print("There must have been some error")
        time.sleep(1)
        basic_math_prog()
        

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
        time.sleep(1) #time delay so that everything doesnt happen in a flash
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
        time.sleep(1) #time delay so that everything doesnt happen in a flash
        basic_math_prog() #function recall to take you back to the basic maths menu
        
    else:
        print("How can you add "+str(numbers_to_add)+" numbers ")
        time.sleep(1) #time delay so that everything doesnt happen in a flash
        basic_math_prog() #function recall to take you back to the basic maths menu


def subtraction_programs():
    print("Hi! welcome to the Subtraction Section ")
    sub1=float(input("Enter the first number: "))
    sub2=float(input("Enter the second number: "))
    sub=sub1-sub2
    print("The difference between the two is: ",sub)
    time.sleep(1) #time delay so that everything doesnt happen in a flash
    print("Here is the code for the above operation :")
    print('''
    sub1=float(input("Enter the first number: "))
    sub2=float(input("Enter the second number: ")) 
    sub=sub1-sub2 
    print("The difference between the two is: ",sub)''')
    time.sleep(1) #time delay so that everything doesnt happen in a flash
    basic_math_prog() #function recall to take you back to the basic maths menu


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
        time.sleep(1) #time delay so that everything doesnt happen in a flash
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
        time.sleep(1) #time delay so that everything doesnt happen in a flash
        basic_math_prog() #function recall to take you back to the basic maths menu
    else:
        print("How can you multiply "+str(numbers_to_mult)+" numbers ")
        time.sleep(1) #time delay so that everything doesnt happen in a flash
        basic_math_prog() #function recall to take you back to the basic maths menu


def division_programs():
    print("Press 1 to perform a simple division between two numbers \nPress 2 to perform a reccuring division with each answer ")
    chc=input("Enter your choice : ")
    if chc=="1":
        num1=float(input("Enter the number you want to divide : "))
        num2=float(input("Enter the number you want to dive with : "))
        val=num1/num2
        print("The quotient is : ",val)
        rem=num1%num2
        print("The remainder is : ",rem)
        time.sleep(1) #time delay so that everything doesnt happen in a flash
        print("Here is the code for the above operation")
        print('''
        num1=float(input("Enter the number you want to divide : "))
        num2=float(input("Enter the number you want to dive with : "))
        val=num1/num2
        print("The quotient is : ",val)
        rem=num1%num2
        print("The remainder is : ",rem)
              ''')
        time.sleep(1) #time delay so that everything doesnt happen in a flash
        basic_math_prog() #function recall to take you back to the basic maths menu
        return False
    elif chc=="2":
        num1=float(input("Enter the number you want to start dividing with :"))
        while True:
            num2=float(input("Enter the number you want to divide with :"))
            div=num1/num2
            print("The answer is (quotient): ",div)
            choice=input("Do you wish to divide further (y/n) ?")
            if choice=="y" or choice=="Y":
                print("New Dividend : ",div)
                num1=div
                num2=0.0
            else :
                print("Final Answer : ",div)
                time.sleep(1) #time delay so that everything doesnt happen in a flash
                print("Here is the code for the above operation")
                print('''
        num1=float(input("Enter the number you want to start dividing with :"))
        while True:
            num2=float(input("Enter the number you want to divide with :"))
            div=num1/num2
            print("The answer is (quotient): ",div)
            choice=input("Do you wish to divide further (y/n) ?")
            if choice=="y" or choice=="Y":
                print("New Dividend : ",div)
                num1=div
                num2=0.0
            else :
                print("Final Answer : ",div)
                return False
                      ''')
                time.sleep(1) #time delay so that everything doesnt happen in a flash
                basic_math_prog() #function recall to take you back to the basic maths menu
                return False
    else:
        print("There must have been some error")
        time.sleep(1) #time delay so that everything doesnt happen in a flash
        basic_math_prog() #function recall to take you back to the basic maths menu
                


#-------------------------------------------------------------------------------------------------
#this is the calculator programs section vvv 

def calculator_prog():       
    print("Under Construction")
    main_menu()


#-------------------------------------------------------------------------------------------------
#this is the random projects programs section vvv 

def randon_proj():
    print("\nYou are in the Random Projects Menu")
    print("\nPress 1 to access the Cesar Cypher Code \nPress 2 to go back to the Main Menu")
    chc=input("Enter your choice: ")
    if chc=="1":
        ceasar_input()
    elif chc=="2":
        print("You will be transfered to the main menu :) ")
        time.sleep(0.5) #time delay so that everything doesnt happen in a flash (keep it at 0.5)
        main_menu()
    else :
        print("There must have been an error :/")
        time.sleep(0.5) #time delay so that everything doesnt happen in a flash (keep it at 0.5)
        randon_proj()
        
        



def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            # Shift the character by the specified amount
            shifted_char = chr(((ord(char) - ord('A' if is_upper else 'a') + shift) % 26) + ord('A' if is_upper else 'a'))
            encrypted_text += shifted_char
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_text += char
    return encrypted_text

def ceasar_input():
    text = input("enter text:")
    shift = int(input("enter shift value:"))
    encrypted_text = caesar_cipher(text, shift)
    print("Original text:", text)
    print("Encrypted text:", encrypted_text)
    time.sleep(1)
    randon_proj()


    




#-------------------------------------------------------------------------------------------------
#this is the animated print section

def anima_print(text):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.003)

#-------------------------------------------------------------------------------------------------
#this is the main menu you see in the start

def main_menu():
    print("\nEnter the serial numbers of the topics that interest you to access them")
    print("1. All Pattern Programs \n2. Basic Mathematics Programs \n3. Calculator Program \n4. Random Projects \n5. Exit")
    chc=int(input("Enter your choice [1,2,3,4 or 5] : "))
    if(chc==1):
        pattern_programs()
    elif(chc==2):
        basic_math_prog()
    elif(chc==3):
        calculator_prog()
    elif(chc==4):
        randon_proj()
    elif(chc==5):
        anima_print('''
    |\__/,|   (`)
  _.|o o  |_   ) )
-(((---(((-------------------------------------------------------------------------------------------------------------
                                        ''')
        print("Thank you for using BPP.")
    else:
        print("You must have made a wrong choice, you can always start again :) ")


#-------------------------------------------------------------------------------------------------
#this is the function call 

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
            

                        ~ 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚑𝚎 𝙱𝚊𝚜𝚒𝚌 𝙱𝚎𝚐𝚒𝚗𝚗𝚎𝚛 𝙿𝚛𝚘𝚐𝚛𝚊𝚖𝚜 𝙼𝚎𝚗𝚞 ~ 

<> 𝚈𝚘𝚞𝚛 𝚗𝚞𝚖𝚙𝚊𝚍 𝚠𝚒𝚕𝚕 𝚋𝚎 𝚝𝚑𝚎 𝚗𝚊𝚟𝚒𝚐𝚊𝚝𝚘𝚛 𝚝𝚑𝚛𝚘𝚞𝚐𝚑 𝚝𝚑𝚒𝚜 𝚙𝚛𝚘𝚐𝚛𝚊𝚖
<> 𝚃𝚑𝚒𝚜 𝚒𝚜 𝚊 𝚙𝚛𝚘𝚐𝚛𝚊𝚖 𝚝𝚑𝚊𝚝 𝚌𝚘𝚗𝚝𝚊𝚒𝚗𝚜 𝚊 𝚖𝚊𝚓𝚘𝚛𝚒𝚝𝚢 𝚘𝚏 𝚋𝚊𝚜𝚒𝚌 𝚙𝚛𝚘𝚐𝚛𝚊𝚖𝚜 𝚍𝚘𝚗𝚎 𝚒𝚗 𝚌𝚘𝚕𝚕𝚎𝚐𝚎 
   𝚊𝚗𝚍 s𝚌𝚑𝚘𝚘𝚕 𝚕𝚎𝚟𝚎𝚕, 𝚞𝚜𝚎 𝚒𝚝 𝚠𝚒𝚜𝚎𝚕𝚢 ''')
time.sleep(0.5)
main_menu()


#add the function recall menu after every error statement 
#pattern regognition and production for the program
#retrive replit database into the code
#lcm hcf 