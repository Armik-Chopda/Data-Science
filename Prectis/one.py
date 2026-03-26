# 1. Check if a list is empty.

li=[]
if not li:
    print('list is empty')

# 2. Check if a given element exists in a list.
l1=[1,2,3,4,5,6,7,3,2,6,"armik"]
el=input("enter element")
found=False
for i in l1:
    if str(i)==el:
        print("Element is found")
        found=True
        break
if not found:
    print("element not found")


    

   





