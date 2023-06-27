from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from sympy.ntheory.primetest import is_gaussian_prime

N = 100
prime_set = set()
for i in range(N):
    for j in range(N):
        if is_gaussian_prime(i + j * 1j):
            prime_set.add(i + j * 1j)
            prime_set.add(i - j * 1j)
            prime_set.add(-i + j * 1j)
            prime_set.add(-i - j * 1j)
primes = np.array(list(prime_set))
plt.figure(figsize=(15, 15))
# sns.set(rc = {'figure.facecolor':(0,0,0,0)})
ax = sns.scatterplot(x=np.real(primes), y=np.imag(primes), color='limegreen', s=35)
# ax.set_aspect('equal')
plt.show()
# plt.savefig('Gaussian_primes.png', transparent=True)