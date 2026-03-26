t=(1,2,-3,4,5,4,3,4,5,4,3,22,2,9,3,4,5,5,5)
x=True
for i in t:
    if i<0:
        x=False
if not x:
    print("Not All Value is positive")  
else:
    print("All value is positive")
