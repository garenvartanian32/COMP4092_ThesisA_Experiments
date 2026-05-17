def widgets(self):
    return self.activity.widgets

def get_widgets(self):
    """Get the Ext JS specific customization from the activity.

        :return: The Ext JS specific customization in `list(dict)` form"""
    return self.widgets()