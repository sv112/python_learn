from dataclasses import dataclass, astuple
from numbers import Number

@dataclass(slots=True, frozen=True)
class Vector:
    x: float
    y: float
    z: float

    def __iter__(self):
        yield from astuple(self)

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, Number):
            return Vector(self.x * other, self.y * other, self.z * other)

        raise TypeError(f'Cannot multiply Vector with {other}')

    def __rmul__(self, other):
        return self.__mul__(other)



if __name__ == '__main__':
    v = Vector(1, 2, 3)
    (x, y, z) = v
    print(x, y , z)

    vector_set = {v}
    Vector(1, 2, 3) in vector_set

    vx = Vector(1, 2, 3) + Vector(6, 5, 4)

    print(vx)

    tuple(vx)
    print(vx * 7)
    print(7 * vx)
    print(vx * 'a')