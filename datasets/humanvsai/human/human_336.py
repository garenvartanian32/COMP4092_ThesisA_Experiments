def get_output_jsonpath_field(self, sub_output=None):
        if sub_output is not None:
            if self.output_fields is None or\
                (isinstance(self.output_fields, dict) and not sub_output in self.output_fields.itervalues()) or\
                    (isinstance(self.output_fields, list) and not sub_output in self.output_fields):
                raise ValueError(
                    "Cannot generate output jsonpath because this ExtractorProcessor will not output {}".format(sub_output))
            output_jsonpath_field = sub_output
        else:
            output_jsonpath_field = self.output_field
        return output_jsonpath_field