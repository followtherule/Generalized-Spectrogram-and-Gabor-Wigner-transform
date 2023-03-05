# Generalied Spectrogram

Analysing 1-dim input data by using Generalized Spectrogram, which is one solution to alleviate the impact from the uncertainty principle in time-frequency analysis.

## Usage

y = GS(x,t,f,B,sgm1,sgm2,a,b)
x: input signal
t: time-axis
f: frequency-axis
B: bandwidth of the window function
sgm1: control the width of the first gaussian window
sgm2: control the width of the second gaussian window
a: magnification of the first Gabor transform
b: magnification of the second Gabor transform
y: output the Generalized Spectrogram $G_{sgm1}^a \overline{G_{sgm2}^b}$

## example

![](https://i.imgur.com/0xWRZ4c.png)

# Gabor-Wigner transform

Analysing 1-dim input data by using Gabor-Wigner transform, which attains high accuracy in both time-domain and frequency domain.

## Usage

y = GW(x,t,f,B,sgm,a,b)
x: input signal
t: time-axis
f: frequency-axis
B: bandwidth of the window function used in the Gabor transform
sgm: control the width of the gaussian window used in the Gabor transform
a: magnification of the Gabor transform
b: magnification of the Wigner transform
y: output the Gabor-Wigner transform $G^a W^b$

## example

![](https://i.imgur.com/vI7eIMq.png)
