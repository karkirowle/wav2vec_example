

### Installation

You need to have miniconda installed.

To run the project please first (make sure that you use Python version 3.7 for Windows)
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

You will also need an audio backend. It should automatically install for Linux, but for Windows you need to install the

```
conda install -c conda-forge pysoundfile
```

If it fails runtime, you can install the backend manually also for Linux:

```
conda install -c conda-forge sox
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

If you want to run the example on a CPU, you can use, you need to write device=cpu.
