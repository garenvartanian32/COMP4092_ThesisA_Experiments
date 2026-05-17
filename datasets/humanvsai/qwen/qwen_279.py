def toggle_save_cb(self, w, res_dict):
    if res_dict.get('selected', False):
        self.save_button.set_sensitive(True)
    else:
        self.save_button.set_sensitive(False)