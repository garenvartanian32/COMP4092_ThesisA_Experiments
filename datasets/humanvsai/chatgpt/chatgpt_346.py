import torch.nn as nn

def get_entropies(m: nn.Module) -> Tuple[float, float]:
    current_entropy = -sum(p * torch.log(p) for p in m.parameters() if p.requires_grad)
    
    max_entropy = 0
    for child in m.children():
        child_entropy = get_entropies(child)[1]
        if child_entropy > max_entropy:
            max_entropy = child_entropy
    
    return current_entropy, max_entropy
