def _ensure_valid_record_size(self, size):
        if size > self.config['max_request_size']:
            raise Errors.MessageSizeTooLargeError(
                "The message is %d bytes when serialized which is larger than"
                " the maximum request size you have configured with the"
                " max_request_size configuration" % (size,))
        if size > self.config['buffer_memory']:
            raise Errors.MessageSizeTooLargeError(
                "The message is %d bytes when serialized which is larger than"
                " the total memory buffer you have configured with the"
                " buffer_memory configuration." % (size,))