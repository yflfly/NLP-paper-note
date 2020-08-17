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
'''
输出结果为：
{'[PAD]': 0, '[ENT]': 1, 'O': 2, 'B-LOC': 3, 'I-LOC': 4, 'B-PER': 5, 'I-PER': 6, 'B-ORG': 7, 'I-ORG': 8}
****************************************************************************************************
[3, 5, 7]
'''

with open('1.txt', encoding='utf-8') as fp:
    for line in fp.readlines():
        line = line.strip()
        if line == '':
            continue
        print(len(line.split()))
