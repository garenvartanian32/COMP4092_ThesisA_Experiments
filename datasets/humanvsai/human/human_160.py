def require_scalar(self, *args: Type) -> None:
        node = Node(self.yaml_node)
        if len(args) == 0:
            if not node.is_scalar():
                raise RecognitionError(('{}{}A scalar is required').format(
                    self.yaml_node.start_mark, os.linesep))
        else:
            for typ in args:
                if node.is_scalar(typ):
                    return
            raise RecognitionError(
                ('{}{}A scalar of type {} is required').format(
                    self.yaml_node.start_mark, os.linesep, args))