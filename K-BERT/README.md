## 知乎专栏：

[here](https://zhuanlan.zhihu.com/p/101302240)

## 论文地址：

[here](https://arxiv.org/abs/1909.07606v1)

## 项目地址：

[here](https://github.com/autoliuweijie/K-BERT)

## K-BERT 引入知识进来

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
python run_kbert_ner.py --pretrained_model_path ./models/google_model.bin --config_path ./models/google_config.json  --vocab_path ./models/google_vocab.txt --train_path ./datasets/msra_ner/train.tsv --dev_path ./datasets/msra_ner/dev.tsv --test_path ./datasets/msra_ner/test.tsv --epochs_num 2 --batch_size 16 --kg_name CnDbpedia --output_model_path ./outputs/kbert_msraner_CnDbpedia.bin 


###  训练的过程如下所示：
```
Labels:  {'[PAD]': 0, '[ENT]': 1, 'O': 2, 'B-LOC': 3, 'I-LOC': 4, 'B-PER': 5, 'I-PER': 6, 'B-ORG': 7, 'I-ORG': 8}
Vocabulary file line 344 has bad format token
Vocabulary Size:  21128
[KnowledgeGraph] Loading spo from /workspace/K-BERT/brain/kgs/CnDbpedia.spo
Start training.
Batch size:  16
The number of training instances: 20864
/pytorch/torch/csrc/utils/python_arg_parser.cpp:756: UserWarning: This overload of add_ is deprecated:
	add_(Number alpha, Tensor other)
Consider using one of the following signatures instead:
	add_(Tensor other, *, Number alpha)
Epoch id: 1, Training steps: 100, Avg loss: 0.643
Epoch id: 1, Training steps: 200, Avg loss: 0.111
Epoch id: 1, Training steps: 300, Avg loss: 0.074
Epoch id: 1, Training steps: 400, Avg loss: 0.058
Epoch id: 1, Training steps: 500, Avg loss: 0.050
Epoch id: 1, Training steps: 600, Avg loss: 0.045
Epoch id: 1, Training steps: 700, Avg loss: 0.045
Epoch id: 1, Training steps: 800, Avg loss: 0.044
Epoch id: 1, Training steps: 900, Avg loss: 0.034
Epoch id: 1, Training steps: 1000, Avg loss: 0.038
Epoch id: 1, Training steps: 1100, Avg loss: 0.035
Epoch id: 1, Training steps: 1200, Avg loss: 0.029
Epoch id: 1, Training steps: 1300, Avg loss: 0.026
Start evaluate on dev dataset.
Report precision, recall, and f1:
0.947, 0.932, 0.940
Start evaluation on test dataset.
Batch size:  16
The number of test instances: 4636
Report precision, recall, and f1:
0.938, 0.931, 0.935
Epoch id: 2, Training steps: 100, Avg loss: 0.033
Epoch id: 2, Training steps: 200, Avg loss: 0.023
Epoch id: 2, Training steps: 300, Avg loss: 0.018
Epoch id: 2, Training steps: 400, Avg loss: 0.019
Epoch id: 2, Training steps: 500, Avg loss: 0.015
Epoch id: 2, Training steps: 600, Avg loss: 0.016
Epoch id: 2, Training steps: 700, Avg loss: 0.017
Epoch id: 2, Training steps: 800, Avg loss: 0.017
Epoch id: 2, Training steps: 900, Avg loss: 0.015
Epoch id: 2, Training steps: 1000, Avg loss: 0.018
Epoch id: 2, Training steps: 1100, Avg loss: 0.015
Epoch id: 2, Training steps: 1200, Avg loss: 0.014
Epoch id: 2, Training steps: 1300, Avg loss: 0.012
Start evaluate on dev dataset.
Report precision, recall, and f1:
0.950, 0.949, 0.950
Start evaluation on test dataset.
Batch size:  16
The number of test instances: 4636
Report precision, recall, and f1:
0.942, 0.949, 0.945
Final evaluation on test dataset.
Batch size:  16
The number of test instances: 4636
Report precision, recall, and f1:
0.942, 0.949, 0.945
```