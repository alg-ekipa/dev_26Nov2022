import json



try:
    with open("  Link   ") as file_reader:
        dict_json = json.load(file_reader)
    
except Exception as e:
    print(f"Pogreška {e}")

print(dict_json)

ime = dict_json["shipTo"]["name"]
ulica = dict_json["shipTo"]["address"]
grad = dict_json["shipTo"]["stay"]

