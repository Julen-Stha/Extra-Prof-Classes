def collatx(number:int):
    '''
    function to calculate the collatz sequence

    args:
        number(int): any integer number

        return:
            res(int): result of the collatz sequence
    '''
    if number%2==0:
        n=number//2
        print(n)
        return n
    else:
        n=3*number+1
        print(n)
        return n

looping = True
while looping:
    try:
        number = int(input("Enter a number:"))
        looping = False
        if number!=0:
            condition = collatx(number)
            while condition!=1:
                condition= collatx(condition)
        else:
            print("Nope")
    except Exception as e:
        print(f"exception {e}")
