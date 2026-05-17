def set_proto_message_event(pb_message_event, span_data_message_event):
    """Sets properties on the protobuf message event.

    :param pb_message_event: protobuf message event
    :type pb_message_event: :class: `~opencensus.proto.trace.Span.TimeEvent.MessageEvent`

    :param span_data_message_event: opencensus message event
    :type span_data_message_event: :class: `~opencensus.trace.time_event.MessageEvent`
    """
    # Your code here