#1
list1 = [i for i in range (2,21,2)]
print(list1)

#2
list2 = {x :x*x*x for x in range(6)}
print(list2)


#3
list3 = ["apple","banana","apple"]
set1={x[0] for x in list3}
print(set1)

set3 = { x[y] for x in list3 for y in range(len(x))}
print(set3)