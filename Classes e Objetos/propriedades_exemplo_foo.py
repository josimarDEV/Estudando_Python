class foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value

    @x.deleter
    def x(self):
        self._x = 0


foo = foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)