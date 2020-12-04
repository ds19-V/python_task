#Create a JSON of all object types and import the JSON into a SQL Database
import json
#dictionary
print(json.dumps({"Name":"DEEPASREE","doe":19}))
#list
print(json.dumps(["BTS","KOREAN"]))
#string
print(json.dumps(("V","JIMIN")))
#tuple
print(json.dumps("ds19_v"))
#integer
print(json.dumps(33))
#float
print(json.dumps(10.1))
#True
print(json.dumps(True))
#False
print(json.dumps(False))
#None
print(json.dumps(None))

