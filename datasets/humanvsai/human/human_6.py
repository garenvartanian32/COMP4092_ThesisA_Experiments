def get_average_record(self, n):
        history_deque = collections.deque()
        averages = []
        for d in self.data_points:
            history_deque.appendleft(d)
            if len(history_deque) > n:
                history_deque.pop()
            avg = sum(history_deque) / len(history_deque)
            averages.append(round(avg, self.lr))
        return averages