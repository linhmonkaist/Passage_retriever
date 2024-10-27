# Advanced Passage Retrieval with Lexical and Semantic Matching

### Description

Passage retrieval is the task of extracting top-k pertinent passages from a dataset as the output given a query, the input. In this research, we use the [BM25 model](https://link.springer.com/referenceworkentry/10.1007/978-0-387-39940-9_921) as a benchmark to explore other models that can achieve better accuracy specifically on the [SQuAD1.1 dataset](https://github.com/rajpurkar/SQuAD-explorer).

In this research, we implement three hybrid methods.

1. Deep Passage Retrieval (DPR) and BM25
2. Bi-encoder retriever and cross-encoder reranker
3. Bi-encoder retriever and fine-tuned cross-encoder reranker
   - Simple fine-tuning
   - Fine-tuning with BM25 scores injection

Comprehensive description of each of the methods and results thereof are presented in our [paper](https://drive.google.com/file/d/1MG5lgEXaPG-2ZvSZrDpCjrI7fGljnY2b/view?usp=drive_link).

### Directory Structure

The directory structure is as follows:

```
├── Bi-encoder Cross-encoder
│   ├── Dataset
│   ├── bm25_vs_bi-crossencoder.ipynb
├── Finetuning Bi-encoder Cross-encoder
│   ├── Preprocessed Data
│   ├── cross_encoder_test.ipynb
│   ├── cross_encoder_train.ipynb
├────── BM25_eval.ipynb
├────── DPR_+_BM25_for_SQuAD.ipynb

```

- `bm25_vs_bi-crossencoder.ipynb`[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/10I5u8GMN_l7ULDBHo6EGxH3z4wbmzTv-/view?usp=drive_link) is for directly applying a pretrained bi-encoder model and a pretrained cross-encoder model for passage retrieval.
- `cross_encoder_test.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OOSHiEXT7CR0dnQO8b-y3G-cVy7Z053i?usp=drive_link) is for quantitative and qualitative evaluation of a given cross-encoder model.
- `cross_encoder_train.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/14po8ii62nx8OSCHrMtIv0xypWp3SWuC5?usp=sharing) is for training a cross-encoder model.
- `BM25_eval.ipynb`[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dbci2BjkW4tzCuZ90x0KMBAbtNk286g_?usp=drive_link) is for evaluating the performance of BM25 and generating BM25 scores to select negative examples as well as to be directly used in hybrid architectures.
- `DPR_+_BM25_for_SQuAD.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qN4NseeVi0Do0AhZPv6J34derXY97gfR?usp=sharing) is for applying DPR + BM25 hybrid architecture for passage retrieval.

### Trained Models

Trained models can be accessible from this [drive](https://drive.google.com/drive/folders/1FcI9a0CVpFs8Z9QIpGk-flYnN4HcMKiS?usp=sharing).

| Model                  | Filename                           | Method                                       | `warmup_steps` | pos-neg ratio |
| :--------------------- | :--------------------------------- | :------------------------------------------- | :------------- | ------------- |
| distilroberta-base     | `cross-encoder-noinjection-v_0`    | Simply finetuned cross-encoder               | 5000           | 1pos-3neg     |
| distilroberta-base     | `cross-encoder-bm25-injection-v_0` | Fine-tuned cross-encoder with BM25 injection | 5000           | N/A           |
| ms-macro-MiniLM-L-6-v2 | `cross-encoder-noinjection-v_1`    | Simply finetuned cross-encoder               | 5000           | 1pos-3neg     |
| ms-macro-MiniLM-L-6-v2 | `cross-encoder-bm25-injection-v_1` | Fine-tuned cross-encoder with BM25 injection | 5000           | N/A           |
| ms-macro-MiniLM-L-6-v2 | `cross-encoder-noinjection-v_2`    | Simply finetuned cross-encoder               | 300            | 1pos-3neg     |
| ms-macro-MiniLM-L-6-v2 | `cross-encoder-bm25-injection-v_2` | Fine-tuned cross-encoder with BM25 injection | 300            | N/A           |
| ms-macro-MiniLM-L-6-v2 | `cross-encoder-noinjection-v_3`    | Simply finetuned cross-encoder               | 5000           | 3pos-1neg     |
| ms-macro-MiniLM-L-6-v2 | `cross-encoder-noinjection-v_4`    | Simply finetuned cross-encoder               | 300            | 3pos-1neg     |
