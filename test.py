
#######################################################        
# names and scores of the student is stored as a lists of list
# print the names of the students in a sorted manner of the second lowest score 


''' 
list=[]
scores=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    listi=[name,score]
    list.append(listi)
    scores.append(score)    
list2=[x for x in list if x[1]!=min(scores)]
#print(list2)
scores=[s for s in scores if s!=min(scores)]
list3=[y for y in list2 if y[1]==min(scores)]
#print(list2)
listnames=[]
for i in list3:
    listnames.append(i[0])
listnames.sort()
for i in listnames:
    print(i,end='\n')
'''

# optimised version

list=[]
scores=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    listi=[name,score]
    list.append(listi)
    scores.append(score)
list2=[x for x in list if x[1]!=min(scores)]
scores=[s for s in scores if s!=min(scores)]
listnames=[y[0] for y in list2 if y[1]==min(scores)]
listnames.sort()
for j in listnames:
    print(j,end='\n')
###################################################################
#  Get list of number of inputs and print the second largest number


n = int(input())
arr = list(map(int, input().split()))
#arr.remove(max(arr))                     # removes only once occurence of the max value
#print(max(arr))
list=[x for x in arr if x != max(arr)]    # removes all the occurence of max value
print(max(list))
###########################################
# 

n = int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
#       arr.append(map(int, input().split()))
arr.remove(max(arr))
print(max(arr))
##########################################
# Square of natural numbers till the input


n = int(input())
i=0
while i<n:
    print(i*i)
    i+=1
###########################################
# Capitalize the first letter of first and last name 


s='hello world'
s=s.split(' ')
for i in range(len(s)):
    s[i]=s[i].capitalize()
print(' '.join(s))
##########################################
# Prime number if not prompt for factors


n=int(input('Enter a number to check if it is prime: '))
i=2
C='N'
factors=[]
while i < n:
    if C=='N':
        if(n%i==0):
            print('{} is divisible by {}. Hence, '.format(n,i),'it is not a prime number.')
            c=input('Do you want the number of factors of {}? Y/N? '.format(n))
            if c=='y' or c=='Y':
                C='Y'; factors=[i]
            else:
                break
        i+=1
    else:
        if(n%i==0):
            factors.append(i)
            i+=1 
        else:
            i+=1
            continue
       
            
else:
    if len(factors)<1:
        print(n,' is  a prime number.')
    else:
        print(factors)
