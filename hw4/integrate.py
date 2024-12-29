import numpy as np

def riemann(f, a, b, n):

    dx = (b[0] - a[0]) / n
    dy = (b[1] - a[1]) / n
    dz = (b[2] - a[2]) / n
    total = 0
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x = a[0] + (i + 0.5) * dx
                y = a[1] + (j + 0.5) * dy
                z = a[2] + (k + 0.5) * dz
                total += f(x, y, z) * dx * dy * dz
    
    return total

def monte_carlo(f, a, b, n):
    
    x = np.random.uniform(a[0], b[0], n)
    y = np.random.uniform(a[1], b[1], n)
    z = np.random.uniform(a[2], b[2], n)
    
    total = 0
    for i in range(n):
        total += f(x[i], y[i], z[i])
    
    volume = (b[0] - a[0]) * (b[1] - a[1]) * (b[2] - a[2])
    return total / n * volume

def func(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

a = [0, 0, 0]
b = [1, 1, 1]
n = 100  

riemann_result = riemann(func, a, b, n)
print("黎曼積分結果:", riemann_result)

monte_carlo_result = monte_carlo(func, a, b, n * 100)
print("蒙地卡羅積分結果:", monte_carlo_result)
