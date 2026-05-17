def _get_header(self):
        out = self._get_row(self.labels)
        out += "\n"
        out += self._get_row(["---"] * len(self.labels))  # line below headers
        return out