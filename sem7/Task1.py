from math import sqrt

def is_int(s: str):
    try:
        int(s)
        return True
    except ValueError:
        return False
    return False

class Vector():
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, s: str = None):
        # '{456, 1632, 321}'
        if s is not None:
            values = s[1:-1].split(', ')
            for value in values:
                assert(is_int(value))
            self.x = float(values[0])
            self.y = float(values[1])
            self.z = float(values[2])
        else:
            self.x = x
            self.y = y
            self.z = z

    def __abs__(self):
        l = sqrt(self.x**2 + self.y**2 + self.z**2)
        return l

    def __add__(self, other):
        x1 = self.x + other.x
        y1 = self.y + other.y
        z1 = self.z + other.z
        return Vector(x1, y1, z1)

    def __sub__(self, other):
        x2 = self.x - other.x
        y2 = self.y - other.y
        z2 = self.z - other.z
        return Vector(x2, y2, z2)

    def __mul__(self, other):
        if isinstance(other, float):
            x3 = self.x * other
            y3 = self.y * other
            z3 = self.z * other
            return Vector(x3, y3, z3)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __matmul__(self, other):

        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def __str__(self):
        return str(self.x) + ' ' + str(self.y) + ' ' + str(self.z)

n = int(input())
A = []
for i in range(n):
    A.append(Vector(s=input()))

result = Vector(0, 0, 0)
for i in range(len(A)):
    result += A[i]
print(result*(1/n))
Area = 0
for i in range(len(A)):
    for j in range(len(A)):
        for k in range(len(A)):
            u1 = A[j] - A[i]
            u2 = A[k] - A[i]
            u3 = u1 @ u2
            S = abs(u3)/2
            Area = max(Area, S)

print(Area)



