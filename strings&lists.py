# strings

s= 'this is a string stored in a variable "s"'
t= '''this is also a string continued
in the next line'''
u= 'this is also a string continued \nin the next line'
u=u+'s'; print(u)
u=u.removesuffix('lines')                                  # u=u[:len(u)-1] checks the string from the suffix and removes, if present
print(s,'\n',t,'\n',u)
print(u[0:7],u[13:21],'by slicing')
print(len(s),'\n',len(t),'\n',len(u))
print(s[1])


# lists - all the items in a list not necessary to be of same data type, lists are mutable

list = [1,2,3.0,'four']
list[0]=1.0
print(list[0])
print(list[3:1:-1])
list.insert(2,2.5)
print(list)
print(list.count('four'))
print(list.index('four'))
print(list.pop(0))
#print(list.sort())
#print(list.remove())

