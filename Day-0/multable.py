def table(n):
    for x in range(1,11):
        print(f'{n} * {x} = {n*x}')

data = int(input("Enter a number:"))
table(data)