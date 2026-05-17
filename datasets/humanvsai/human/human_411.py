def list_replications(self):
        docs = self.database.all_docs(include_docs=True)['rows']
        documents = []
        for doc in docs:
            if doc['id'].startswith('_design/'):
                continue
            document = Document(self.database, doc['id'])
            document.update(doc['doc'])
            documents.append(document)
        return documents