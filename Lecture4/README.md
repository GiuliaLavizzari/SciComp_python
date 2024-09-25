# Smoothing exercise

After generating and smearing the data as illustrated in the exercise, Scipy `convolute` is used to smooth them, considering a gaussian kernel.
Several values of the parameter sigma were tested: here we plot two, showing that lower values of sigma result in smaller smoothing effects.
![alt text](https://github.com/GiuliaLavizzari/SciComp_python/blob/b15f433089786e47fb70b44b792c82647f89af5a/Lecture4/smoothing/smootingEx.png)

# Interpolation exercise

A function is created (A sine dumped by a decaying exponential, summed to a polynomial term) and used to generate a sample.

Interpolation of such sample is then performed, either using scipy CubicSpline (`--cubicSpline`) or via interp1d (the kind of interpolation can be specified via the `--intsetting` argument).
Residuals are computed as Ytrue (i.e. the actual function) -  Yinterpolated (i.e. the interpolated function). Some results are shown in the next sections.

### CubicSpline:
![alt text](https://github.com/GiuliaLavizzari/SciComp_python/blob/7aa0203c1b65e71d779e97099cf5bdaceb33fdd6/Lecture4/interpolation/cubicSpline.png)

### interp1d
![alt text](https://github.com/GiuliaLavizzari/SciComp_python/blob/7aa0203c1b65e71d779e97099cf5bdaceb33fdd6/Lecture4/interpolation/interp_quadratic.png)
![alt text](https://github.com/GiuliaLavizzari/SciComp_python/blob/7aa0203c1b65e71d779e97099cf5bdaceb33fdd6/Lecture4/interpolation/interp_linear.png)
