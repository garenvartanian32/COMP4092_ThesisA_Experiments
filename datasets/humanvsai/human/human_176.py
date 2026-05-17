def get_all_memberships(
            self, limit_to=100, max_calls=None, parameters=None,
            since_when=None, start_record=0, verbose=False):
        if not self.client.session_id:
            self.client.request_session()
        query = "SELECT Objects() FROM Membership"
        # collect all where parameters into a list of
        # (key, operator, value) tuples
        where_params = []
        if parameters:
            for k, v in parameters.items():
                where_params.append((k, "=", v))
        if since_when:
            d = datetime.date.today() - datetime.timedelta(days=since_when)
            where_params.append(
                ('LastModifiedDate', ">", "'%s 00:00:00'" % d))
        if where_params:
            query += " WHERE "
            query += " AND ".join(
                ["%s %s %s" % (p[0], p[1], p[2]) for p in where_params])
        query += " ORDER BY LocalID"
        # note, get_long_query is overkill when just looking at
        # one org, but it still only executes once
        # `get_long_query` uses `ms_object_to_model` to return Organizations
        membership_list = self.get_long_query(
            query, limit_to=limit_to, max_calls=max_calls,
            start_record=start_record, verbose=verbose)
        return membership_list or []