def approx_derivative(f, x, delta=1e-6):
    derivative = (f(x+delta)-f(x-delta))/(2*delta)
    return derivative
 
def approx_derivative_2(f, delta=1e-6):
    def f_prime(x):
        derivative = (f(x + delta) - f(x - delta)) / (2 * delta)
        return derivative
    return  f_prime
