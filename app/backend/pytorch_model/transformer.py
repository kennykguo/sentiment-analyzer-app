import torch
import torch.nn as nn
import torch.nn.functional as F
from torchtext.vocab import build_vocab_from_iterator
import torchtext.transforms as T
import io

# Define your hyperparameters
block_size = 256
n_embd = 768
n_head = 12
n_layer = 2
dropout = 0.4
output_size = 2

# Load vocabulary
def yield_tokens(file_path):
    with io.open(file_path, encoding='utf-8') as f:
        for line in f:
            yield [line.split("\t")[0]]

vocab = build_vocab_from_iterator(yield_tokens("sentencepiece/transformer.vocab"), 
                                  specials=['<cls>', '<pad>', '<eos>', '<unk>'], 
                                  special_first=True)
vocab.set_default_index(vocab['<unk>'])

# Define text transform
text_transform = T.Sequential(
    T.SentencePieceTokenizer("sentencepiece/transformer.model"),
    T.VocabTransform(vocab),
    T.AddToken(vocab['<cls>'], begin=True),
    T.Truncate(max_seq_len=254),
    T.AddToken(vocab['<eos>'], begin=False),
    T.ToTensor(padding_value=vocab['<pad>']),
    T.PadTransform(max_length=256, pad_value=0),
)

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
        return out, wei

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
        attn_weights = torch.stack(attn_weights, dim=1)
        return out, attn_weights

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
        x = x + sa_out
        x = x + self.ffwd(self.ln2(x))
        return x, attn_weights

class Transformer(nn.Module):
    def __init__(self):
        super().__init__()
        self.token_embedding_table = nn.Embedding(len(vocab), n_embd)
        self.position_embedding_table = nn.Embedding(block_size + 1, n_embd)
        self.blocks = nn.ModuleList([Block(n_embd, n_head=n_head) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, output_size)
 
    def forward(self, idx):
        B, T = idx.shape
        tok_emb = self.token_embedding_table(idx)
        pos_emb = self.position_embedding_table(torch.arange(T, device=idx.device))
        x = tok_emb + pos_emb

        attn_weights = None
        for i, block in enumerate(self.blocks):
            x, attn_weights = block(x)

        x = self.ln_f(x)
        logits = self.lm_head(x[:, 0, :])

        return logits, attn_weights