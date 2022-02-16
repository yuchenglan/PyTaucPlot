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

plt.figure("(CaSr)MnWO6: Tauc Plot")

#figure size etc?
#fig = plt.figure(figsize=(8,4), dpi=100)
plt.figure(figsize=(3,4.85))

#for n= 1/2 direct allowed
plt.scatter(1239.8 / x_Ca200, (y_Ca200 * 1239.8 / x_Ca200)**2, marker = 'x', label='x = 2.00') #Ca$_2$MnWO$_6$') # n = 1/2, direct allowed, 2.30 eV') # nm -> eV: 1239.8 / x
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
plt.ylim(0, np.max(y_Ca200)*1.2)
plt.tick_params(axis="y",direction="in", labelsize=10)
plt.tick_params(axis="x",direction="in", labelsize=10)
#plt.title('Tauc Plots')
plt.legend(frameon=False)
plt.tight_layout()

#save figure
#plt.savefig('test.png', dpi=100)
plt.savefig('(CaSr)MnWO6_TaucPlot.pdf', dpi=500)

plt.show()





