import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline

def complex_function(x, a, b, c, d, alpha, beta, omega, scale_factor):

    poly_term = a * x**3 + b * x**2 + c * x + d # poly (3rd degree)
    exp_term = np.exp(-alpha * x) # decaying exp
    osc_term = beta * exp_term * np.sin(omega * x) # sine modulated by decaying exp
    
    return scale_factor * (poly_term + osc_term)

import argparse
parser = argparse.ArgumentParser(description='Command line options parser')
parser.add_argument("-is", "--intsetting", type=str, default="cubic", help="Kind of int1d interpolation (linear, cubic....)")
parser.add_argument("-cS", "--cubicSpline", action="store_true", help="Implements cubicSpline interpolation")
args = parser.parse_args()

intsetting = args.intsetting


# -------------- generating sample
N = 30
L = 30.0
x = np.linspace(0, L, N*2, endpoint=False)

a, b, c, d = 0.002, -0.05, 0.5, 5.0
alpha, beta, omega = 0.1, 10.0, 5.0
scale_factor = 5

y = complex_function(x, a, b, c, d, alpha, beta, omega, scale_factor)

# -------------- plot the sample
fig, ax = plt.subplots(2, facecolor='white', gridspec_kw={'height_ratios': [3, 1]}, dpi=580, figsize=(16, 7))
ax[0].scatter(x, y, label="Generated sample",color='royalblue', alpha=0.8, s=12)
ax[1].set_xlabel("x (a.u.)", fontsize=14)
ax[0].set_ylabel("y (a.u.)", fontsize=14)
ax[1].set_ylabel("Residuals", fontsize=14)


# -------------- if cubicSpline
if args.cubicSpline:
  interp = CubicSpline(x, y)

  x_new = np.linspace(0, L-1, N*100, endpoint=False)
  y_new  = interp(x_new)
  y_true = complex_function(x_new, a, b, c, d, alpha, beta, omega, scale_factor)

  # -------------- plot
  ax[0].set_title(f"Interpolation exercise: CubicSpline", fontsize=16)
  ax[0].plot(x_new, y_true, linestyle='--', label="Real function", alpha=0.9, color= 'royalblue')
  ax[0].plot(x_new, y_new, label="Interpolation", alpha=0.9, color= 'firebrick')
  ax[1].plot(x_new, y_true-y_new, alpha=0.8, color= 'grey')
  ax[1].fill_between(x=x_new, y1=y_true-y_new,color= "grey",alpha= 0.2)
  ax[1].set_ylim(-5,5)
  ax[1].axhline(y=0, linestyle='-', alpha=0.7, color='black', linewidth=1)
  ax[1].axhline(y=1, linestyle='--', alpha=0.7, color='black', linewidth=1)
  ax[1].axhline(y=-1, linestyle='--', alpha=0.7, color='black', linewidth=1)
  ax[0].legend(fontsize=14)
  plt.subplots_adjust(wspace=0, hspace=0)
  plt.savefig(f'cubicSpline.png')

  exit()

else:

  # -------------- interpolate
  interp = interp1d(x, y, kind=intsetting) #linear
  x_new = np.linspace(0, L-1, N*100, endpoint=False)
  y_new  = interp(x_new)
  y_true = complex_function(x_new, a, b, c, d, alpha, beta, omega, scale_factor)

  # -------------- plot
  ax[0].set_title(f"Interpolation exercise: {intsetting}", fontsize=16)
  ax[0].plot(x_new, y_true, linestyle='--', label="Real function", alpha=0.9, color= 'royalblue')
  ax[0].plot(x_new, y_new, label="Interpolation", alpha=0.9, color= 'firebrick')
  ax[1].plot(x_new, y_true-y_new, alpha=0.8, color= 'grey')
  ax[1].fill_between(x=x_new, y1=y_true-y_new,color= "grey",alpha= 0.2)
  ax[1].set_ylim(-5,5)
  ax[1].axhline(y=0, linestyle='-', alpha=0.7, color='black', linewidth=1)
  ax[1].axhline(y=1, linestyle='--', alpha=0.7, color='black', linewidth=1)
  ax[1].axhline(y=-1, linestyle='--', alpha=0.7, color='black', linewidth=1)
  ax[0].legend(fontsize=14)
  plt.subplots_adjust(wspace=0, hspace=0)
  plt.savefig(f'interp_{intsetting}.png')


