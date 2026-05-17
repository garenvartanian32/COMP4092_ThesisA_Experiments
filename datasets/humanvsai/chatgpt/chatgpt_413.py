from flask import current_app
from werkzeug.utils import cached_property

class MochaProxy:
    def __init__(self, method_name):
        self.method_name = method_name
    
    @cached_property
    def mocha(self):
        return current_app.config['MOCHA_CLASS']()
    
    def __call__(self, *args, **kwargs):
        method = getattr(self.mocha, self.method_name)
        
        return method(*args, **kwargs)

def create_mocha_proxy(name):
    return MochaProxy(name)
