```python
# https://www.kaggle.com/code/emirkocak/in-depth-series-sentiment-analysis-w-transformers (word cloud implementation)
import torch
import torch.nn as nn
import torchtext
from torchtext.data.functional import generate_sp_model, load_sp_model, sentencepiece_tokenizer, sentencepiece_numericalizer
from torchtext.vocab import build_vocab_from_iterator
import torchtext.transforms as T
from torch.utils.data import Dataset, DataLoader
import torch.utils.data.dataloader as dataloader
from torch.nn import functional as F
import torch.optim as optim

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import math
import os
import re
```


```python
root = "/kaggle/input/movies"
```


```python
with open(os.path.join(root, "reviews.csv"), encoding='latin-1') as f:
        with open(os.path.join("/kaggle/working", "data.txt"), "w") as f2:
            for line in f:
                text_only = "".join(line.split(",")[:-1])
                filtered = re.sub(r'\\|\\n|;', ' ', text_only.replace('"', ' ').replace('\n', ' ')) # Replaces double quotes with a space, and \n with a space
                # Replaces \\, \\n, and; with a space
                # Replaces HTML codes with real characters
                filtered = filtered.replace(' #39;', "'")
                filtered = filtered.replace(' #38;', "&")
                filtered = filtered.replace(' #36;', "$")
                filtered = filtered.replace(' #151;', "-")
                f2.write(filtered.lower() + "\n")
```


```python
# Generate the SentencePiece tokenizer
# Text tokenizer and detokenizer
# It will tokenize words into subpieces instead of words
# This function will create a set of subtokens to fit the set vocabulary size
# There will always be enough subwords to subtokenize a dataset if you think about it :) -> max 2 length pairs = 26!
# Saved in the home directory
generate_sp_model(os.path.join("/kaggle/working", "data.txt"), vocab_size=20000, model_prefix='/kaggle/working/transformer')
```


```python

```


```python

```


```python

```


```python
class IMDB(Dataset):
    def __init__(self, root):
        self.root = root

        # Reads the file into a pandas DataFrame with Latin-1 encoding
        self.df = pd.read_csv(os.path.join(root, "reviews.csv"), names=["Article", "Class"], encoding='latin-1')

        # Replaces empty entries with a space
        self.df.fillna('', inplace=True)

        # Clean the 'Article' column
        self.df['Article'] = self.df['Article'].str.replace(r'\\n|\\|\\r|\\r\\n|\n|"', ' ', regex=True)
        self.df['Article'] = self.df['Article'].replace({' #39;': "'", ' #38;': "&", ' #36;': "$", ' #151;': "-"}, regex=True)

        # Shuffle the DataFrame
        self.df = self.df.sample(frac=1).reset_index(drop=True)

    # To use for DataLoader
    def __getitem__(self, index):
        text = self.df.loc[index]["Article"].lower()
        
        class_label = self.df.loc[index]["Class"]

        if class_label == 'positive':
            class_index = 1
        else:
            class_index = 0
            
        return class_label, text

    def __len__(self):
        return len(self.df)

# Example usage:
train_dataset = IMDB(root)
print(len(train_dataset))
print(train_dataset.df.loc[0]["Article"])
print(train_dataset.df.loc[0]["Class"])

```

    50000
    This film would usually classify as the worst movie production ever. Ever. But in my opinion it is possibly the funniest. The horrifying direction and screenplay makes this film priceless. I bought the movie whilst sifting through the bargain DVD's at my local pound shop. Me and some friends then watched it, admittedly whilst rather drunk. It soon occurred that this wasn't any normal film. Instead a priceless relic of what will probably be James Cahill's last film. At first we were confused and were screaming for the DVD player to be turned off but thankfully in our abnormal state no-one could be bothered. Instead we watched the film right through. At the end we soon realised we had found any wasters dream, something that you can acceptably laugh at for hours, whilst laughing for all the wrong reasons. We soon showed all our other friends and they too agreed, this wasn't a work of abysmal film. This was a film that you can truly wet yourself laughing at. This was a film that anyone can enjoy. This was genius.
    1



