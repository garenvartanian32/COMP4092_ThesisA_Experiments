def slicenet_middle(encoder_output, decoder_input):
    """
    Middle part of slicenet, connecting encoder and decoder.
    Arguments:
        encoder_output: output tensor from the encoder
        decoder_input: input tensor to the decoder
    Returns:
        tensor representing the middle part of slicenet
    """
    # concatenate the encoder output and decoder input along the channel axis
    middle_output = torch.cat((encoder_output, decoder_input), dim=1)
    # perform some operations on the concatenated tensor
    middle_output = F.relu(middle_output)
    middle_output = F.dropout(middle_output, p=0.5)
    # return the resulting tensor
    return middle_output
