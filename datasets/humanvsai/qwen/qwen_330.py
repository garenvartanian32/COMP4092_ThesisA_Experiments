def showPluginMenu(self, panel, point=None):
    if point is None:
        point = self.cursor().pos()
    menu = QMenu(panel)
    menu.addAction('Action 1')
    menu.addAction('Action 2')
    menu.exec_(point)