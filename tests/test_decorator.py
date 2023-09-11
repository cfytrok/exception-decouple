from unittest import TestCase, IsolatedAsyncioTestCase
from exception_decouple import redirect_exceptions


class TestHandler(TestCase):
    def test_function_handler(self):
        self.assertTrue(some_function(KeyError))
        with self.assertRaises(Exception):
            some_function(Exception)

    def test_function_handler_with_args(self):
        self.assertTrue(many_args_function(KeyError, 'arg2', kwarg1='kwarg1'))
        with self.assertRaises(Exception):
            many_args_function(Exception)

    def test_method_handler(self):
        obj = SomeClass()
        self.assertTrue(obj.some_method(KeyError))
        with self.assertRaises(Exception):
            obj.some_method(Exception)


class TestAsyncHandler(IsolatedAsyncioTestCase):
    async def test_coro_function_handler(self):
        self.assertTrue(await coro_function(KeyError))
        with self.assertRaises(Exception):
            await coro_function(Exception)

    async def test_coro_method_handler(self):
        obj = SomeClass()
        self.assertTrue(await obj.coro_method(KeyError))
        with self.assertRaises(Exception):
            await obj.coro_method(Exception)


def function_handler(exception, e):
    return True


@redirect_exceptions(function_handler, KeyError)
def some_function(exception):
    raise exception


def any_args_handler(*args, e, **kwargs):
    return True


@redirect_exceptions(any_args_handler, KeyError)
def many_args_function(exception, arg2, kwarg1=None):
    raise exception


async def coro_handler(exception, e):
    return True


@redirect_exceptions(coro_handler, KeyError)
async def coro_function(exception):
    raise exception


def method_handler(self, exception, e):
    return True


async def coro_method_handler(self, exception, e):
    return True


class SomeClass:
    @redirect_exceptions(method_handler, KeyError)
    def some_method(self, exception):
        raise exception

    @redirect_exceptions(coro_method_handler, KeyError)
    async def coro_method(self, exception):
        raise exception
