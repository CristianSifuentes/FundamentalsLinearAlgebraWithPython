from abc import ABC, abstractmethod

class LinearAlgebraFactory(ABC):
    @abstractmethod
    def create_vector(self, components):
        pass

    @abstractmethod
    def create_matrix(self, rows, columns, data):
        pass

class ThreeDimensionalVector:
    def __init__(self, x, y, z):
        self.components = (x, y, z)

    def __str__(self):
        return f"({self.components[0]}, {self.components[1]}, {self.components[2]})"

class ThreeDimensionalMatrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

class ThreeDimensionalFactory(LinearAlgebraFactory):
    def create_vector(self, components):
        if len(components) != 3:
            raise ValueError("A 3D vector must have exactly 3 components.")
        return ThreeDimensionalVector(*components)

    def create_matrix(self, rows, columns, data):
        if rows != 3 or columns != 3:
            raise ValueError("A 3x3 matrix is required for 3D operations.")
        return ThreeDimensionalMatrix(data)

def perform_operations(factory):
    v1 = factory.create_vector((1, 2, 3))
    v2 = factory.create_vector((4, 5, 6))
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")

    matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = factory.create_matrix(3, 3, matrix_data)
    print("Matrix:")
    print(matrix)

    # Realizar operaciones matriciales o vectoriales aquí
    # Por ejemplo, suma de vectores, multiplicación de matrices, etc.

# Uso de la fábrica concreta para realizar operaciones en 3D
factory = ThreeDimensionalFactory()
perform_operations(factory)
