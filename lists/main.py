list1=[1,2,3,4,5]
list1.append(1)
print(list1)

list1.extend([2,3,4])
print(list1)

list1.insert(1,5)
print(list1)

list1.pop()
print(list1)

list1.remove(5)
print(list1)

#list1.clear()
#print(list1)

i=0
while i<len(list1):
    print(list1[i])
    i+=1

