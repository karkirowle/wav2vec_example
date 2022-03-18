

### Installation

You need to have miniconda installed.

To run the project please first
```
conda create --name wav2vec_example
conda activate wav2vec_example

```

Then just the appopriate pytorch install for you, which you can look up [here](https://pytorch.org/get-started/locally/),
e.g., for Linux:

```
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
```

then install the required HuggingFace libraries

```
conda install datasets transformers -c huggingface
```

### Run an example

After activating your conda environment with

```
conda activate wav2vec_example
```

Just use
```
python example.py
```
