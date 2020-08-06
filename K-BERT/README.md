# 知乎专栏：

[here](https://zhuanlan.zhihu.com/p/101302240)

# 论文地址：

[here](https://arxiv.org/abs/1909.07606v1)

# 项目地址：

[here](https://github.com/autoliuweijie/K-BERT)

# K-BERT 引入知识进来


### NER example

Run an example on the msra_ner dataset with CnDbpedia:

```
CUDA_VISIBLE_DEVICES='0' nohup python3 -u run_kbert_ner.py \
    --pretrained_model_path ./models/google_model.bin \
    --config_path ./models/google_config.json \
    --vocab_path ./models/google_vocab.txt \
    --train_path ./datasets/msra_ner/train.tsv \
    --dev_path ./datasets/msra_ner/dev.tsv \
    --test_path ./datasets/msra_ner/test.tsv \
    --epochs_num 5 --batch_size 16 --kg_name CnDbpedia \
    --output_model_path ./outputs/kbert_msraner_CnDbpedia.bin \
    > ./outputs/kbert_msraner_CnDbpedia.log &
```