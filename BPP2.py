import time

def anima_print(text):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.003)

def sleep():
    time.sleep(0.5)

def dic_to_list(topic):
        #using the keys as a list to print 
        temp=[]
        for i in topic.keys():
            temp.append(i)
        return temp

def greet(topic,choice):
    print(f"Hello! You are in the {topic[choice]} Section")

def exit_status():
    anima_print('''
    |\__/,|   (`)
  _.|o o  |_   ) )
-(((---(((-------------------------------------------------------------------------------------------------------------
                                        ''')
    print("Thank you for using BPP.")



#-----------------------------------------------------------------------------------------------------------------------------



def main():
    anima_print(r'''
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
    print("\n\n")
    menu()  


def menu():
    sleep()
    choice=input_choice_func(MENUP)
    check_choice(choice,MENU)


def maths():
    sleep()
    choice=input_choice_func(MATHSP)
    check_choice(choice,MATHS)
    greet(MATHS,choice)


def addition():
    sleep()
    choice=input_choice_func(ADDITIONP)
    check_choice(choice,ADDITION)
    greet(ADDITION,choice)


def simple_add():
    sleep()
    numbers_to_add1=float(input("\nEnter the 1st number you want to add : "))
    numbers_to_add2=float(input("Enter the 2nd number you want to add : "))
    sleep()
    print(f"Sum of {numbers_to_add1} and {numbers_to_add2} is : {numbers_to_add1 + numbers_to_add2} \n")

    addition()


def rec_add():
    sleep()
    numbers_to_add1=float(input("\nEnter the 1st number you want to add : "))

    while True:
        numbers_to_add2=float(input("Enter the number you want to add : "))
        sum=numbers_to_add1+numbers_to_add2
        print("The answer is : ",sum)
        choice=input("Do you wish to add further (y/n) ?")
        if choice == "y" or choice =="Y":
            print(f"Currently the sum is : {sum} \n")
            numbers_to_add1=sum
            numbers_to_add2=0.0
        
        else :
            sleep()
            print(f"Final Answer : {sum} \n")
            break

    addition()


def subtraction():
    sleep()
    print("\nHello! You are in the Subtraction Section")
    sub1=float(input("\nEnter the first number: "))
    sub2=float(input("Enter the second number: "))
    
    
    sleep()
    print("The difference between the two is: ", (sub1-sub2))
    
    maths()


def multiplication():
    sleep()
    choice=input_choice_func(MULTIPLICATIONP)
    check_choice(choice,MULTIPLICATION)
    greet(MULTIPLICATION,choice)


def simple_multi():
    n1=float(input("\nEnter the number you wish to multiply : "))
    n2=float(input(f"Enter the number you wish to multiply with {n1} : "))
    print(f"The product of {n1} and {n2} is = {n1*n2}")

    maths()


def rec_multi():
    number1=float(input("\nEnter the 1st number you want to multiply : "))

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
            sleep()
            break

    multiplication()


def division():
    sleep()
    choice=input_choice_func(DIVISIONP)
    check_choice(choice,DIVISION)
    greet(DIVISION,choice)


def simple_div():
    sleep()
    num1=float(input("\nEnter the number you want to divide : "))
    num2=float(input("Enter the number you want to dive with : "))
    print("The quotient is : ", (lambda a,b: a/b)(a=num1,b=num2))
    print("The remainder is : ",  (lambda a,b: a % b)(a=num1,b=num2)) 
    
    division()
              

def rec_div():
    sleep()
    num1=float(input("\nEnter the number you want to start dividing with :"))
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

            division()

            break



#-----------------------------------------------------------------------------------------------------------------------------


def pattern():
    sleep()
    choice=input_choice_func(PATTERNP)
    check_choice(choice,PATTERN)
    greet(PATTERN,choice) 


def box():
    sleep()
    choice=input_choice_func(BOXP)
    check_choice(choice,BOX)
    greet(BOX,choice) 

def rectangle():
    sleep()
    l=int(input("\nEnter the length of the rectangle you want to create : "))
    b=int(input("Enter the breath of the rectangle you want to create : "))
    ch=input("Enter any character you want the rectangle to be made with : ")

    while b>0:
        print(ch*l)
        b-=1

    box()


def square():
    sleep()
    a=int(input("\nEnter the side of the squre : "))
    ch=input("Enter any character you want the rectangle to be made with : ")
    tmp=a
    while a>0:
        print(ch*tmp)
        a-=1

    box()


def triangle():
    sleep()
    choice=input_choice_func(TRIANGLEP)
    check_choice(choice,TRIANGLE)
    greet(TRIANGLE,choice)

def right_angle_tri_left():
    sleep()
    n=int(input("Enter the size of the triangle you wish to create : "))
    chc=input("Enter the character you want the traingle to be made of : ")
    for i in range (1,n):
        print(chc*i)
    
    triangle()


def right_angle_tri_right():
    sleep()
    pass

def right_angle_tri_upsidedown_left():
    sleep()

    pass

def right_angle_tri_upsidedown_right():
    sleep()

    pass

def equilateral_triangle():
    sleep()

    pass


def circle():
    sleep()
    choice=input_choice_func(PATTERNP)
    check_choice(choice,PATTERN)
    greet(PATTERN,choice)



#-----------------------------------------------------------------------------------------------------------------------------


            
def other():
    sleep()
    choice=input_choice_func(OTEHRSP)
    check_choice(choice,OTHERS)
    greet(OTHERS,choice) 


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
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    encrypted_text = caesar_cipher(text, shift)
    print("Original text: ", text)
    print("Encrypted text: ", encrypted_text)




#-----------------------------------------------------------------------------------------------------------------------------



#The function below is a function that makes the menu the way it is, displays the options from the respective dictionaries or lists and 
#takes the returns the users choice 
    
def input_choice_func(topic): 

    if type(topic)==dict:
    #topic here will be the topic you are currently surfing through

        tmp=dic_to_list(topic)

        #printing the available options for dictionary
        for key in topic.keys() :
            print(f"Enter {key} for ", topic[key])
        
        choice=input("Enter your choice : ")
        
        if (str(choice) not in str(tmp)):
            print("\nInvalid Input\n")

            input_choice_func(topic)

        return choice

        

    else:
        #printing the options if its a list 
        for i in range (len(topic)):
            print(f"Enter {i+1} for "+topic[i])

        choice=input("Enter your choice : ")

        if (0> int(choice) >= len(topic)):
            print("\nInvalid Input\n")

            input_choice_func(topic)


        return choice





#check menu 
#this is where that choice matters, here the users choice is used to navigate thru the available functions and calls it

def check_choice(choice,topic):

    choice=int(choice) #because the input function returns choice as a string 

    if type(topic)==dict: #so that this function can be used for dictionaries and lists

        for key in topic:

            if choice == key:

                time.sleep(0.5)
                print()
                topic[key]() #executes the function contained in the dictionary 
                break

    else:
       for i in len(topic):
           print(f"Enter {i+1} for "+str(topic[i]))



#-----------------------------------------------------------------------------------------------------------------------------


                
'''DATABASE
Any changes you want to make in the options, or add new projects or change the way for navigation can be done here
__________________________________________________________________________________________________________________
'''


OTHERS={1:caesar_cipher,
        2:menu}

OTEHRSP={1:"Ceasar Cipher",
        2:"Go Back"}


#---------------------------------------------------------------------------------------------------------------------------


PATTERN={1:box,
         2:triangle,
         3:circle,
         4:menu}

PATTERNP={1:"Box Programs",
          2:"Triangle Pattern Programs",
          3:"Circle Pattern programs",
          4:"Go Back"}


BOX={1:rectangle,
     2:square,
     3:pattern}

BOXP={1:"Rectangle Pattern Program",
      2:"Square Pattern Program",
      3:"Go Back"}


TRIANGLE={1:right_angle_tri_left,
          2:right_angle_tri_right,
          3:right_angle_tri_upsidedown_left,
          4:right_angle_tri_upsidedown_right,
          5:equilateral_triangle,
          6:pattern}

TRIANGLEP={1:"Right angle triangle on the left side ",
           2:"Right angle triangle on the right side",
           3:"Upside down right angle triangle on the left side",
           4:"Upside down right angle triangle on the right side",
           5:"Equilateral triangle",
           6:"Go Back"}


CIRCLE={}

CIRCLEP={}




#---------------------------------------------------------------------------------------------------------------------------


MATHS={ 1 : addition,
        2 : subtraction ,
        3 : multiplication, 
        4 : division, 
        5 : menu}

MATHSP={1:"Addition Programs",
        2:"Subtraction Program",
        3:"Multiplication Programs",
        4:"Division Programs",
        5:"Go Back"}


#---------------------------------------------------------------------------------------------------------------------------


ADDITION={1: simple_add , 
          2: rec_add , 
          3: maths}

ADDITIONP={1: "Simple Addition", 
           2: "Recurring Addition" , 
           3: "Go Back"}


#---------------------------------------------------------------------------------------------------------------------------


MULTIPLICATION={1: simple_multi,
                2: rec_multi,
                3: maths}

MULTIPLICATIONP={1: "Multiplication of Two Numbers",
                2: "Recurring Multiplication",
                3: "Go Back"}

#---------------------------------------------------------------------------------------------------------------------------


DIVISION={1:simple_div,
          2:rec_div,
          3:maths}

DIVISIONP={1:"Simple Division",
          2:"Recurring Division",
          3:"Go Back"}


#---------------------------------------------------------------------------------------------------------------------------


MENU={1:maths, 
      2:pattern, 
      3:other, 
      4:exit_status}

MENUP={1:"Basic Mathematics Programs", 
       2:"Pattern Programs", 
       3:"Other Projects", 
       4:"Exit"}
    

#---------------------------------------------------------------------------------------------------------------------------
    

main()
