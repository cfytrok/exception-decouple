import inspect


def redirect_exceptions(handler, *exceptions):
    """Redirect handling exceptions to handler"""

    def decorator(func):
        if inspect.iscoroutinefunction(func):
            async def wrapper(*args, **kwargs):
                try:
                    return await func(*args, **kwargs)
                except exceptions as e:
                    return await handler(e=e, *args, **kwargs)
        else:
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    return handler(e=e, *args, **kwargs)
        return wrapper
    return decorator