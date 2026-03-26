di=[{"id":1,"age":12,'name':"armik"},
    {"id":2,"age":2,'name':"armik"},
    {"id":3,"age":10,'name':"armik"},
    {"id":4,"age":15,'name':"armik"},
    {"id":5,"age":8,'name':"armik"},
    {"id":6,"age":16,'name':"armik"},
    {"id":7,"age":6,'name':"armik"},
    {"id":8,"age":14,'name':"armik"}]
l=[]
for i in di:
    if i['age']>10:
        l.append(i["age"])
        print(i)
if len(l)!=len(di):
    print("Not values are greater than 10")
else:
    print(" all dictionary values are greater than 10 ")  

# flag = True

# for i in di:
#     if i['age'] <= 10:
#         flag = False
#         break

# if flag:
#     print("All values are greater than 10")
# else:
#     print("Not all values are greater than 10")        