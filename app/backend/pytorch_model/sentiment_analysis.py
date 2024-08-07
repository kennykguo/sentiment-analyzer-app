import torch
import torch.nn.functional as F
from torchtext.vocab import build_vocab_from_iterator
from torchtext.data.utils import get_tokenizer
from transformers import GPT2Tokenizer, GPT2ForSequenceClassification
import pandas as pd
import numpy as np

# Load the GPT model and tokenizer
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model_path = "models/gpt.pth"
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2ForSequenceClassification.from_pretrained('gpt2')
model.load_state_dict(torch.load(model_path))
model = model.to(device)
model.eval()

def predict_single_text(text):
    inputs = tokenizer(text, return_tensors='pt').to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=-1)
    label = torch.argmax(probs, dim=1)
    return 'positive' if label.item() == 1 else 'negative'
