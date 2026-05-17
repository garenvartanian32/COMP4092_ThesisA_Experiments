def reset(self):
    try:
        self.queue_manager.reset()
        self.task_status = 'reset'
        return 0
    except Exception as e:
        print(f'Failed to reset task status: {e}')
        return 1