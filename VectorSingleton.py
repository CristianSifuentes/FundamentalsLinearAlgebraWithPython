'''
Claro, aquí tienes un ejemplo más avanzado que implementa el concepto de vectores en álgebra lineal utilizando un patrón de diseño Singleton para crear y operar con vectores en un sistema de coordenadas tridimensional. El patrón Singleton asegura que solo haya una instancia de un vector en el sistema:
'''
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector ({self.x}, {self.y}, {self.z})"

class VectorFactory:
    _vector_instance = None

    def get_vector(self):
        if self._vector_instance is None:
            self._vector_instance = Vector(0, 0, 0)
        return self._vector_instance

# Ejemplo de uso
factory = VectorFactory()
vector1 = factory.get_vector()
vector2 = factory.get_vector()

vector1.x = 1
vector1.y = 2
vector1.z = 3

vector2.x = 4
vector2.y = 5
vector2.z = 6

print(f"Vector 1: {vector1}")
print(f"Vector 2: {vector2}")

'''
En este ejemplo, hemos creado una clase Vector que representa un vector tridimensional con componentes x, y y z. La clase VectorFactory utiliza el patrón Singleton para asegurar que solo haya una instancia de vector en el sistema. Cuando obtenemos un vector del VectorFactory, en realidad estamos obteniendo la misma instancia compartida. Esto es útil en situaciones donde necesitas asegurarte de que todos los objetos que representan un vector se refieran al mismo objeto físico en el espacio tridimensional.

Puedes ampliar este ejemplo agregando más operaciones vectoriales o propiedades a la clase Vector. Esto ilustra cómo se pueden usar patrones de diseño avanzados en conjunción con conceptos de álgebra lineal, como vectores, para modelar sistemas más complejos y mantener una única fuente de verdad para los objetos del mundo real que representan.
'''
