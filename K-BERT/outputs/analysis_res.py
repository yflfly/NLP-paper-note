# coding:utf-8
'''
对输出的结果进行整理
'''

pred = []
gold = []
with open('pred_label.txt', encoding='utf-8') as fp:
    for line in fp.readlines():
        line = line.strip()
        if line == '':
            continue
        if line.startswith('pred:'):
            line = line.split('pred:')[-1]
            pred.append(line)
        if line.startswith('gold:'):
            line = line.split('gold:')[-1]
            gold.append(line)

for i in range(len(pred)):
    pred_linshi = []
    linshi = pred[i].split()
    for each in linshi:
        if each != '[ENT]':
            pred_linshi.append(each)

    gold_linshi = []
    linshi = gold[i].split()
    for each in linshi:
        if each not in ['[ENT]', '[PAD]']:
            gold_linshi.append(each)
    pred_linshi = pred_linshi[:len(gold_linshi)]

    pred[i] = ' '.join(pred_linshi)
    gold[i] = ' '.join(gold_linshi)

# text_a	label
text = []
with open('test.tsv', encoding='utf-8') as fp:
    for line in fp.readlines():
        line = line.strip()
        if line == '' or line == 'text_a	label':
            continue
        line = line.split('\t')
        text.append(line[0])

print(len(pred), len(gold), len(text))

with open('text_gold_pred.txt', 'w', encoding='utf-8') as fw:
    fw.write('text\tgold\tpred\n')
    for i in range(len(pred)):
        pred_l = pred[i].split()
        gold_l = gold[i].split()
        text_l = text[i].split()
        for j in range(len(pred_l)):
            fw.write(text_l[j] + '\t' + gold_l[j] + '\t' + pred_l[j] + '\n')
        fw.write('\n')
