def run_example(self, source):
        code = compile(source, "<docs>", "exec")
        buffer = []
        invoke = partial(self.invoke, _output_lines=buffer)
        def println(text=""):
            buffer.append(text)
        exec(
            code,
            self.namespace,
            {
                "invoke": invoke,
                "println": println,
                "isolated_filesystem": self.isolated_filesystem,
            },
        )
        return buffer