#!/usr/bin/env python3

# written following https://nialltl.neocities.org/articles/mpm_guide.html
import taichi as ti
import time

ti.init()

N = 10000
e = 2.71
dt = 2e-3

X = ti.Vector.field(2, float, N)  # material coords
x = ti.Vector.field(2, float, N)


@ti.kernel
def advance(t: ti.f32):
    t = t*dt
    for i in X:
        # Equations of motion update
        x[i][0] = X[i][0]
        x[i][1] = X[i][1]-5*t


@ti.kernel
def init():
    for i in X:
        X[i] = [ti.random()*0.4+0.3, ti.random()*0.4+0.3]


init()
gui = ti.GUI('Equation of Motion')
i = 0
while gui.running:
    advance(i)
    gui.circles(x.to_numpy(), radius=1.5, color=0x068587)
    gui.show()
    i += 1
