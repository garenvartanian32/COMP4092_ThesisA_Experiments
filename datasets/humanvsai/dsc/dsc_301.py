class TaskManager:
    def __init__(self):
        self.status = "initial"

    def reset(self):
        try:
            self.status = "initial"
            return 0
        except Exception as e:
            print(f"Reset failed: {e}")
            return 1