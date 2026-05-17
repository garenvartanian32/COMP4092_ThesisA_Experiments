def _create_properties(self):
        self._frame = f = ttk.Labelframe(self._sframe.innerframe,
                                         text=_('Widget properties'))
        f.grid(sticky='nswe')
        label_tpl = "{0}:"
        row = 0
        col = 0
        groups = (
            ('00', _('Required'), properties.WIDGET_REQUIRED_OPTIONS,
             properties.REQUIRED_OPTIONS),
            ('01', _('Standard'), properties.WIDGET_STANDARD_OPTIONS,
             properties.TK_WIDGET_OPTIONS),
            ('02', _('Specific'), properties.WIDGET_SPECIFIC_OPTIONS,
             properties.TK_WIDGET_OPTIONS),
            ('03', _('Custom'), properties.WIDGET_CUSTOM_OPTIONS,
             properties.CUSTOM_OPTIONS),
        )
        for gcode, gname, plist, propdescr in groups:
            padding = '0 0 0 5' if row == 0 else '0 5 0 5'
            label = ttk.Label(self._frame, text=gname,
                              font='TkDefaultFont 10 bold', padding=padding,
                              foreground='#000059')
            label.grid(row=row, column=0, sticky='we', columnspan=2)
            row += 1
            for name in plist:
                kwdata = propdescr[name]
                labeltext = label_tpl.format(name)
                label = ttk.Label(self._frame, text=labeltext, anchor=tk.W)
                label.grid(row=row, column=col, sticky=tk.EW, pady=2)
                widget = self._create_editor(self._frame, name, kwdata)
                widget.grid(row=row, column=col+1, sticky=tk.EW, pady=2)
                row += 1
                self._propbag[gcode+name] = (label, widget)
                logger.debug('Created property: {0}-{1}'.format(gname,name))