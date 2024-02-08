## Homework

Question 1: What is the sum of the outputs of the generator for limit = 5?
A: 10.23433234744176
B: 7.892332347441762
C: 8.382332347441762
D: 9.123332347441762

**Answer 1: C: 8.382332347441762**
![image](https://github.com/garjita63/de-zoomcamp-2024-homework-workshop-data-ingestion/assets/77673886/b384c0e0-ffc4-47c6-9081-cd79094fd0ee)


Question 2: What is the 13th number yielded by the generator?
A: 4.236551275463989
B: 3.605551275463989
C: 2.345551275463989
D: 5.678551275463989

**Answer 2: B: 3.605551275463989**
![image](https://github.com/garjita63/de-zoomcamp-2024-homework-workshop-data-ingestion/assets/77673886/179ac2e1-20f2-45ac-95ab-e518a7214db8)


Question 3: Append the 2 generators. After correctly appending the data, calculate the sum of all ages of people.
A: 353
B: 365
C: 378
D: 390

**Answer 3: A: 353**
```
import dlt
import json

pipeline = dlt.pipeline(pipeline_name='person_append',
                        destination='duckdb',
                        dataset_name='person_append_dataset')

from typing import AsyncGenerator

## Data Dictionary 1
def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

people = ""
for person in people_1():
    person
    people = people + str(person) + ','

people = people[:-1]
people = '[' + people + ']'
people = people.replace("\'", "\"")
people = json.loads(people)

info = pipeline.run(people, table_name="person", write_disposition="replace")
print(info)

## Data Dictionary 2
def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

people = ""
for person in people_2():
    person
    people = people + str(person) + ','

people = people[:-1]
people = '[' + people + ']'
people = people.replace("\'", "\"")
people = json.loads(people)

info = pipeline.run(people, table_name="person", write_disposition="append")
print(info)
```
![image](https://github.com/garjita63/de-zoomcamp-2024-workshop-data-ingestion/assets/77673886/cf1ae869-bd4d-4ac6-a6d0-e253e3708979)

![image](https://github.com/garjita63/de-zoomcamp-2024-homework-workshop-data-ingestion/assets/77673886/8fa657c2-f741-43d6-b0b6-d723ca27f814)

![image](https://github.com/garjita63/de-zoomcamp-2024-homework-workshop-data-ingestion/assets/77673886/80f7a893-ca33-4ff0-9656-6c8526856edd)



Question 4: Merge the 2 generators using the ID column. Calculate the sum of ages of all the people loaded as described above.
A: 205
B: 213
C: 221
D: 230

**Answer 4:**
```
import dlt
import json

pipeline = dlt.pipeline(pipeline_name='person_merge',
                        destination='duckdb',
                        dataset_name='person_merge_dataset')

from typing import AsyncGenerator

## Data D(ictionary) 1
def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

people = ""
for person in people_1():
    person
    people = people + str(person) + ','
 
people = people[:-1]
people = '[' + people + ']'
people = people.replace("\'", "\"")
people = json.loads(people) 

info = pipeline.run(people, table_name="person", write_disposition="replace")
print(info)   

## Data (Dictionary) 2

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

people = ""
for person in people_2():
    person
    people = people + str(person) + ','

people = people[:-1]
people = '[' + people + ']'
people = people.replace("\'", "\"")
people = json.loads(people) 

info = pipeline.run(people, table_name="person", write_disposition="merge", primary_key="ID")
print(info)   
```
![image](https://github.com/garjita63/de-zoomcamp-2024-homework-workshop-data-ingestion/assets/77673886/f26afce3-bbb8-4416-a741-b7317a828449)

![image](https://github.com/garjita63/de-zoomcamp-2024-homework-workshop-data-ingestion/assets/77673886/f912dd3e-731c-4e7f-8378-6ec48b2f3dcc)

![image](https://github.com/garjita63/de-zoomcamp-2024-homework-workshop-data-ingestion/assets/77673886/5379a33b-05ec-401e-9e20-875fb4dbcce9)

