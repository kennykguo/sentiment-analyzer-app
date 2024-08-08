import torch
import torch.nn.functional as F
from .transformer import Transformer, text_transform, vocab

def predict_single_text(model, text, text_transform, vocab):
    device = next(model.parameters()).device
    tokens = text_transform([text]).to(device)
    
    with torch.no_grad():
        logits, attn_weights = model(tokens)
    
    probs = F.softmax(logits, dim=-1)
    label = torch.argmax(probs, dim=1)
    
    # Analyze attention weights
    att_map = attn_weights[0, -1, :, :]  # Last head, first sample
    att_weights = att_map[0]  # Attention weights for the [CLS] token
    top10 = att_weights.argsort(descending=True)[:10]
    top10_tokens = [vocab.lookup_token(tokens[0][idx].item()) for idx in top10]
    
    prediction = 'positive' if label.item() == 1 else 'negative'
    return prediction, top10_tokens

def load_model(model_path):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = Transformer()
    model.load_state_dict(torch.load(model_path, map_location=device))
    model = model.to(device)
    model.eval()
    return model