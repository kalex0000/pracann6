#Develop a fuzzy membership function and visualize different membership types 
(Triangular, Trapezoidal, Gaussian).
import numpy as np
import matplotlib.pyplot as plt
# -------------------------------
# Membership Functions
# -------------------------------
def triangular_mf(x, a, b, c):
    """Triangular membership function"""
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)
def trapezoidal_mf(x, a, b, c, d):
    """Trapezoidal membership function"""
    return np.maximum(
        np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)), 0
    )
def gaussian_mf(x, mean, sigma):
    """Gaussian membership function"""
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2)
# -------------------------------
# Example & Visualization
# -------------------------------
x = np.linspace(0, 10, 200)
triangular = triangular_mf(x, a=2, b=5, c=8)
trapezoidal = trapezoidal_mf(x, a=2, b=4, c=6, d=8)
gaussian = gaussian_mf(x, mean=5, sigma=1.5)
plt.figure(figsize=(8, 6))
plt.plot(x, triangular, label="Triangular MF (a=2, b=5, c=8)")
plt.plot(x, trapezoidal, label="Trapezoidal MF (a=2, b=4, c=6, d=8)")
plt.plot(x, gaussian, label="Gaussian MF (mean=5, σ=1.5)")
plt.title("Fuzzy Membership Functions")
plt.xlabel("Universe of Discourse (x)")
plt.ylabel("Membership Degree μ(x)")
plt.legend()
plt.grid(True)
plt.show()

