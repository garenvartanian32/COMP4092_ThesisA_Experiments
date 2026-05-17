from typing import TypeVar, Callable, Any
T = TypeVar('T')
def accepts(arg_type: T) -> Callable[[Any], T]:
    def check_accepts(func):
        def new_func(*args, **kwargs):
            assert isinstance(args[0], arg_type), f"Type Error: argument '{arg_type}' expected"
            return func(*args, **kwargs)
        return new_func
    return check_accepts

def returns(ret_type: T) -> Callable[[Any], T]:
    def check_returns(func):
        def new_func(*args, **kwargs):
            result = func(*args, **kwargs)
            assert isinstance(result, ret_type), f"Type Error: return type '{ret_type}' expected"
            return result
        return new_func
    return check_returns
