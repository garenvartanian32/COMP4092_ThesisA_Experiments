def continuous_decode_on_eval_data(self, checkpoint, dataset):
    """Decode from dataset on new checkpoint."""
    # Load the checkpoint
    self.load_checkpoint(checkpoint)

    # Iterate over the dataset
    for data in dataset:
        # Decode the data
        decoded_data = self.decode(data)

        # Print the decoded data
        print(decoded_data)