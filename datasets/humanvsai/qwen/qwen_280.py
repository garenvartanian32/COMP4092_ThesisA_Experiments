def continuous_decode_on_eval_data(self):
    self.model.eval()
    self.model.to(self.device)
    self.model.zero_grad()
    self.model.decoder.start_of_sequence_token_id = self.tokenizer.bos_token_id
    self.model.decoder.end_of_sequence_token_id = self.tokenizer.eos_token_id
    self.model.decoder.pad_token_id = self.tokenizer.pad_token_id
    with torch.no_grad():
        for batch in self.eval_dataloader:
            batch = {k: v.to(self.device) for (k, v) in batch.items()}
            outputs = self.model.generate(input_ids=batch['input_ids'], max_length=self.max_length, num_beams=self.num_beams, early_stopping=True)
            decoded_outputs = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
            self.process_decoded_outputs(decoded_outputs)

def process_decoded_outputs(self, decoded_outputs):
    """Process the decoded outputs."""
    for output in decoded_outputs:
        print(output)