def fact(n):
    if n==0:
        return 1
    else:
        output=1
        for x in range(1,n+1):
            output *= x
        return output

data=int(input("Enter a number:"))
x=fact(data)
print(x)