from PyQt5.QtWidgets import QMenu, QAction

def showPluginMenu(self, panel, point=None):
    """Creates the interface menu for this view widget.  If no point is \
        supplied, then the current cursor position will be used.
        
        :param      panel | <XViewPanel>
                    point | <QPoint> || None"""

    # Create a menu
    menu = QMenu()

    # Create actions
    action1 = QAction("Action 1", self)
    action2 = QAction("Action 2", self)

    # Add actions to the menu
    menu.addAction(action1)
    menu.addAction(action2)

    # Show the menu
    if point is None:
        menu.exec_(QCursor.pos())
    else:
        menu.exec_(point)