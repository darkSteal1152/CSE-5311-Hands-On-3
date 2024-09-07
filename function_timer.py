import time
import numpy as np
import matplotlib.pyplot as plt

def f(n):
    x = 1
    for i in range(1, n):
        for j in range(1, n):
            x = x + 1

    return x

input_values = np.concatenate([np.arange(1, 10), np.arange(10, 100, 10), np.arange(100, 1000, 100), np.arange(1000, 10000, 1000)])
times = []

for n in  input_values:
    start_time = time.time()
    f(n)
    times.append(time.time() - start_time)

polynomial_coefficients = np.polyfit(input_values, times, 2)
polynomial = np.poly1d(polynomial_coefficients)

fitted_times = polynomial(input_values)

plt.plot(input_values, times, label="Observed f(n)")
plt.plot(input_values, fitted_times, label="Estimated f(n)", linestyle="--")
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Function Benchmark')
plt.legend()
plt.grid(True)
plt.show()

print(polynomial)
