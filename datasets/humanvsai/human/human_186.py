def format_sass_stack(self):
        if not self.rule_stack:
            return ""
        ret = ["on ", self.format_file_and_line(self.rule_stack[0]), "\n"]
        last_file = self.rule_stack[0].source_file
        # TODO this could go away if rules knew their import chains...
        # TODO this doesn't mention mixins or function calls.  really need to
        # track the call stack better.  atm we skip other calls in the same
        # file because most of them are just nesting, but they might not be!
        # TODO the line number is wrong here for @imports, because we don't
        # have access to the UnparsedBlock representing the import!
        # TODO @content is completely broken; it's basically textual inclusion
        for rule in self.rule_stack[1:]:
            if rule.source_file is not last_file:
                ret.extend((
                    "imported from ", self.format_file_and_line(rule), "\n"))
            last_file = rule.source_file
        return "".join(ret)