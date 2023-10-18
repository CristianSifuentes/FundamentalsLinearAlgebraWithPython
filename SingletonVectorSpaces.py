class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

class VectorSpace2D:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VectorSpace2D, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        pass

    def dot_product(self, vector1, vector2):
        return vector1.x * vector2.x + vector1.y * vector2.y


if __name__ == "__main__":
    space = VectorSpace2D()

    vector1 = Vector2D(1, 2)
    vector2 = Vector2D(3, 4)

    print("Vector 1:", vector1)
    print("Vector 2:", vector2)

    result = vector1 + vector2
    print("Sum:", result)

    result = vector1 - vector2
    print("Subtraction:", result)

    scalar = 3
    result = vector1 * scalar
    print("Scalar Multiplication:", result)

    dot_product = space.dot_product(vector1, vector2)
    print("Dot Product:", dot_product)
