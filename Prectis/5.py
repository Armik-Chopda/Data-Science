d={"id":1,"name":"armik","email":"armikchpod@gamil.com","location":"surat"}
d2={"id":1,"name":"armik","email":"armikchpod@gamil.com","location":"surat"}
x=input("enter value ")
kys=[]
val=[]
for i,j in d.items():
    val.append(j)
if x in val:
    print("yes")
else:
    print("no")
if d==d2:
    print("dictionaries for equality")
