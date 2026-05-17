def lstm_hidden_bias(tensor: torch.Tensor) -> None:
    # gates are (b_hi|b_hf|b_hg|b_ho) of shape (4*hidden_size)
    tensor.data.zero_()
    hidden_size = tensor.shape[0]  
    tensor.data[hidden_size:(2 * hidden_size)] = 1.0