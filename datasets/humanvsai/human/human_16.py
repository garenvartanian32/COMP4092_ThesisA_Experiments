def save_config(self):
        self.set_option('recent_projects', self.recent_projects)
        self.set_option('expanded_state',
                        self.explorer.treewidget.get_expanded_state())
        self.set_option('scrollbar_position',
                        self.explorer.treewidget.get_scrollbar_position())
        if self.current_active_project and self.dockwidget:
            self.set_option('visible_if_project_open',
                            self.dockwidget.isVisible())