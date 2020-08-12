# coding:utf-8
def load(vocab_path, is_quiet=False):
    w2i = {}
    i2w = []
    w2c = {}
    with open(vocab_path, mode="r", encoding="utf-8") as reader:
        for index, line in enumerate(reader):
            try:
                w = line.strip().split()[0]
                w2i[w] = index
                i2w.append(w)
            except:
                w2i["???" + str(index)] = index
                i2w.append("???" + str(index))
                if not is_quiet:
                    print("Vocabulary file line " + str(index + 1) + " has bad format token")
        assert len(w2i) == len(i2w)
    print(w2i)
    print(i2w)

vocab_path = 'google_vocab.txt'
load(vocab_path)
