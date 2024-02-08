import dlt
import json

pipeline = dlt.pipeline(pipeline_name='person_append',
                        destination='duckdb',
                        dataset_name='person_append_dataset')

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

info = pipeline.run(people, table_name="person")
print(info)   
