import json

tekst_json = 

try:
    with open("  Link  ") as file_reader:
        tekst_json = file_reader.read()

except Exception as e:
    print(f"Pogreška {e}")


dict_json = json.loads(tekst_json)
print(dict_json)

dict_json = {}

try:
    with open("  Link   ") as file_reader:
        dict_json = json.load(file_reader)
    
except Exception as e:
    print(f"Pogreška {e}")

print(dict_json)