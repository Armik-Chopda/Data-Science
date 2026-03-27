class data:
    def syllabus(self):
        print("this is my data_science syllabus")
class web:
    def syllabus(self):
        print("this is my web syllabus")

def class_parcer(data):
    for i in data:
        i.syllabus()
data=data()
web=web()
li=[data,web]
print(class_parcer(li))
