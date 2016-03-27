x = input("enter the range up to which calculate:  ")
print ("")
a=0
b=1
print(a)
print(b)
x= int(x)
num= 0
while num<=x :
    ans = a+b
    print(ans)
    a=b
    b=ans
    num += 1