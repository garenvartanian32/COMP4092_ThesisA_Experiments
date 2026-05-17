def resizeColumnsToContents(self):
    # Reimplementation of Qt Method to avoid removing the header.
    header = self.horizontalHeader()
    if not header:
        return
    header.setStretchLastSection(False)
    if self.model() and self.model().rowCount() > 0:
        self.setVisible(False)
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            width = header.sectionSize(i)
            self.setColumnWidth(i, width)
        self.setVisible(True)
    header.setStretchLastSection(True)

