import json
from pathlib import Path

json_folder = Path("../jfk_json")
json_schema = "../schema.json"
output_tsv = Path("summaries.tsv")

with open(json_schema, 'r', encoding='utf-8') as f:
    schema = json.load(f)

arrays = {}

with open(output_tsv, 'w', encoding='utf-8') as f:
    columns = ["filename"]
    for k1, value in schema["properties"].items():
        if value["type"] == "array":
            arrays[k1] = {}
        else:
            columns.append(k1)
    print(*columns, sep="\t", file=f)
    for json_file in sorted(json_folder.glob("*.json")):
        with open(json_file, 'r', encoding='utf-8') as fjson:
            data = json.load(fjson)
        items = [json_file.stem]
        for k1, value in schema["properties"].items():
            if value["type"] == "array":
                dict = arrays[k1]
                for item in data.get(k1, []):
                    dict.setdefault(item, []).append(json_file.stem)
            else:
                items.append(data.get(k1, "").replace("\r\n", "\n").replace("\n", " ").replace("\r", " "))
        print(*items, sep="\t", file=f)

for k1, v1 in arrays.items():
    with open(f"{output_tsv.stem}-{k1}.tsv", 'w', encoding='utf-8') as f:
        print(k1, "filename", sep="\t", file=f)
        for k2 in sorted(v1):
            v2 = v1[k2]
            for filename in v2:
                print(k2, filename, sep="\t", file=f)
