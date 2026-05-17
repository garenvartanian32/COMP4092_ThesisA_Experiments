def to_dict(self):
        obj_dict = super(Text, self).to_dict()
        texts_dict = None
        if isinstance(self.text, list):
            texts_dict = [t.to_dict() for t in self.text]
        child_dict = {
            'type': self.__class__.__name__,
            'text': texts_dict
        }
        obj_dict.update(child_dict)
        return obj_dict