def find_all_by_parameters(self, task_name, session=None, **task_params):
        with self._session(session) as session:
            query = session.query(TaskRecord).join(TaskEvent).filter(TaskRecord.name == task_name)
            for (k, v) in six.iteritems(task_params):
                alias = sqlalchemy.orm.aliased(TaskParameter)
                query = query.join(alias).filter(alias.name == k, alias.value == v)
            tasks = query.order_by(TaskEvent.ts)
            for task in tasks:
                # Sanity check
                assert all(k in task.parameters and v == str(task.parameters[k].value) for (k, v) in six.iteritems(task_params))
                yield task