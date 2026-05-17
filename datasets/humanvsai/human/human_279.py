def toggle_save_cb(self, w, res_dict):
        if len(res_dict) > 0:
            self.w.save.set_enabled(True)
        else:
            self.w.save.set_enabled(False)