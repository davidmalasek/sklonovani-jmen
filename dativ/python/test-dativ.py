from dativ import dativ
import json
import os

root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
names_json_path = os.path.join(root_folder, "test", "names.json")

with open(names_json_path, "r") as file:
    data = json.load(file)
    names = data["names"]

print("-Komu, čemu?-")
for name in names:
    print(dativ(name) + " (" + name + ")")
print("-Komu, čemu?-")
