import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import convolve as convolve

def fdata(x, L):
    # function for data gen (taken from exercise)
    A = L/10.0
    return 2*np.sin(2*np.pi*x/L) + x*(L-x)**2/L**3 * np.cos(x) + \
           5*x*(L-x)/L**2 + A/2 + 0.1*A*np.sin(13*np.pi*x/L)

def gaussian(x,A,mu,sigma): 
    # custom gaussian function
    return A/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x-mu)**2/(2.*sigma**2))

# ------------ generate data
N = 2048
L = 50.0
x = np.linspace(0, L, N, endpoint=False)
orig = fdata(x, L)
noisy = orig + 0.5*np.random.randn(N)

fig, ax = plt.subplots(figsize=(16, 6), dpi=580, facecolor='white')
ax.set_title( 'Smoothing noisy signal', fontsize=16)
ax.plot(x, noisy, label = 'Noisy data (smeared)', color='dodgerblue',alpha=0.7, linewidth=3)
ax.plot(x, orig, label = 'Clean data', color='royalblue',linewidth=4)
plt.ylabel('y=f(x) (a.u.)', fontsize=13)
plt.xlabel('x (a.u.)', fontsize=13)

# ------------ smoothing with gaussian kernel
kernel_size = 100 
x_kernel = np.linspace(-3, 3, kernel_size)
A, mu = 1, 0

colors = ['purple', 'crimson']

for i,sigma in enumerate([0.1, 1.]):
    gaus = gaussian(x_kernel, A, mu, sigma)
    gaus /= np.sum(gaus)
    res = convolve(noisy, gaus, mode='same')

    ax.plot(x, res, color=colors[i], label=f"Smoothed - sigma {sigma}")



plt.legend()
#plt.show()
plt.savefig('smootingEx.png')
