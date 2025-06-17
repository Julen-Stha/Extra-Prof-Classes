def collatx(number):
    if number%2==0:
        n=number//2
        print(n)
        return n
    else:
        n=3*number+1
        print(n)
        return n


number = int(input("Enter a number:"))
if number!=0:
    condition = collatx(number)
    while condition!=1:
        condition= collatx(condition)
else:
    print("Nope")