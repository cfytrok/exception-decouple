import functools
import inspect


def redirect_exceptions(handler, *exceptions):
    """Redirect handling exceptions to handler"""

    def decorator(func):
        if inspect.iscoroutinefunction(func):
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                try:
                    return await func(*args, **kwargs)
                except exceptions as e:
                    return await handler(*args, e=e, **kwargs)
        else:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    return handler(*args, e=e, **kwargs)
        return wrapper

    return decorator
