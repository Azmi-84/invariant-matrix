import numpy as np
import matplotlib.pyplot as plt

a_val = 1
c_values = np.linspace(-230, 230, 10)

x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

psi = a_val * (X**2 * Y - (Y**3)/3)

plt.figure(figsize=(12, 6))
contour = plt.contour(X, Y, psi, levels=c_values, colors='blue')
plt.clabel(contour, inline=True, fontsize=8)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True, alpha=0.5)
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.savefig('stream_function_plot.svg', format='svg')
plt.show()