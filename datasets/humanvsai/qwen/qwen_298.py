def lstm_hidden_bias(tensor):
    tensor[1] = 1
    tensor[0] = 0
    tensor[2] = 0
    tensor[3] = 0
import torch
biases = torch.zeros(4)