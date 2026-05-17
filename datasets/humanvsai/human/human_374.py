def check(self):
		if self.__next_start is not None:
			utc_now = utc_datetime()
			if utc_now >= self.__next_start:
				result = []
				for task_source in self.__next_sources:
					records = task_source.has_records()
					if records is not None:
						result.extend(records)
				self.__update_all()
				if len(result) > 0:
					return tuple(result)