```python
# Split 90% - 10%
validation_split = 0.9

# Total train examples
n_train_examples = int(len(train_dataset) * validation_split)

# Total validation examples
n_valid_examples = len(train_dataset) - n_train_examples

# Splits them based on values provided
train_data, valid_data = torch.utils.data.random_split(train_dataset, [n_train_examples, n_valid_examples], generator=torch.Generator().manual_seed(42))
```


```python
# Create dataloaders for the training and testing datasets
# Dataloaders allow for batching, shuffling

batch_size = 128

train_loader = dataloader.DataLoader(train_data, shuffle=True, batch_size=batch_size, drop_last = True)

test_loader = dataloader.DataLoader(valid_data, shuffle=True, batch_size=batch_size, drop_last = True)
```


```python
def yield_tokens(file_path):
    with io.open(file_path, encoding='utf-8') as f:
        # Iterate through each line in the file
        for line in f:
            # Accesses the vocab file, splits the line by tab, and gets the first entry (the actual token)
            # Yield the token from the first column (split by tab)
            yield [line.split("\t")[0]]

# Build a vocabulary from the tokens yielded by the yield_tokens function
    # <pad> is a padding token that is added to the end of a sentence to ensure the length of all sequences in a batch is the same
    # <sos> signals the "Start-Of-Sentence" aka the start of the sequence
    # <eos> signal the "End-Of-Sentence" aka the end of the sequence
    # <unk> "unknown" token is used if a token is not contained in the vocab
# From torchtext library (build_vocab_from_iterator)
# Builds a generator object, that is treated like an iterator
vocab = build_vocab_from_iterator(yield_tokens("/kaggle/working/transformer.vocab"), specials=['<sos>', '<pad>', '<eos>', '<unk>'], special_first=True)

# Set the default index for unknown tokens to the index of the '<unk>' token
vocab.set_default_index(vocab['<unk>'])
```


```python
# Maximum sequence length for text inputs
max_len = 256

# Data transform to turn text into vocab tokens
text_transform = T.Sequential(
    # Tokenize with pre-existing Tokenizer
    T.SentencePieceTokenizer("/kaggle/working/transformer.model"),
    # Converts the sentences to indices based on given vocabulary
    T.VocabTransform(vocab=vocab),
    # Add <sos> at the beginning of each sentence. 1 because the index for <sos> in the vocabulary is 1 as seen in previous section
    T.AddToken(vocab['<sos>'], begin=True),
    # Crop the sentence if it is longer than the max length minus 2 to accommodate <sos> and <eos> tokens
    T.Truncate(max_seq_len=max_len-2),
    # Add <eos> at the end of each sentence. 2 because the index for <eos> in the vocabulary is 2 as seen in previous section
    T.AddToken(vocab['<eos>'], begin=False),
    # Convert the list of lists to a tensor. This will also pad a sentence with the <pad> token if it is shorter than the max length.
    # This ensures all sentences are the same length!
    T.ToTensor(padding_value=vocab['<pad>']),
    # Pad the sequence to ensure it's exactly max_len tokens long
    T.PadTransform(max_length=max_len, pad_value=vocab['<pad>']),
)
```


```python

```


```python

```


```python

```


```python
# No changes

class FeedForward(nn.Module):
    def __init__(self, n_embd):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 4 * n_embd),
            nn.ReLU(),
            nn.Linear(4 * n_embd, n_embd),
            nn.Dropout(dropout),
        )
    
    def forward(self, x):
        return self.net(x)
```


```python
# Updated to unpack the tuple

class Block(nn.Module):
    def __init__(self, n_embd, n_head):
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_head, head_size)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ffwd = FeedForward(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self, x):
        sa_out, attn_weights = self.sa(self.ln1(x))
        x = x + sa_out  # Residual connection
        x = x + self.ffwd(self.ln2(x))
        return x, attn_weights
```


