<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>

# PyTaucPlot
Calculate band gap from UV-vis spectrum.

Created and maintained by Yucheng Lan, Kit Sze, and Ben Ogueri

## versions
1. Version 0.21.01: Standardized plot of UV-vis spectrum and Tauc plots.  Manually input data, output figures, and find bandgaps.
2. Version 0.22.01: Machine Learning is introduced to find bandgaps
3. Version 0.22.05: GUI (coming)

# Background of UV-vis spectroscopy
## Absorptance
1. Absorptance is defined as the ratio of the radiant flux absorbed by a body, to the incident upon it. $ (I_0 - I) / I_0 $.  Absorptance depends on the size of the object as well as the concentration of the material.

## Absorbance
1. Absorbance is defined as $ log_{10} (I_0 / I)$, where $I_0$ is the intensity of the incident light, and $I$ is the intensity of the light that passed through the sample.  The light is monochromatic and set to a specified wavelength. 
2. The absorbance depends on the concentration of the sample and size of the sample. 
3. The absorbance of a solution is linearly proportional to the concentration, according to the Beer - Lambert law, if the $I_0 / I$ value lie between 0.2 and 0.7. 
4. When absorbance is defined in fields other than chemistry, it is defined as $ log_e (I_0 / I)$.

## absorption coefficient $\alpha$
1. In the case of negligible light scattering, the rate of light absorption can be well described by the Beer–Lambert law.  $I (x) = I_0 e^{- \alpha x}$ 
2. Absorption Coefficient = ln(Incident Power/Absorbed Power)*(Thickness of material^-1)
3. $\alpha = ln ( I_0 / (I_0 - I) / l$
4. unit: 1/centimeter, cm-1

## absorption coefficient $\alpha$ and absorbance $A$
1. $A = ln (I_0 / I)$ or $A = log_{10} (I_0 / I)$ 
2. $\alpha = A / d$ or $\alpha = A / d * ln10$ where $d$ is the thickness of samples
3. absorptance $fA = (I0 - I) / I0 = 1 - 10^(-A)$

## difference between absorbance and absorptance
1. Absorbance varies linearly with the concentration, while absorptance varies nonlinearly.
2. Absorptance is the flux ratio of the object, while absorbance is the log value of the intensity ratio.
3. Absorptance is a measurement of the flux that has been absorbed, while absorbance is a measurement of flux that has passed through.

