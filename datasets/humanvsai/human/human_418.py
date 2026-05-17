def export_task(self, img, cont):
        return self._tasks_manager.create("export", img=img, cont=cont)