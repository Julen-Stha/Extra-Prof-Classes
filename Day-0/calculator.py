def calculator(a,b,operator):
    if operator == '+':
        return (a+b)
    elif operator =='-':
        return (a-b)
    elif operator =='*':
        return (a*b)
    elif operator =='/':
        return (a/b)
    else:
        print("Wrong operator")
while True:
    data1=int(input("Enter first number:"))
    data2=int(input("Enter second number:"))
    op= input("Enter operator:")
    result = calculator(data1,data2,op)
    print(f'Result of {data1} {op} {data2} = {result}')
    again = input("Do you want to process another number?")
    if again=="NO":
        break