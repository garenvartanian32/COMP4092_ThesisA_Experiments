def edit_project_preferences(self):
    if self.projects.get_active_project():
        project_path = self.projects.get_active_project().get_root_path()
        self.preferences_dialog.show_preferences_dialog(project_path)
    else:
        self.show_message('No active project found.')