import json
# Input Names
names = [name.upper() for name in input().split()]

# Check for The storage File
try: # If found then load JSSON data
    with open("student_dataset.json","r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError): # else Create a New JSON data
    data = {"Students":{},
            "total_days":0}

# Increment the number of working Days
data ["total_days"] += 1
total_days = data["total_days"]

# Extract names from the list and marks the atttendance accordingly
students = data["Students"]
for name in names:
     if name not in students:
        students[name]={"Present":0,
                         "Absent":0 }
        
     data["Students"][name]["Present"]+=1
     data["Students"][name]["Absent"]=data["total_days"]-data["Students"][name]["Present"]

# Relode the updated data back to JSON
with open("student_dataset.json","w") as f:
    json.dump(data, f, indent=4)

print("Attendance updated Succesfully")