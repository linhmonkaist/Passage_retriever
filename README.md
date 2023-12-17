# Advanced Passage Retrieval with Lexical and Semantic Matching

The directory structure is as follows:

```
├── Bi-encoder Cross-encoder
│   ├── Dataset
│   ├── bm25_vs_bi-crossencoder.ipynb
├── Finetuning Bi-encoder Cross-encoder
│   ├── Preprocessed Data
│   ├── cross_encoder_test.ipynb
│   ├── cross_encoder_train.ipynb
├────── DPR_+_BM25_for_SQuAD.ipynb
```

- `bm25_vs_bi-crossencoder.ipynb` is for directly applying a pretrained bi-encoder model and a pretrained cross-encoder model for passage retrieval.
- `cross_encoder_test.ipynb` is for quantitative and qualitative evaluation of a given cross-encoder model
- `cross_encoder_train.ipynb` is for training a cross-encoder model
- `DPR_+_BM25_for_SQuAD.ipynb` is for applying DPR + BM25 hybrid architecture for passage retrieval

Trained models are stored in this [drive](https://drive.google.com/drive/folders/1FcI9a0CVpFs8Z9QIpGk-flYnN4HcMKiS?usp=sharing).