```python
# Updated to return attention weights

class Head(nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.key = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        B, T, C = x.shape
        k = self.key(x)
        q = self.query(x)
        wei = q @ k.transpose(-2, -1) * C ** -0.5
        wei = F.softmax(wei, dim=-1)
        wei = self.dropout(wei)
        v = self.value(x)
        out = wei @ v
        return out, wei  # Return attention weights
```


```python
class MultiHeadAttention(nn.Module):
    def __init__(self, num_heads, head_size):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size) for _ in range(num_heads)])
        self.proj = nn.Linear(n_embd, n_embd)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        out = []
        attn_weights = []
        for h in self.heads:
            head_out, head_attn = h(x)
            out.append(head_out)
            attn_weights.append(head_attn)
        out = torch.cat(out, dim=-1)
        out = self.dropout(self.proj(out))
        attn_weights = torch.stack(attn_weights, dim=1)  # (B, num_heads, T, T)
        return out, attn_weights
```


```python
class Transformer(nn.Module):
    def __init__(self):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd)
        self.position_embedding_table = nn.Embedding(block_size + 1, n_embd)
        self.blocks = nn.ModuleList([Block(n_embd, n_head=n_head) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, output_size)
 
    def forward(self, idx):
        B, T = idx.shape
        tok_emb = self.token_embedding_table(idx)  # (B, T, C)
        pos_emb = self.position_embedding_table(torch.arange(T, device=idx.device))  # (T, C)
        x = tok_emb + pos_emb  # (B, T, C) - broadcasting

        for i, block in enumerate(self.blocks):
            x, attn_weights = block(x)  # Save attention weights from the last block

        x = self.ln_f(x)
        logits = self.lm_head(x[:, 0, :])  # (B, output_size) - we use the CLS token representation

        return logits, attn_weights
```


```python
# Hyperparameters
device = 'cuda' if torch.cuda.is_available() else 'cpu'
block_size = 256
n_embd = 768
n_head = 12
n_layer = 2
dropout = 0.3
nepochs = 10
output_size = 2
vocab_size = len(vocab)
learning_rate = 5e-4
```


```python
# Define the model

model = Transformer()

model.to(device)

optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=5e-4)

loss_fn = nn.CrossEntropyLoss()

lr_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=nepochs, eta_min=0)

training_loss_list = []
test_loss_list = []
training_acc_list = []
test_acc_list = []
```


```python
# Training Loop
# Train for 10 epochs or so... first
train_acc = 0
test_acc = 0

for epoch in range(nepochs):

    model.train()
    
    print("training:")
    
    train_acc_count = 0
    test_acc_count = 0
    train_steps = 0
    
    for labels, texts in train_loader:
        text_tokens = text_transform(list(texts)).to(device)
        labels = labels.to(device)
        logits, _ = model(text_tokens)
        loss = F.cross_entropy(logits, labels)
        
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()
    
        # Log the training loss
        training_loss_list.append(loss.item())
        
        # Update training accuracy
        train_acc_count += (logits.argmax(1) == labels).sum().item()
        train_steps += batch_size
    
    # Calculate average training accuracy
    train_acc = (train_acc_count / train_steps)
    training_acc_list.append(train_acc)
    
    # Update learning rate
    lr_scheduler.step()
    
    # Set the model to evaluation mode
    model.eval()
    
    print("evaluating:")
    train_acc_count = 0
    test_acc_count = 0
    test_steps = 0
    
    
    with torch.no_grad():
        for labels, texts in test_loader:
            text_tokens = text_transform(list(texts)).to(device)
            labels = labels.to(device)
            logits, _ = model(text_tokens)
            loss = F.cross_entropy(logits, labels)
            
            test_acc_count += (logits.argmax(1) == labels).sum().item()
            test_steps += batch_size
        
        # Calculate average testing accuracy
        test_acc = (test_acc_count / test_steps)
        test_acc_list.append(test_acc)

    # Print out the results for this epoch
    print(f'Epoch {epoch+1}/{nepochs}')
    print(f'Training Accuracy: {train_acc*100:.2f}%')
    print(f'Testing Accuracy: {test_acc*100:.2f}%')
```

    training
    evaluating
    Epoch 1/10
    Training Accuracy: 70.15%
    Testing Accuracy: 79.51%
    training



    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Cell In[15], line 27
         24 optimizer.step()
         26 # Log the training loss
    ---> 27 training_loss_list.append(loss.item())
         29 # Update training accuracy
         30 train_acc_count += (logits.argmax(1) == labels).sum().item()


    KeyboardInterrupt: 



