def showPluginMenu(self, panel, point=None):
        if not self._pluginMenu:
            self._pluginMenu = XViewPluginMenu(self)
        
        if point is None:
            point = QtGui.QCursor.pos()
        
        self._pluginMenu.setCurrentPanel(panel)
        self._pluginMenu.exec_(point)