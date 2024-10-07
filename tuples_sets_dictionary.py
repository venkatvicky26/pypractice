# TUPLES
#################################
# tuples are same as lists which can have any type of data but cannot be modified, added or deleted

x=['a','b','c']
a=(1,'1','two',x,'1')
print(x,a)
print(a.count('1'))
print(a.index(1))
# casting tuple into list is possible
print(type(list(a)),a,list(a),sep='|')


# SETS
#################################
# sets are same as list - can contain any data type, values can be added and removed 
# but cannot be modified and are always unordered
# mainly it does not allow duplicates

s={1,2,3,'a','b','c','d','c'}
print(s)                # will not allow duplicates 'c'
x=['a','b','c']
a=[1,'x','y','z','x']           
print(s)
s.union(a)              # cannot union with nested datastructures like list of lists, # try with variable x instead of 'x' for union
print(s)
for i in range(len(s)):
    s={1,2,4,'a','x','y','z'}
    s.pop()                    # values can be poped but it pops in a random manner
    print(s)

