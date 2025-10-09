from . import wrapt


class Typed(wrapt.AutoObjectProxy):
    def __init__(self, wrapped):
        wrapt.AutoObjectProxy.__init__(self, wrapped)
        self._self_type = type(wrapped)
        
    def _assign_(self, value, *annotation):
        self.__wrapped__ = value
        if not issubclass(type(value), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value)}")
        return self

    def __iadd__(self, other):
        value = wrapt.AutoObjectProxy.__iadd__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __isub__(self, other):
        value = wrapt.AutoObjectProxy.__isub__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __imul__(self, other):
        value = wrapt.AutoObjectProxy.__imul__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __itruediv__(self, other):
        value = wrapt.AutoObjectProxy.__itruediv__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __ifloordiv__(self, other):
        value = wrapt.AutoObjectProxy.__ifloordiv__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __imod__(self, other):
        value = wrapt.AutoObjectProxy.__imod__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __ipow__(self, other):
        value = wrapt.AutoObjectProxy.__ipow__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __ilshift__(self, other):
        value = wrapt.AutoObjectProxy.__ilshift__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __irshift__(self, other):
        value = wrapt.AutoObjectProxy.__irshift__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __iand__(self, other):
        value = wrapt.AutoObjectProxy.__iand__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __ixor__(self, other):
        value = wrapt.AutoObjectProxy.__ixor__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __ior__(self, other):
        value = wrapt.AutoObjectProxy.__ior__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value

    def __imatmul__(self, other):
        value = wrapt.AutoObjectProxy.__imatmul__(self, other)
        if not issubclass(type(value.__wrapped__), self._self_type):
            raise TypeError(f"Expected an instance of {self._self_type} but received an instance of {type(value.__wrapped__)}")        
        return value
