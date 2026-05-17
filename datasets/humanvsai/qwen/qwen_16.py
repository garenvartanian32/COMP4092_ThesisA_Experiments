def save_config(self):
    config = {}
    config['projects'] = self.opened_projects
    config['tree_widget_state'] = self.tree_widget.saveState().toBase64().data().decode('utf-8')
    if self.current_project:
        config['dock_widget_visible'] = self.dock_widget.isVisible()
    with open(self.config_file_path, 'w') as config_file:
        json.dump(config, config_file, indent=4)