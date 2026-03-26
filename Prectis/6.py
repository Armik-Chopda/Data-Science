s=(1,"ar",{"id":7},[1,3,6])
s1=(1,"ar",{"id":7},[1,3,6],2)
if not s:
    print("yes")
else:
    print("not")
if s==s1:
    print("equal")
else:
    print(" not equal")

l={2,5,7,4,3,5,6,8,9,0,2,1,2,12,78,88,99} 
l2={2,5,7,4,3,5,6,12,88,3,99}
# l3=l-l2
# l4=l-l3
# if l4==l2:
#     print("subset")

# else:
#     print("not")
if l2.issubset(l):
    print("yes")
else:
    print("not")
if l.issuperset(l2):
    print("yes")
else:
    print("no")            