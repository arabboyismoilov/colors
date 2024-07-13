oddiy = list(range(10))
list1 = oddiy[7:]
list2 = oddiy[:7]
list1.extend(list2)

dict1 = {}
for i in range(len(oddiy)):
    dict1.update({oddiy[i]:list1[i]})

son = input("son kirit: ")

yangi_son = ""
for i in son:
    yangi_son += str(dict1[int(i)])

print(yangi_son)


