def keyPressEvent(self, event):
    if event.key() == Qt.Key_Delete:
        selected_items = self.selectedItems()
        for item in selected_items:
            if item.isHeader():
                event.ignore()
                return
        super().keyPressEvent(event)
    else:
        super().keyPressEvent(event)