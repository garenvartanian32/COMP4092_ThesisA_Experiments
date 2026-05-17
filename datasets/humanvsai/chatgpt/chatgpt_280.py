def decode_from_dataset_on_new_checkpoint(checkpoint_path: str, dataset: str) -> str:
    """
    Decodes the given dataset using the model weights stored in the given checkpoint file.

    Args:
        checkpoint_path: The path to the checkpoint file that contains the model weights.
        dataset: The dataset to decode.

    Returns:
        The decoded dataset.
    """
    # Load the checkpoint
    checkpoint = torch.load(checkpoint_path)

    # Initialize the model with the checkpoint weights
    model = MyModel()
    model.load_state_dict(checkpoint['model_state_dict'])

    # Decode the dataset using the model
    decoded_dataset = model.decode(dataset)

    return decoded_dataset
