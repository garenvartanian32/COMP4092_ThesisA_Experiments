def run(self, data):
        result_type = namedtuple('Result', 'code messages')
        if self.passes is True:
            result = result_type(Checker.Code.PASSED, '')
        elif self.passes is False:
            if self.allow_failure:
                result = result_type(Checker.Code.IGNORED, '')
            else:
                result = result_type(Checker.Code.FAILED, '')
        else:
            try:
                result = self.check(data, **self.arguments)
                messages = ''
                if isinstance(result, tuple):
                    result, messages = result
                if result not in Checker.Code:
                    result = Checker.Code.PASSED if bool(result) else Checker.Code.FAILED
                if result == Checker.Code.FAILED and self.allow_failure:
                    result = Checker.Code.IGNORED
                result = result_type(result, messages)
            except NotImplementedError:
                result = result_type(Checker.Code.NOT_IMPLEMENTED, '')
        self.result = result