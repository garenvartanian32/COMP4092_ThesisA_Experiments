def set_proto_message_event():
    pb_message_event.id = span_data_message_event.id
    pb_message_event.uncompressed_size = span_data_message_event.uncompressed_size
    pb_message_event.compressed_size = span_data_message_event.compressed_size
    pb_message_event.type = span_data_message_event.type
    return pb_message_event