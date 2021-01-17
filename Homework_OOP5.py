import json
import yaml

data = {}
data["Place"] = ['Armenia', 'Tavush']
data ["Monastery"] = ["Haghartsin Monastery", "Makaravank Monastery"]
data["Park"] = ["Dilijan National Park", "Ijevan Dendropark"]
data["Lake"] = ["Lake Parz"]
data ["Location_chek"] = [True]
with open ("mydata.json","w") as f:
	json.dump(data, f)
	
with open("mydata.json") as json_file:
	data = json.load(json_file)

#json to txt #1
with open("json_to_txt.txt", "w") as w:
	t1 = json.dump(data,w)


# #json to yaml #2

with open("json_to_yaml.yaml","w") as file:
	new_item = ["for yaml", 12, 0.52, 655, True] 
	d = yaml.dump(data,file)
	d = yaml.dump(new_item, file)

with open("json_to_yaml.yaml") as new:
	yaml_data = yaml.full_load(new)

#yaml to json #3

with open("yaml_to_json.json", "w") as file1:
	j = json.dump(yaml_data,file1)

#yaml to txt #4
with open("yaml_to_text.txt","w") as file2:
	t = yaml.dump(yaml_data,file2)
	


