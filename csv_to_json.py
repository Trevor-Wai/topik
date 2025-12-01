import csv
import json

csv_file = 'vocab.csv'
json_file = 'vocab.json'

data = []
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 2:
            data.append({"korean": row[0], "chinese": row[1]})

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Converted {csv_file} to {json_file}")
