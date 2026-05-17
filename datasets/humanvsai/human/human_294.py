def policies(self):
        policies = [self._pb.integer_policy, self._pb.float_policy,
                    self._pb.string_policy, self._pb.bool_policy]
        key_types = ["integer", "float", "string", "bool"]
        return zip(key_types, policies)