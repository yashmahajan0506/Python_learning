#reading csv files:- 
import csv 

with open("my_data.csv","r") as file:
    reader=csv.reader(file)
    for i in reader:
     print(i)
     
with open("my_data.csv","r") as file:
    reader=csv.DictReader(file)
    for i in reader:
     print(i['Name'],i['Age'])
     
# for writing :-  


with open('employee.csv','w') as file:
    writer=csv.writer(file)
    writer.writerow(['id','name','age','city'])
    writer.writerow([1,'yash',20,'Ahm'])

with open('employee.csv','r') as file:
    reader=csv.reader(file)
    for i in reader:
        print(i)

# with open('employee.csv', mode='w', newline='') as file:
#     fieldnames = ['id', 'name', 'age', 'city']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': 2, 'name': 'aju', 'age': 22, 'city': 'Surat'})


# with open('employee.csv','r') as file:
#     reader=csv.reader(file)
#     for i in reader:
#         print(i)


with open('employee.csv','w') as file:
    fieldnames=['id','name','age','city']
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':3,'name':'yash','age':20,'city':'ahm'})
    

with open('employee.csv','a') as file:
    writer=csv.writer(file)
    writer.writerow([4,'sujal',21,'punjab'])