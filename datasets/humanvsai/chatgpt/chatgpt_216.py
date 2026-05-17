def set_properties_on_pb_message_event(pb_message_event, span_data_message_event):
    """Sets properties on the protobuf message event.

    :type pb_message_event:
        :class: `~opencensus.proto.trace.Span.TimeEvent.MessageEvent`
    :param pb_message_event: protobuf message event
    :type span_data_message_event:
        :class: `~opencensus.trace.time_event.MessageEvent`
    :param span_data_message_event: opencensus message event
    """
    pb_message_event.id = span_data_message_event.id
    pb_message_event.uncompressed_size_bytes = span_data_message_event.uncompressed_size_bytes
    pb_message_event.compressed_size_bytes = span_data_message_event.compressed_size_bytes
    pb_message_event.type = span_data_message_event.type
    pb_message_event.data = span_data_message_event.data
