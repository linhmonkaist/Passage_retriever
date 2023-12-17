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

- `bm25_vs_bi-crossencoder.ipynb`[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/10I5u8GMN_l7ULDBHo6EGxH3z4wbmzTv-/view?usp=drive_link) is for directly applying a pretrained bi-encoder model and a pretrained cross-encoder model for passage retrieval.
- `cross_encoder_test.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OOSHiEXT7CR0dnQO8b-y3G-cVy7Z053i?usp=drive_link) is for quantitative and qualitative evaluation of a given cross-encoder model
- `cross_encoder_train.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/14po8ii62nx8OSCHrMtIv0xypWp3SWuC5?usp=sharing) is for training a cross-encoder model
- `DPR_+_BM25_for_SQuAD.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qN4NseeVi0Do0AhZPv6J34derXY97gfR?usp=sharing) is for applying DPR + BM25 hybrid architecture for passage retrieval

Trained models are stored in this [drive](https://drive.google.com/drive/folders/1FcI9a0CVpFs8Z9QIpGk-flYnN4HcMKiS?usp=sharing).
