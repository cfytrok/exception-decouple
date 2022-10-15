A decorator that allows you to decouple exception handling. Separating logic and error handling makes the code more readable.

# Installation
```
$ pip install exception-decouple
```
# Example
```python
from exception_decouple import redirect_exceptions


# Let's say you have a function and want to decouple error handling.
def foo(some_arg):
    try:
        raise KeyError
    except KeyError:
        return False
    except TypeError:
        return True


# You define a handler function and add an argument e to the existing ones.
def handler(some_arg, e):
    if isinstance(e, KeyError):
        return False
    elif isinstance(e, TypeError):
        return True


# Now you use a decorator to redirect exception handling to this function
@redirect_exceptions(handler, KeyError, TypeError)
def foo(some_arg):
    raise KeyError


# You can use chained decorators
def key_error_handler(some_arg, e):
    return False


def type_error_handler(some_arg, e):
    return True


@redirect_exceptions(key_error_handler, KeyError)
@redirect_exceptions(type_error_handler, TypeError)
def foo(some_arg):
    raise KeyError

# You can use the decorator with methods and coroutines too. 
# Just make sure the handler takes the same arguments. 
def method_handler(self, some_arg, e):
    pass

async def coro_handler(some_arg, e):
    pass
```