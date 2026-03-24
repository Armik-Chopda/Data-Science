name=['armik',23,56,'vasu','meet',55,667.0,'krishna',54,99,'hit','prince']
new=[]
values=[]
for i in name:
    if type(i) == int or type(i)==float:
        values.append(i)
    if type(i)==str:
        new.append(i.upper())
print(new)
print(values)