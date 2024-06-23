# Antisymmetric function

import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk


def set_k1(value):
    global k1
    k1 = float(value)
    function_selected(True)


def set_k2(value):
    global k2
    k2 = float(value)
    function_selected(True)


def function_selected(event):
    global combo_func
    global zz0, zz1, zz0_min, zz0_max, zz1_min, zz1_max
    global z_min0, z_max0, z_min1, z_max1
    global ax0, ax1
    global plt0, plt1
    # print(combo_func.get())
    if combo_func.get() == option_func[0]:
        ax0.set_title(title_ax0 + "x + y")
        ax1.set_title(title_ax1 + "x - y")
        zz0 = xx + yy
        zz1 = xx - yy
    elif combo_func.get() == option_func[1]:
        ax0.set_title(title_ax0 + "x**2 + y**2")
        ax1.set_title(title_ax1 + "x**2 - y**2")
        zz0 = xx ** 2 + yy ** 2
        zz1 = xx ** 2 - yy ** 2
    elif combo_func.get() == option_func[2]:
        ax0.set_title(title_ax0 + "(x + y)**2")
        ax1.set_title(title_ax1 + "(x - y)**2")
        zz0 = (xx + yy) ** 2
        zz1 = (xx - yy) ** 2
    elif combo_func.get() == option_func[3]:
        ax0.set_title(title_ax0 + "cos(x/100) + cos(y/100)")
        ax1.set_title(title_ax1 + "cos(x/100) - cos(y/100)")
        zz0 = np.cos(xx / 100) + np.cos(yy / 100)
        zz1 = np.cos(xx / 100) - np.cos(yy / 100)
    elif combo_func.get() == option_func[4]:
        ax0.set_title(title_ax0 + "cos(x/100 + y/100)")
        ax1.set_title(title_ax1 + "cos(x/100 - y/100)")
        zz0 = np.cos(xx / 100 + yy / 100)
        zz1 = np.cos(xx / 100 - yy / 100)
    elif combo_func.get() == option_func[5]:
        ax0.set_title(title_ax0 + "e**(ix/100 + iy / 100)(real)")
        ax1.set_title(title_ax1 + "e**(ix/100 - iy / 100)(real)")
        zz0 = np.real(np.exp(1j * (xx / 100) + 1j * (yy / 100)))
        zz1 = np.real(np.exp(1j * (xx / 100) - 1j * (yy / 100)))
    elif combo_func.get() == option_func[6]:
        ax0.set_title(title_ax0 + "e**(ik1x/400 + ik2y/400) + e**(ik1y/400 + ik2x/400)(real)")
        ax1.set_title(title_ax1 + "e**(ik1x/400 + ik2y/400) - e**(ik1y/400 + ik2x/400)(real)")
        zz0 = np.real(np.exp(1j * (k1 * xx / 400) + 1j * (k2 * yy / 400)) + np.exp(1j * (k1 * yy / 400) + 1j * (k2 * xx / 400)))
        zz1 = np.real(np.exp(1j * (k1 * xx / 400) + 1j * (k2 * yy / 400)) - np.exp(1j * (k1 * yy / 400) + 1j * (k2 * xx / 400)))
    else:
        pass
    zz0_min = np.min(zz0)
    zz0_max = np.max(zz0)
    zz1_min = np.min(zz1)
    zz1_max = np.max(zz1)
    if zz0_min == zz0_max:
        zz0_min -= 1.
        zz0_max += 1.
    if zz1_min == zz1_max:
        zz1_min -= 1.
        zz1_max += 1.
    z_min0 = np.round(zz0_min)
    z_max0 = np.round(zz0_max)
    z_min1 = np.round(zz1_min)
    z_max1 = np.round(zz1_max)
    ax0.set_zlim(z_min0, z_max0)
    ax1.set_zlim(z_min1, z_max1)
    plt0.remove()
    plt1.remove()
    plt0 = ax0.plot_wireframe(xx, yy, zz0, linewidth=1, rstride=100, cstride=100)
    plt1 = ax1.plot_wireframe(xx, yy, zz1, linewidth=1, rstride=100, cstride=100)


def update_diagrams():
    pass


# Animation control
def reset():
    global is_play, cnt
    is_play = False
    cnt = 0
    update_diagrams()


def switch():
    global is_play
    if is_play:
        is_play = False
    else:
        is_play = True


def update(f):
    global cnt
    # global txt_step
    # txt_step.set_text("Step=" + str(cnt))
    if is_play:
        cnt += 1
        update_diagrams()


