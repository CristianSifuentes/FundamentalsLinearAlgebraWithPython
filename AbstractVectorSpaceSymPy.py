from sympy import symbols, expand, diff, simplify

# Definir las variables simbólicas
x = symbols('x')

# Crear una función que genere polinomios en el espacio vectorial
def generate_polynomial(coefficients):
    return sum(coefficients[i] * x**i for i in range(len(coefficients)))

# Definir dos polinomios arbitrarios
p1 = generate_polynomial([1, 2, 3])  # p1(x) = 1 + 2x + 3x^2
p2 = generate_polynomial([2, 0, -1]) # p2(x) = 2 - x^2

# Realizar operaciones en el espacio vectorial
result_sum = p1 + p2
result_diff = p1 - p2
result_derivative = diff(p1, x)
result_simplified = simplify(p1)

# Imprimir resultados
print(f'p1(x) = {p1}')
print(f'p2(x) = {p2}')
print(f'p1(x) + p2(x) = {result_sum}')
print(f'p1(x) - p2(x) = {result_diff}')
print(f'Derivative of p1(x) = {result_derivative}')
print(f'Simplified p1(x) = {result_simplified}')
