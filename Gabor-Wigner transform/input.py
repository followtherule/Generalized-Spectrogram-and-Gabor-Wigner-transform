import numpy as np

global inputs

# set your inputs here
dt = 0.05
df = 0.01
t1 = np.linspace(0.0, 9.95, 200)
t2 = np.linspace(10.0, 19.95, 200)
t3 = np.linspace(20.0, 30.0, 201)
t = np.linspace(0.0, 30.0, 601)
x1 = np.cos(2 * np.pi * t1)
x2 = np.cos(6 * np.pi * t2)
x3 = np.cos(4 * np.pi * t3)
x = np.concatenate((x1, x2, x3), axis = None)
f = np.linspace(-5.0, 5.0, 1001)
B = 2.5
sgm = 0.1
a = 2.6
b = 0.7

inputs = x, t, f, B, sgm, a, b