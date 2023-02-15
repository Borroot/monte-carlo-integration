# AUTHOR: Borroot
# Markov Chain Monte Carlo integration visualised
# Using (b-a)/N * sum_i^N f(x_i) ~= integral_a^b f(x) dx
# and the Markov Chain property

import random
import math
import matplotlib.pyplot as plt

# plotting parameter
resolution_exact = 100
number_of_bars = 500

# sampling parameters
samples = 100000
burnin = 0.2
a = 0
b = 2 * math.pi

def f(x):
    return abs(math.sin(x))

values = []

# create the samples
current = random.uniform(a, b)
for i in range(samples):
    values.append(current)

    # accept a new proposal point with a certain probability
    proposal = random.uniform(a, b)
    acceptance = min(f(proposal) / f(current), 1)

    if random.uniform(0, 1) < acceptance:
        current = proposal

values = values[int(samples * burnin):]

# integral calculation pure, i.e. 'one bar'
integral = (b - a) / samples * sum(map(f, values))
print('integral pure:', integral)

# plot approximation
width = max((b - a) / 100, (b - a) / number_of_bars)
xs = [values[i] for i in range(0, int(samples * burnin), int(samples * burnin / number_of_bars))]
ys = [f(x) for x in xs]
plt.bar(xs, ys, width = width)

# plot exact
xs = list(map(lambda x: x / resolution_exact, range(a, int(b * resolution_exact))))
ys = list(map(f, xs))
plt.plot(xs, ys, color = 'orange')

# set domain and show
plt.xlim([a, b])
plt.show()
