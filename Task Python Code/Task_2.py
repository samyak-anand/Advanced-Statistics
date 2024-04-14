"""
Let 𝑌 be the random variable with the time to hear an owl from your room’s open window (in
hours). Assume that the probability that you still need to wait to hear the owl after 𝑦 hours is one
of the following:
a) If 𝜉4 is 0: the probability is given by 𝜉5e−𝜉6𝑦+𝜉7e−𝜉8𝑦
b) If 𝜉4 is 1: the probability is given by 𝜉5e−𝜉6𝑦2+𝜉7e−𝜉8𝑦8
c) If 𝜉4 is 2: the probability is given by 𝜉5e−𝜉6√𝑦+𝜉7 e-𝜉8 √𝑦3
d) If 𝜉4 is 3: the probability is given by 𝜉5e−𝜉6 𝑦2+𝜉7e−𝜉8𝑦2
Find the probability that you need to wait between 2 and 4 hours to hear the owl, compute and
display the probability density function graph as well as a histogram by the minute. Compute and
display in the graphics the mean, variance, and quartiles of the waiting times. Please pay
attention to the various units of time!

"""

import numpy as np
from matplotlib import pyplot as plt

def cdf(x):
    return 1 - (np.exp(-4*x**2) * 41/99 + np.exp(-3*x**2) * 58 / 99)
def pdf(x):
    return (np.exp(-4*x**2) * 3.31 + np.exp(-3*x**2) *3.51)
#CDF
x = np.linspace(0, 1, 200)
fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(x, cdf(x), color='y')
ax.axvline(0.03795, color='b', label=f'25th percentile')
ax.axvline(0.0914, color='r', label=f'50th percentile')
ax.axvline(0.18288, color='g', label=f'75th percentile')
plt.xlabel('Count', fontsize='10')
plt.ylabel('Value', fontsize='10')
plt.title("CDF")
ax.legend()
plt.show()

#PDF
x = np.linspace(0, 1, 200)
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, pdf(x), color='y')
ax.axvline(0.03795, color='b', label=f'25th percentile')
ax.axvline(0.0914, color='r', label=f'50th percentile')
ax.axvline(0.18288, color='g', label=f'75th percentile')
plt.xlabel('Count', fontsize='10')
plt.ylabel('Value', fontsize='10')
plt.title("PDF")
ax.legend()
plt.show()


cdf_=cdf(4) - cdf(2)
print ("CDF is:",cdf_ )
data = cdf(x)
fig, ax = plt.subplots(figsize=(10, 4))
plt.hist(data, bins=np.arange(min(data), max(data) + 1/60, 1/60))
plt.xlabel('Count', fontsize='10')
plt.ylabel('Value', fontsize='10')
plt.title("Histogram")
plt.show()
