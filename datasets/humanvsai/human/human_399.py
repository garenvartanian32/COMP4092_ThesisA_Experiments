def replace(self, nodes):
        files = {}
        for node in nodes:
            if node.family == "SearchFile":
                files[node.file] = node.children
            elif node.family == "SearchOccurence":
                file = node.parent.file
                if not file in files:
                    files[file] = []
                files[file].append(node)
        replacement_pattern = self.Replace_With_comboBox.currentText()
        SearchAndReplace.insert_pattern(replacement_pattern, self.__replace_with_patterns_model)
        replace_results = {}
        for file, occurrences in files.iteritems():
            editor = self.__container.get_editor(file)
            if editor:
                document = editor.document()
            else:
                cache_data = self.__files_cache.get_content(file)
                if cache_data is None:
                    LOGGER.warning(
                        "!> {0} | '{1}' file doesn't exists in files cache!".format(self.__class__.__name__, file))
                    continue
                content = self.__files_cache.get_content(file).content
                document = self.__get_document(content)
                self.__cache(file, content, document)
            replace_results[file] = self.__replace_within_document(document, occurrences, replacement_pattern)
        self.set_replace_results(replace_results)
        self.__container.engine.notifications_manager.notify(
            "{0} | '{1}' pattern occurence(s) replaced in '{2}' files!".format(self.__class__.__name__,
                                                                               sum(replace_results.values()),
                                                                               len(replace_results.keys())))