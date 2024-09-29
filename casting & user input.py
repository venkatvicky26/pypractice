# casting = converting one data type into another data type

a=int('10')
b=int("20")
print(a+b)

# user input 

print('enter value for a')
a=int(input())             # input() prompts for user input at this line
print('enter value for b')
b=int(input())
print('addition of a & b =',a+b)

# user input & casting exercise
# input - Name, Department, Score
# output - 
# My name is venkat
# My department is Mechanical_BI
# My score is 7.8/10

print('Enter you name','\n','Name:')
Name=input()
print('Enter you Department','\n','Department:')
Department=input()
print('Enter you Score','\n','Score:')
Score=int(input())

print('My name is ', Name)
print('My department is ',Department)
print('My score is ',Score/10,'/10')