# Global variables
# Animation control
cnt = 0
is_play = False

# Data structure
range_xy = 1000
x = np.arange(- range_xy, range_xy)
y = np.arange(- range_xy, range_xy)
xx, yy = np.meshgrid(x, y)
zz0 = xx + yy
zz1 = xx - yy

zz0_min = np.min(zz0)
zz0_max = np.max(zz0)
zz1_min = np.min(zz1)
zz1_max = np.max(zz1)

k1 = 1.
k2 = 1.

# Generate figure and axes
title_tk = "Antisymmetric function"
title_ax0 = "Symmetric:\n"
title_ax1 = "Antisymmetric:\n"

x_min0 = - range_xy
x_max0 = range_xy
y_min0 = x_min0
y_max0 = x_max0
z_min0 = np.round(zz0_min)
z_max0 = np.round(zz0_max)

x_min1 = - range_xy
x_max1 = range_xy
y_min1 = x_min1
y_max1 = x_max1
z_min1 = np.round(zz1_min)
z_max1 = np.round(zz1_max)

fig = Figure()
ax0 = fig.add_subplot(121, projection='3d')
ax0.set_box_aspect((4, 4, 4))
ax0.grid()
ax0.set_title(title_ax0 + "x + y")
ax0.set_xlabel('x')
ax0.set_ylabel('y')
ax0.set_zlabel('z')
ax0.set_xlim(x_min0, x_max0)
ax0.set_ylim(y_min0, y_max0)
ax0.set_zlim(z_min0, z_max0)

ax1 = fig.add_subplot(122, projection='3d')
ax1.set_box_aspect((4, 4, 4))
ax1.grid()
ax1.set_title(title_ax1 + "x - y")
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.set_xlim(x_min1, x_max1)
ax1.set_ylim(y_min1, y_max1)
ax1.set_zlim(z_min1, z_max1)

# Text items
'''
txt_step = ax0.text2D(x_min0, y_max0, "Step=" + str(0))
xz, yz, _ = proj3d.proj_transform(x_min0, y_max0, z_max0, ax0.get_proj())
txt_step.set_position((xz, yz))
'''

# Plot items
plt0 = ax0.plot_wireframe(xx, yy, zz0, linewidth=1, rstride=100, cstride=100)
plt1 = ax1.plot_wireframe(xx, yy, zz1, linewidth=1, rstride=100, cstride=100)

# Embed in Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Animation
'''
frm_anim = ttk.Labelframe(root, relief='ridge', text='Animation', labelanchor='n')
frm_anim.pack(side='left', fill=tk.Y)
btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
btn_play.pack(side='left')
btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
btn_reset.pack(side='left')
'''

# Function
frm_func = ttk.Labelframe(root, relief='ridge', text='Function', labelanchor='n')
frm_func.pack(side='left', fill=tk.Y)
option_func = ["x+-y", "x**2+-y**2", "(x+-y)**2", "cos(x)+-cos(y)", "cos(x+-y)",
               "e**(ix+-iy)", "e**(ik1x+ik2y)+-e**(ik1y+ik2x)"]
variable = tk.StringVar()
combo_func = ttk.Combobox(frm_func, values=option_func, textvariable=variable, width=30)
combo_func.set(option_func[0])
combo_func.bind("<<ComboboxSelected>>", function_selected)
combo_func.pack()

# k1, k2
frm_k = ttk.Labelframe(root, relief="ridge", text="k1, k2", labelanchor="n")
frm_k.pack(side='left', fill=tk.Y)

lbl_k1 = tk.Label(frm_k, text="k1:")
lbl_k1.pack(side='left')
var_k1 = tk.StringVar(root)
var_k1.set(str(k1))
spn_k1 = tk.Spinbox(
    frm_k, textvariable=var_k1, format="%.1f", from_=-6., to=6., increment=0.5,
    command=lambda: set_k1(var_k1.get()), width=6
    )
spn_k1.pack(side='left')

lbl_k2 = tk.Label(frm_k, text="k2:")
lbl_k2.pack(side='left')
var_k2 = tk.StringVar(root)
var_k2.set(str(k2))
spn_k2 = tk.Spinbox(
    frm_k, textvariable=var_k2, format="%.1f", from_=-6., to=6., increment=0.5,
    command=lambda: set_k2(var_k2.get()), width=6
    )
spn_k2.pack(side='left')

# main loop
anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
root.mainloop()
