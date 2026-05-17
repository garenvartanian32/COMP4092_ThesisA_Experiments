def set_span_from_ids(self, span_list):
        this_span = Cspan()
        this_span.create_from_ids(span_list)
        self.node.append(this_span.get_node())