#Booleans - True/False
#Arithmetic - +,-,/,*,%
#Conditional - <,>,==,<>or=!
#Logical operators - And, or, not
#If-Else, Multiple IFs, If-Elif-Else

#CHECK IF A NUMBER IS PRIME

#If-Else

#print('Enter a number to check if it is a even number: ')
number=int(input('Enter a number to check if it is a even number: '))  # Line number 11 - within the input function

# print(number/2,type(number/2))                                   # Result of division is float even though it is divisible

DataType_Result=number%2==0                                        # % - modulus - gives the remainder
                                                                   # DataType_Result contains a value of boolean data type

#print(2==2)                                                       # eg for getting boolean result from print function
print(DataType_Result)

if(str(DataType_Result)=='True'):                                  # str converts the data type to string
    print('It is an even number')
else:
    print('It is an odd number')


#CHECK DIVISIBILTY OF NUMBER BY 3 AND 5

number=int(input('Enter a number to check if it is divisible by both 3 and 5: '))
n3=number%3==0
n5=number%5==0

# Working of Multiple If conditions                                 # - evaluates all the if conditions and shows the output of all the satisfied conditions
if(n3==True):
    print(number,' is divisible by 3')
if(n5==True):
    print(number,' is divisible by 5')
if(n3==True and n5==False):
    print(number,' is divisible by 3 but not by 5')
if(n3==False and n5==True):
    print(number,' is divisible by 5 but not by 3')
if(n3==True and n5==True):
    print(number,' is divisible by both 3 and 5')
else:
    print(number,' is not divisible by both 3 and 5') 


#If-Elif-Else                                                       # - Evaluates and gives the output of one satisfied condition
print('if-elif')

if(n3==True and n5==True):
    print(number,' is divisible by both 3 & 5')
elif(n3==True and n5==False):
    print(number,' is divisible by 3 but not by 5')
elif(n3==False and n5==True):
    print(number,' is divisible by 5 but not by 3')
else:
    print(number,' is not divisible by both 3 and 5')

# CHECK IF A NUMBER IS ZERO, IF NOT STATE IF IT IS POSITIVE(ODD OR EVEN) OR NEGATIVE(ODD OR EVEN)

#Nested conditions

print('nested conditions')

if(number!=0):
    if(number%2==0):
        if(number>0):
#            print('{} is a positive odd number').__format__(str(number))       # format does not accept any other data type other than string and does not take any keyword arguements
             print(number,' is a positive odd number')
        else:
            print(number,' is a positive odd number')

        
    else:
        if(number<0):
            print(number,' is a negative even number')
        else:
            print(number,' is a negative odd number')
else:
    print('the number is ',number)

