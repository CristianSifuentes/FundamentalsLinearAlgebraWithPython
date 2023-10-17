class LinearTransformation:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LinearTransformation, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.rotation_angle = 0.0

    def set_rotation(self, angle_degrees):
        self.rotation_angle = angle_degrees

    def transform(self, vector):
        import math
        # Realizar la transformación lineal (rotación) en 2D
        radians = math.radians(self.rotation_angle)
        x = vector[0]
        y = vector[1]
        new_x = x * math.cos(radians) - y * math.sin(radians)
        new_y = x * math.sin(radians) + y * math.cos(radians)
        return (new_x, new_y)


if __name__ == "__main__":
    transformation = LinearTransformation()
    print(f"Rotation Angle: {transformation.rotation_angle} degrees")

    vector = (1, 0)  # Vector horizontal (1, 0)
    transformed_vector = transformation.transform(vector)
    print(f"Transformed Vector: {transformed_vector}")

    # Cambiamos el ángulo de rotación
    transformation.set_rotation(45.0)
    print(f"Rotation Angle: {transformation.rotation_angle} degrees")

    transformed_vector = transformation.transform(vector)
    print(f"Transformed Vector: {transformed_vector}")
