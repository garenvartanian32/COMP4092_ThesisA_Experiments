def keyPressEvent(self, event):
        event, text, key, ctrl, shift = restore_keyevent(event)
        cursor_position = self.get_position('cursor')
        if cursor_position < self.header_end_pos:
            self.restrict_cursor_position(self.header_end_pos, 'eof')
        elif key == Qt.Key_Delete:
            if self.has_selected_text():
                self.remove_text()
            else:
                self.stdkey_clear()
        elif key == Qt.Key_Backspace:
            if self.has_selected_text():
                self.remove_text()
            elif self.header_end_pos == cursor_position:
                return
            else:
                self.stdkey_backspace()
        elif key == Qt.Key_X and ctrl:
            self.cut()
        else:
            CodeEditor.keyPressEvent(self, event)