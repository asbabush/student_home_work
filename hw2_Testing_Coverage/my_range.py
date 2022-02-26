class CheckType:
    """
    descriptor for check data type
    """

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, int):
            instance.__dict__[self.name] = value
        else:
            raise TypeError(f"'{__name__.type(value)}" f" object cannot be interpreted as an integer")

    def __set_name__(self, owner, name):
        self.name = name


class my_range:
    """
    range(stop) -> range object
    range(start, stop, step) -> range object

    Return an object that produces a sequence of integers from start
    (inclusive) to stop (exclusive) by step.  range(i, j) produces i,
    i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted!
    range(4) produces 0, 1, 2, 3. These are exactly the valid indices
    for a list of 4 elements. When step is given, it specifies the
    increment (or decrement).
    """

    start = CheckType()
    stop = CheckType()
    step = CheckType()

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        if step == 0:
            raise ValueError("my_range() arg 3 must not be zero")

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start >= self.stop:
                raise StopIteration
            value = self.start
            self.start += self.step
            return value
        elif self.step < 0:
            if self.start <= self.stop:
                raise StopIteration
            value = self.start
            self.start += self.step
            return value
