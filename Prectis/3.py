st=input("enter string = ")
t=(1,2,3,"armik","chopda",[1,2,3,4,5],"dhruv")
t2=(1,2,3,"armik","chopda",[1,2,3,4,5],"dhruv")
exists=False
for i in t:
    if i==st:
        print(" yes String is exists in tuple")
        exists=True
        break
if exists==False:
    print("No String is not exists in tuple")
    
if t==t2:
    print("yes")
else:
    print("no")
ind=int(input("enter index number = "))
if ind==(-len(t)) and ind<len(t):
    print(t[ind])
else:
    print("invalid index number ")