import json

python_object = {
"name": "John",
"age": 30,
"city": "New York"
}


class jsonp():
    id:int  
    name:str 
    title:str 
    author :str 
    

j = jsonp()
j.id = 2
j.author = "C"
j.name = "eslam"
j.title = "hhh"

jdict = j.
print(jdict)
json_string = json.dumps(jdict)

# Print JSON string
print(json_string)  # Output: {"name": "John", "age": 30, "city": "New York"}
