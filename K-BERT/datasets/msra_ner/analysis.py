# coding:utf-8

labels_map = {"[PAD]": 0, "[ENT]": 1}
begin_ids = []

# Find tagging labels
with open('train.tsv', mode="r", encoding="utf-8") as f:
    for line_id, line in enumerate(f):
        if line_id == 0:
            continue
        labels = line.strip().split("\t")[1].split()
        for l in labels:
            if l not in labels_map:
                if l.startswith("B") or l.startswith("S"):
                    begin_ids.append(len(labels_map))
                labels_map[l] = len(labels_map)
print(labels_map)
print('*' * 100)
print(begin_ids)
