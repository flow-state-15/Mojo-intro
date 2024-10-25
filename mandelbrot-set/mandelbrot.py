import matplotlib
matplotlib.use('Agg')  # Use the Agg backend (for image file output) for debugging display
import matplotlib.pyplot as plt
import numpy as np
import warnings
import time

s = time.perf_counter_ns()

warnings.filterwarnings("ignore")

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

# def is_stable(c, num_iterations):
#     z = 0
#     for _ in range(num_iterations):
#         z = z ** 2 + c
#     return abs(z) <= 2
def is_stable(c, num_iterations):
    """
    Check if a complex number 'c' remains bounded under the Mandelbrot iteration.

    Args:
      c: A complex number or an array of complex numbers.
      num_iterations: The maximum number of iterations to perform.

    Returns:
      A boolean or an array of booleans indicating stability.
    """
    mask = np.full(c.shape, True, dtype=bool)  # Initialize a mask with True values
    z = np.zeros_like(c)  # Initialize z as an array of zeros with the same shape as c
    for _ in range(num_iterations):
        z = z**2 + c
        mask = mask & (np.abs(z) <= 2)  # Update the mask based on the stability condition
    return mask  # Return the mask indicating stability

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]

c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
plt.imshow(is_stable(c, num_iterations=20), cmap="binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
# plt.draw() # display backend is not working
plt.savefig('testimg.png') # creating an image instead of display

e = time.perf_counter_ns()
print("execution time in NS: ", e-s)