import json
from pathlib import Path

url = "https://github.com/7shi/jfk_files/blob/misc/jfk_text/%s.md"

summaries = {}

with open("summaries-ja.txt", 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f]

it = iter(lines)
json_folder = Path("jfk_json")
for json_file in sorted(json_folder.glob("*.json")):
    with open(json_file, 'r', encoding='utf-8') as fjson:
        data = json.load(fjson)
    summaries[json_file.stem] = (data["summary"], next(it))

while True:
    try:
        search = input("Enter a search term: ")
        if not search:
            break
        for key, (en, ja) in summaries.items():
            if en.startswith(search):
                print(f"> {ja}[{key}]({url % key})")
    except EOFError:
        break