```python
_ = plt.figure(figsize=(10, 5))
_ = plt.plot(np.linspace(0, nepochs, len(training_loss_list)), training_loss_list)
_ = plt.plot(np.linspace(0, nepochs, len(test_loss_list)), test_loss_list)

_ = plt.legend(["Train", "Test"])
_ = plt.title("Training Vs Test Loss")
_ = plt.xlabel("Epochs")
_ = plt.ylabel("Loss")
```


    
![png](output_23_0.png)
    



```python
# Save the model
torch.save(model.state_dict(), 'gpt.pth')
```


```python
# Have to run atleast one epoch fully through
_ = plt.figure(figsize=(10, 5))
_ = plt.plot(np.linspace(0, nepochs, len(training_acc_list)), training_acc_list)
_ = plt.plot(np.linspace(0, nepochs, len(test_acc_list)), test_acc_list)

_ = plt.legend(["Train", "Test"])
_ = plt.title("Training Vs Test Accuracy")
_ = plt.xlabel("Epochs")
_ = plt.ylabel("Accuracy")
print("Max Test Accuracy %.2f%%" % (np.max(test_acc_list) * 100))
```

    Max Test Accuracy 79.51%



    
![png](output_25_1.png)
    



```python
def predict_single_text(model, text, text_transform, vocab):
    # Transform the input text to tokens
    tokens = text_transform([text]).to(device)
    print(tokens.shape)
    
    with torch.no_grad():
        logits, attn_weights = model(tokens)
    
    # Get the probabilities and predicted label
    probs = F.softmax(logits, dim=-1)
    label = torch.argmax(probs, dim=1)
    
    print(probs)
    
    print(attn_weights.shape)
    
    # Example of analyzing attention maps
    # Get the attention map for the last head and the first sample
    att_map = attn_weights[0, -1, :, :]  # Shape: (T, T)
    
    # Sum the attention weights across all tokens for the [CLS] token
    att_weights = att_map[0]  # Attention weights for the [CLS] token
    
    # Get top 10 tokens with the highest attention weights
    top10 = att_weights.argsort(descending=True)[:10]
    top10_tokens = [vocab.lookup_token(tokens[0][idx].item()) for idx in top10]
    
    print("Top 10 tokens with highest attention:", top10_tokens)
    
    if label.item() == 0:
        return 'negative'
    else:
        return 'positive'

# Example usage:
text = "That's pretty much the whole soundtrack to this film. I just saw this baby at the Munich Film Festival and it rocked the house. Director Doug Pray is never seen in this documentary, nor I think he is even heard, but he has done a very intimate look into the lives and history of the mixer. He has segmented his film into about eight chapters and then his motley group of enthusiastic interviews will be spiced throughout according to what they are talking about. I was never big into scratching but the film does a wonderful job of keeping elementary for those who know little, and infusing in-jokes for those who are experts themselves in this area. Mix Master Mike from the Beastie Boys is in this film, but it wasn't until after the film that I could name several heavy hitters in the industry (DJ Shadow, Q- Bert, etc). The extreme fascination for turntables by these talented and quirky DJs is evident in their explanations of what their music means to them. The film also sheds some gratifying light on these guys (and one woman) to be classified as musicians. Pray doesn't let his film idle and if there exists a slow scene it is soon re-energized by hardly ever ceasing music. If nothing else, this film will increase your slang vocabulary. I have to get back to digging, so I'll end this review. See it, it will be of interest. Good stuff man. Good stuff."
output = predict_single_text(model, text, text_transform, vocab)
print("Predicted sentiment:", output)
```


```python

```
