#using numpy module to read data in # much faster than CSV module 
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline #for smooth points


#loading data
# x in nm
# y is absorbance A or absorption coefficient alpha
# absorptance fA = (I0-I)/I0 = 1 - 10^(-A)
# A = ln (I/I0); alpha = ln10 * A / length in centimeter
# absorption coefficient alpha ~ absorbance A
# absorption coefficient: cm-1
x_Ca200, y_Ca200 = np.loadtxt('Ca2MnWO6.csv', delimiter=',', unpack=True) # step = 0.1nm; start: 200 nm
x_Ca175, y_Ca175 = np.loadtxt('Ca1.75Sr0.25MnWO6.csv', delimiter=',', unpack=True) # step = 0.1nm; start: 200 nm
x_Ca150, y_Ca150 = np.loadtxt('Ca1.5Sr0.5MnWO6.csv', delimiter=',', unpack=True) # step = 0.1nm; start: 200 nm
x_Ca100, y_Ca100 = np.loadtxt('Ca1Sr1MnWO6.csv', delimiter=',', unpack=True) # step = 0.1nm; start: 200 nm
x_Ca50, y_Ca50 = np.loadtxt('Ca0.5Sr1.5MnWO6.csv', delimiter=',', unpack=True) # step = 0.1nm; start: 200 nm
x_Ca25, y_Ca25 = np.loadtxt('Ca0.25Sr1.75MnWO6.csv', delimiter=',', unpack=True) # step = 0.1nm; start: 200 nm
x_Ca0, y_Ca0 = np.loadtxt('Sr2MnWO6.csv', delimiter=',', unpack=True) # step = 0.1nm; start: 200 nm


plt.figure("(CaSr)MnWO6: Tauc Plot")

#figure size etc?
#fig = plt.figure(figsize=(8,4), dpi=100)
plt.figure(figsize=(3,4.85))

#for n= 1/2 direct allowed
#plt.scatter(1239.8 / x, (y * 1239.8 / x)**2, marker = 'x', label='n = 1/2, direct allowed, 1.88 eV') # nm -> eV: 1239.8 / x
plt.scatter(1239.8 / x_Ca200, (y_Ca200 * 1239.8 / x_Ca200)**2, marker = 'x', label='x = 2.00') #Ca$_2$MnWO$_6$') # n = 1/2, direct allowed, 2.30 eV') # nm -> eV: 1239.8 / x
plt.scatter(1239.8 / x_Ca175, (y_Ca175 * 1239.8 / x_Ca175)**2, marker = 'o', label='x = 1.75') # Ca$_{1.75}$Sr$_{0.25}$)MnWO$_6$') # n = 1/2, direct allowed, 1.90 eV') # nm -> eV: 1239.8 / x
plt.scatter(1239.8 / x_Ca150, (y_Ca150 * 1239.8 / x_Ca150)**2, marker = 'v', label='x = 1.50') #(Ca$_{1.5}$Sr$_{0.5}$)MnWO$_6$') # n = 1/2, direct allowed, 1.78 eV') # nm -> eV: 1239.8 / x
plt.scatter(1239.8 / x_Ca100, (y_Ca100 * 1239.8 / x_Ca100)**2, marker = '^', label='x = 1.00') #(CaSr)MnWO$_6$') # n = 1/2, direct allowed, 1.68 eV') # nm -> eV: 1239.8 / x
plt.scatter(1239.8 / x_Ca50, (y_Ca50 * 1239.8 / x_Ca50)**2, marker = 's', label='x = 0.50') #(Ca$_{0.5}$Sr$_{1.5}$)MnWO$_6$') # n = 1/2, direct allowed, 1.75 eV') # nm -> eV: 1239.8 / x
plt.scatter(1239.8 / x_Ca25, (y_Ca25 * 1239.8 / x_Ca25)**2, marker = 'D', label='x = 0.25') #(Ca$_{0.25}$Sr$_{1.75}$)MnWO$_6$') # n = 1/2, direct allowed, 1.83 eV') # nm -> eV: 1239.8 / x
plt.scatter(1239.8 / x_Ca0, (y_Ca0 * 1239.8 / x_Ca0)**2, marker = '*', label='x = 0.00') #Sr$_2$MnWO$_6$') # n = 1/2, direct allowed, 2.28 eV') # nm -> eV: 1239.8 / x
# for n = 3/2 direct forbidden
#plt.scatter(1239.8 / x, (y * 1239.8 / x)**(2/3), label='n = 3/2, direct forbidden') # nm -> eV: 1239.8 / x
# for n = 2 indirect allowed
#plt.plot(1239.8 / x, (y * 1239.8 / x)**(1/2), label='n = 2, n = 2 indirect allowed') # nm -> eV: 1239.8 / x
# for n= 3 indirect forbidden
#plt.plot(1239.8 / x, (y * 1239.8 / x)**(1/3), label='n = 3, n = 3 indirect forbidden') # nm -> eV: 1239.8 / x
plt.xlabel(r'Photon energy $h \nu$ (eV)', fontsize=12)
#for n= 1/2
plt.ylabel(r'$(\alpha h \nu)^{2}$ (cm$^{-1}$ $\cdot$ eV)$^{2}$', fontsize=12) # n = 1/2 here
#for n= 3/2
#plt.ylabel(r'$(\alpha h \nu)^{1/n}$ $(cm^{-1} \times eV)^{2/3}$', fontsize=12)
#for n= 2
#plt.ylabel(r'$(\alpha h \nu)^{1/n}$ $(cm^{-1} \times eV)^{1/2}$', fontsize=12)
#for n= 3
#plt.ylabel(r'$(\alpha h \nu)^{1/n}$ $(cm^{-1} \times eV)^{1/3}$', fontsize=12)
plt.xlim(1, 4)
plt.ylim(0,5.1)
plt.tick_params(axis="y",direction="in", labelsize=10)
plt.tick_params(axis="x",direction="in", labelsize=10)
#plt.title('Tauc Plots')
plt.legend(frameon=False)
plt.tight_layout()

# linear fitting of least squares ?
# bandgap ?

# prepare data for fitting in Tauc plot
# x_tauc in eV: hv = ?
#x_fitting = x[3000 : 6000]
#y_fitting = y[3000 : 6000]

#prepare data for Tauc plots
#x_tauc = 1239.8 / x_fitting # hv = hc / lambda = 12398 in eV nm / lambda in nm
# y_tauc: (a eV)^(1/n) ~ hv - Eg
# n = 1/2 direct allowed
#y_tauc1 = (y_fitting * x_tauc)**2
# n = 3/2 direct forbidden
#y_tauc2 = (y_fitting * x_tauc)**(2/3)
# n = 2 indirect allowed
#y_tauc3 = (y_fitting * x_tauc)**(1/2)
# n = 3 indirect forbidden
#y_tauc4 = (y_fitting * x_tauc)**(1/3)


#save figure
#plt.savefig('test.png', dpi=100)
plt.savefig('(CaSr)MnWO6_TaucPlot.pdf', dpi=500)

plt.show()





