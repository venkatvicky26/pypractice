

##########################################

n = int(input())
i=0
while i<n:
    print(i*i)
    i+=1

###########################################

s='hello world'
s=s.split(' ')
for i in range(len(s)):
    s[i]=s[i].capitalize()
print(' '.join(s))

##########################################

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
