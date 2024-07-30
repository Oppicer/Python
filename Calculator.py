#variables
answer = 0
factor1 = 0
factor2 = 0
sign = ""

#functions
def first_step():
    global factor1
    factor1 = input("Enter your first factor")


def second_step():
    global sign, factor1
    if int(factor1) >= 0 or int(factor1) < 0:
        sign = input("type plus, minus, multiplication, or division")
    

def adding():
    global answer, factor1, factor2
    answer = int(factor1) + int(factor2)


def subtracting():
    global answer, factor1, factor2
    answer = int(factor1) - int(factor2)
 

def multiplying():
    global answer, factor1, factor2
    answer = int(factor1) * int(factor2)

def dividing():
    global answer, factor1, factor2
    answer = int(factor1) / int(factor2)

def third_step():
    global sign, factor1, factor2
    if sign == "plus":
        factor2 =input("Enter your second factor")
        adding()
    elif sign == "minus":
        factor2 = input("Enter your second factor")
        subtracting()
    elif sign == "multiplication":
        factor2 =input("Enter your second factor")
        multiplying()
    elif sign == "division":
        factor2 =input("Enter your second factor")
        dividing()
    else:
        print("unrecognized, try again")
        third_step()


def fourth_step():
    global answer
    print (answer)



first_step()
second_step()
third_step()
fourth_step()

    


    
    
    
