def _load(self, filename=None):
        if not filename:
            filename = self.filename
        wb_ = open_workbook(filename)
        self.rsr = {}
        sheet_names = []
        for sheet in wb_.sheets():
            if sheet.name in ['Title', ]:
                continue
            ch_name = AHI_BAND_NAMES.get(
                sheet.name.strip(), sheet.name.strip())
            sheet_names.append(sheet.name.strip())
            self.rsr[ch_name] = {'wavelength': None,
                                 'response': None}
            wvl = np.array(
                sheet.col_values(0, start_rowx=5, end_rowx=5453))
            resp = np.array(
                sheet.col_values(2, start_rowx=5, end_rowx=5453))
            self.rsr[ch_name]['wavelength'] = wvl
            self.rsr[ch_name]['response'] = resp