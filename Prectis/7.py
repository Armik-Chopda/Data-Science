li1=[1,2,3,4,5,6,7,8,2]
li2=[1,2,3,4,5,6,7,8]
if len(li1)==len(li2):
    print("same length")
elif len(li1)>len(li2):
    print("List one is big")
else:
    print("List two is big")
li3=["armik"]
f=True
for i in li3:
    if type(i) is str:
        continue
    else:
        f=False
        break

if not f:
    print("contains not only strings")
else:
    print("contains only strings")       
