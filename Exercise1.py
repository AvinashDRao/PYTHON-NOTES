# WAP OF SINGLE DIGIT,DOUBLE DIGIT AND THREE DIGIT

user_input=int(input('enter the user input-1 :  '))
if user_input in range(0,10):
    print(user_input*100)
if user_input in range (10,100):
    print(user_input**5)
if user_input in range(100,1000):
    user_input_02=int(input('enter the user input-2 :  '))
    print(user_input+user_input_02)


# WAP OF MILEAGE OF THE BIKE

initial_reading=int(input('enter the initial odometer reading :  '))
final_reading=int(input('enter the final odometer reading :  '))
fuel_consumption=int(input('enter the fuel consumption in litre :  '))
mileage=(fuel_consumption-initial_reading)/fuel_consumption
print(f'mileage of the bike is {mileage} Kmpl')


# WAP OF MULTIPLICATION TABLE FOR USER INPUT

user_input=int(input('enter the number: '))
for i in range(1,11):
    table=(user_input)*i
    print(user_input,'x',i,'=',table)


# WAP OF EVEN_ODD_PRIME NUMBER

user_input=int(input('Enter the number:  '))
if user_input==0:
    print ('user_input is invalid number')
else:
    if user_input>1:
        for i in range(2,user_input):
            if   (user_input%i)==0:
                print ('user_input is not a prime number')
                break
        else:
            print ('user_input is a prime number') 
    else:
        print ('user_input is a prime number')

    if (user_input % 2)==0:
        print('User_input is even number')
    else:
        print('User_input is odd number')

