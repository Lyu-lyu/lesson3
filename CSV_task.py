 
developers = [
{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
{'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
{'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]
import csv 

with open ('userdata.csv', 'w', encoding = 'utf-8', newline = '') as f:
    fields = ['name', 'job', 'age']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for person in developers:
        writer.writerow(person)
