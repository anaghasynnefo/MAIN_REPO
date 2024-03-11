list = [1,2,3,2,4,5,5,6,7,8,8,9,3]
print("The original list is : " + str(list))
result = []

for i in list:
    if i not in result:
        result.append(i)
 
print("list after removing duplicates : " + str(result))