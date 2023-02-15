# AUTHOR: Bram Pulles
# Monte Carlo integration visualised
# Using (b-a)/N * sum_i^N f(x_i) ~= integral_a^b f(x) dx

import random
import math
import matplotlib.pyplot as plt

# plotting parameter
resolution_exact = 100

# sampling parameters
number_of_bars = 30
samples_per_bar = 5

# domain of f(x)
a = 0
b = 2 * math.pi

def f(x):
    return math.sin(x)

# list to store all the values for plotting
width = (b - a) / number_of_bars
heights = []

# create the bar heights by integration
for bar in range(number_of_bars):
    values = [random.uniform(width * bar, width * bar + width) for _ in range(samples_per_bar)]
    integral = width / samples_per_bar * sum(map(f, values))
    heights.append(integral / width)

# integral calculation from bars
print('integral from bars:', sum(heights) * width)

# integral calculation pure, i.e. 'one bar'
samples = 10000
values = [random.uniform(a, b) for _ in range(samples)]
integral = (b - a) / samples * sum(map(f, values))
print('integral pure:', integral)

# plot approximation
xs = list(map(lambda x: x * width + width / 2, range(number_of_bars)))
plt.bar(xs, heights, width = 0.8 * width)

# plot exact
xs = list(map(lambda x: x / resolution_exact, range(a, int(b * resolution_exact))))
ys = list(map(f, xs))
plt.plot(xs, ys)

# set domain and show
plt.xlim([a, b])
plt.show()
