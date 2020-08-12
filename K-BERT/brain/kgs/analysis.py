# coding:utf-8
spo_path = 'CnDbpedia.spo'
lookup_table = {}
with open(spo_path, 'r', encoding='utf-8') as f:
    tag = 0
    for line in f:
        tag += 1
        try:
            print(line)
            subj, pred, obje = line.strip().split("\t")
            # print(subj, '*', pred, '*', obje)
        except:
            print("[KnowledgeGraph] Bad spo:", line)
        # if self.predicate:
        #     value = pred + obje
        # else:
        #     value = obje
        value = pred + obje
        if subj in lookup_table.keys():
            lookup_table[subj].add(value)
        else:
            lookup_table[subj] = set([value])
        print(lookup_table)
        print('*' * 100)

        if tag > 5:
            break
