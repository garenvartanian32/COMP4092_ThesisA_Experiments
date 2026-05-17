def get(self, id):
        self.cur.execute("SELECT * FROM jobs WHERE hash=?", (id,))
        item = self.cur.fetchone()
        if item:
            return dict(zip(
                ("id", "description", "last-run", "next-run", "last-run-result"),
                item))
        return None