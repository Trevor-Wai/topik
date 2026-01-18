import csv
import json

csv_file = 'vocab1.csv'
json_file = 'vocab1.json'

data = []
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 4:
            data.append({"korean": row[0], "chinese": row[1], "explanation": row[2], "pos": row[3]})

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Converted {csv_file} to {json_file}")
