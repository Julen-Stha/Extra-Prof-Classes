list1 = []
for x in range(5):
    list1.append(x)
    print(list1[x])


list2=[i for i in range(5)]
print(list2)

list3 = [i for i in range(5) if i%2==0]
print(list3)


dict1 = {i: i * i for i in range(5) if i%2==0}
print(dict1)
