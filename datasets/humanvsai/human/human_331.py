def get_texts(self):
        with self.getstream() as text_stream:
            for i, line in enumerate(text_stream):
                line = SMSCorpus.case_normalizer(line)
                if self.mask is not None and not self.mask[i]:
                    continue
                ngrams = []
                for ng in tokens2ngrams(self.tokenizer(line)):
                    if SMSCorpus.ignore_matcher(ng):
                        continue
                    ngrams += [ng]
                yield ngrams