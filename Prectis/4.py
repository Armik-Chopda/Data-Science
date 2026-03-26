d={"id":1,"name":"armik","email":"armikchpod@gamil.com","location":"surat"}
in1=input("Enter key = ")
x=False
for i in d.keys():
    if in1==i:
        print(" yes your key is found in the dict")
        x=True
        break
if not x:
    print("not found your key in the dict")


    