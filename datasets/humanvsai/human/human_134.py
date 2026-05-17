def _index_entities(self):
        all_ents = pd.DataFrame.from_records(
            [v.entities for v in self.variables.values()])
        constant = all_ents.apply(lambda x: x.nunique() == 1)
        if constant.empty:
            self.entities = {}
        else:
            keep = all_ents.columns[constant]
            ents = {k: all_ents[k].dropna().iloc[0] for k in keep}
            self.entities = {k: v for k, v in ents.items() if pd.notnull(v)}