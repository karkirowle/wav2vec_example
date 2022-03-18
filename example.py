import torchaudio
from datasets import load_dataset, load_metric
from transformers import (
    Wav2Vec2ForCTC,
    Wav2Vec2Processor,
)
import torch

model_name = "facebook/wav2vec2-large-xlsr-53-dutch"
device = "cuda"
chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"]'  # noqa: W605

model = Wav2Vec2ForCTC.from_pretrained(model_name).to(device)
processor = Wav2Vec2Processor.from_pretrained(model_name)

speech, _ = torchaudio.load("sentence-03.wav")
resampler = torchaudio.transforms.Resample(orig_freq=16_000, new_freq=16_000)
speech = resampler.forward(speech.squeeze(0))
features = processor(speech, sampling_rate=16000, padding=True, return_tensors="pt")
input_values = features.input_values.to(device)
attention_mask = features.attention_mask.to(device)

with torch.no_grad():

    logits = model(input_values, attention_mask=attention_mask).logits
    pred_ids = torch.argmax(logits, dim=-1)
    print(processor.batch_decode(pred_ids))


