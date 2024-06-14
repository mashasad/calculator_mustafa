def add (num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1-num2


def mutply (num1,num2):
    return num1 * num2

def division(num1, num2):
    return num1/num2

def power (num1, num2):
    return num1**num2

def getremainder (num1, num2):
    return num1%num2

def getwholennum (num1, num2):
    return num1//num2

operations = input ('''select one of the operations:\n
                    1 - Addition               2- subtraction \n
                    3 -division                4 mutiplication\n
                    5 -exponational            6 - get remainder\n
                    7 - get whole number       8- quit''')

list_operation =['1','2','3','4','5','6','7','8']

while operations != '8':
    if operations in list_operation:
        num1 = int(input('enter the first number:'))
        num2 = int(input('enter the second number:'))

        if operations == '1':
            answer = add(num1, num2)
        elif operations == '2':
            answer = subtraction(num1, num2)
        elif  operations == '3':
            answer =division(num1, num2)
        elif operations == '4':
            answer = mutply(num1, num2)
        elif operations == '5':
            answer = power(num1, num2)
        elif operations == "6":
            answer =getremainder(num1,num2)
        elif operations == "7":
            answer =getwholennum(num1,num2)
        print("answer is: ", answer)      
    
    else:
        print ("we could not find your request. plese try again!..\n\n")


    operations = input ('''select one of the operations:\n
                    1 - Addition               2- subtraction \n
                    3 -division                4 mutiplication\n
                    5 -exponational            6 - get remainder\n
                    7 - get whole number       8- quit''')
