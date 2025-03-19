import json
from pathlib import Path
from tqdm import tqdm

json_folder = Path("jfk_json")
output_text = Path("summaries.txt")
output_fn = Path("filenames.txt")

with open(output_fn, 'w', encoding='utf-8') as ffn:
    with open(output_text, 'w', encoding='utf-8') as ftext:
        for json_file in tqdm(sorted(json_folder.glob("*.json")), desc="Processing JSON files"):
            print(json_file.stem, file=ffn)
            with open(json_file, 'r', encoding='utf-8') as fjson:
                data = json.load(fjson)
            print(data["summary"].strip(), file=ftext)
