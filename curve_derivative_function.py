import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + x*3 +2

x = np.linspace(-10, 10, 100)
df = np.gradient(f(x), x)

plt.plot(x, df)
plt.xlabel('x')
plt.ylabel('df/dx')
plt.title('Représentation graphique d_une courbe dérivée')
plt.grid(True)
plt.show()