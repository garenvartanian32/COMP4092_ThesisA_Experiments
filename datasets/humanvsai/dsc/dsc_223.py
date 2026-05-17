from enum import Enum

class Method(Enum):
    PUT = 1

def update(callback=None, path=None, method=Method.PUT, resource=None, tags=None, summary="Update specified resource."):
    """Decorator to configure an operation that updates a resource."""
    def decorator(func):
        # Here you can add your decorator logic
        def wrapper(*args, **kwargs):
            # Here you can add your wrapper logic
            return func(*args, **kwargs)
        return wrapper
    return decorator