def _repr_html_(self):
        """Returns a dataframe with html code when you enabled eager evaluation
        by 'spark.sql.repl.eagerEval.enabled', this only called by REPL you are
        using support eager evaluation with HTML.
        """
        import cgi
        if not self._support_repr_html:
            self._support_repr_html = True
        if self.sql_ctx._conf.isReplEagerEvalEnabled():
            max_num_rows = max(self.sql_ctx._conf.replEagerEvalMaxNumRows(), 0)
            sock_info = self._jdf.getRowsToPython(
                max_num_rows, self.sql_ctx._conf.replEagerEvalTruncate())
            rows = list(_load_from_socket(sock_info, BatchedSerializer(PickleSerializer())))
            head = rows[0]
            row_data = rows[1:]
            has_more_data = len(row_data) > max_num_rows
            row_data = row_data[:max_num_rows]

            html = "<table border='1'>\n"
            # generate table head
            html += "<tr><th>%s</th></tr>\n" % "</th><th>".join(map(lambda x: cgi.escape(x), head))
            # generate table rows
            for row in row_data:
                html += "<tr><td>%s</td></tr>\n" % "</td><td>".join(
                    map(lambda x: cgi.escape(x), row))
            html += "</table>\n"
            if has_more_data:
                html += "only showing top %d %s\n" % (
                    max_num_rows, "row" if max_num_rows == 1 else "rows")
            return html
        else:
            return None