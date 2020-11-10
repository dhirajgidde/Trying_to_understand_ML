
print("hellow WOrld")

print("Welocome to python")

num=10
print("The variable",num)
print("The Varialbe {} is great".format(num))
tejas="Tajas"
tejas='''dsad
dsadasd'''
tejas=10
flt=10.4
bol=True
print(type(tejas))

#Single line comment
'''
dsadsad

dsadsa
d
ad
sd
'''

#Arithmetic Operations

a=10
b=30

print(a+b)
print(a/b)
print(a//b)
print(a**b)

#Conditional Operators

if a<b and b==30:
    n=10
    print("A is a largest number")
    if a==25:
        print("we are in nested if")
elif b>a:
    print("B is greater")
else:
    print("Both are equals")

#Data Structure

#list
lst=[1,2,3,4,"String",'c',10.4]

print(lst[1:6:2])
print(lst[::-1])
print(lst[0]-lst[1])
lst.insert(2,"Tejas")
print(lst)
lst.append(123)
print(lst)
lst.pop()
print(lst)
#lst.reverse()
print(lst)
lst.remove(1)
print(lst)
lst.clear()
print(lst)

