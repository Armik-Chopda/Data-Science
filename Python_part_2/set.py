#set
# set is a collaction of Unordered Unique values

set1={22,45,34,67,67,34,22,87}  
print(set1)
# output is {34, 67, 22, 87, 45}
print(len(set1))
print(22 in set1)
 

set2=set("abcdefghijk")
set3=set("aeiou")
print(set2) 
print(set3)
print(set2-set3)
print(set2|set3)#Union -use for all elements one time
print(set2 & set3)#intersection - use for common elements
print(set2^set3)# - use for not common elements