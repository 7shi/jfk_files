import os, json
from glob import glob
from pathlib import Path

json_dir = "../jfk_json"
summaries = {}
for json_file in glob(f"{json_dir}/*.json"):
    with open(json_file, "r", encoding="utf-8") as f:
        summaries[Path(json_file).stem] = json.load(f)

with open("schema.json", "r", encoding="utf-8") as f:
    schema = json.load(f)
with open("filenames.txt", "r", encoding="utf-8") as f:
    filenames = [line.strip() for line in f]
with open("summaries-title-ja.txt", "r", encoding="utf-8") as f:
    titles_ja = [line.strip() for line in f]
with open("summaries-ja.txt", "r", encoding="utf-8") as f:
    summaries_ja = [line.strip() for line in f]

properties = schema["properties"]
props = ["title", "title_ja", "summary", "summary_ja"]
for key in properties:
    if key not in props:
        props.append(key)

for i, filename in enumerate(filenames):
    data = summaries[filename]
    new_data = {}
    for key in props:
        if key == "title_ja":
            new_data[key] = titles_ja[i]
        elif key == "summary_ja":
            new_data[key] = summaries_ja[i]
        elif key in data:
            new_data[key] = data.pop(key)
    if data:
        raise ValueError(f"Unexpected keys in {filename}: {data.keys()}")
    with open(f"{json_dir}/{filename}.json", "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)
