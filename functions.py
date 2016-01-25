def fibonacci(x):
    a = 0
    b = 1
    print(a)
    print(b)
    x=int(x)
    count = 0
    while count <= x:
        ans = a+b
        print (ans)
        a = b
        b = ans
        count += 1
