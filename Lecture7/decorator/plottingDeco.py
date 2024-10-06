import numpy as np
from matplotlib import pyplot as plt
import mplhep as hep
from functools import wraps

def hep_style_decorator(style="CMS", lumi="137 $fb^{-1}$", status='preliminary', savefig_name="ciao", palette=plt.cm.Set2.colors):
    def decorator_plot(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            plt.rc('axes', prop_cycle=plt.cycler(color=palette))
            
            fig = func(*args, **kwargs)
            
            # mplhep stuff here
            hep.style.use(style)
            hep.cms.label(rlabel=lumi, llabel=status)
            
            fig.savefig(savefig_name+".png")
            fig.savefig(savefig_name+".pdf")

            return fig 
        return wrapper
    return decorator_plot


@hep_style_decorator(savefig_name="my_sine_func")
def make_plot():
    x = np.linspace(0, 10, 1000, endpoint=False)
    y1 = np.sin(x)
    y2 = np.sin(2 * x)
    y3 = np.sin(3 * x)

    fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
    ax.plot(x, y1, label='sin(x)')
    ax.plot(x, y2, label='sin(2x)')
    ax.plot(x, y3, label='sin(3x)')
    ax.set_xlabel('x (a.u.)', fontsize=16)
    ax.set_ylabel('y (a.u.)', fontsize=16)
    ax.legend()

    return fig 

make_plot()


