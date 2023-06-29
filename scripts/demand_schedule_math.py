import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
matplotlib.rcParams.update({'font.size': 14})

START = 0
END = 16
RESOLUTION = 0.01
DEMAND = 4
CAPACITY = 8

ARROW_HEAD_DISTANCE = 12
ARROW_TAIL_DISTANCE = 16


x = np.arange(START, END, RESOLUTION)

k_dummy = np.repeat(DEMAND, len(x))
k = k_dummy * RESOLUTION
a = np.cumsum(k)
s = np.fmod(a, CAPACITY)
c = np.repeat(CAPACITY, len(x))

fig, ax = plt.subplots()
ax.plot(x, k_dummy, label='$k(t)$', linestyle='dotted', color='black')
ax.plot(x, a, label='$a(t)$', linestyle='dashed', color='black')
ax.plot(x, s, label='$a_f(t, c)$', linestyle='solid', color='black')
ax.plot(x, c, label='_nolegend_', linestyle='solid', color='lightgray')

# https://stackoverflow.com/questions/4624970/finding-local-maxima-minima-with-numpy-in-a-1d-numpy-array
is_spawn = np.r_[True, s[1:] < s[:-1]] & np.r_[s[:-1] < s[1:], True]
is_spawn[0] = False
spawn_indices = np.where(is_spawn)[0]

for i in spawn_indices:
    head = x[i], s[i] + ARROW_HEAD_DISTANCE
    tail = x[i], s[i] + ARROW_TAIL_DISTANCE
    x_, y_ = tail
    dx, dy = head[0] - tail[0], head[1] - tail[1]
    ax.arrow(x_, y_, dx, dy, head_width=0.2, head_length=1, length_includes_head=True, color='red')

ax.set_xlabel('Zeit $t$')
ax.set_ylabel('Kohlemenge')
ax.get_xaxis().set_ticks([0])
ax.get_yaxis().set_ticks([CAPACITY])
ax.set_xticklabels(['$t_0$'])
ax.set_yticklabels(['$c$'])
ax.set_ylim([0, 40])
ax.legend(loc='upper left')


plt.show()
