import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 初始化参数
fig, ax = plt.subplots(figsize=(9, 9))
fig.patch.set_facecolor('k')
ax.set_facecolor('k')
ax.set_xlim(0, 400)
ax.set_ylim(0, 400)
ax.set_aspect('equal')
ax.axis('off')

# 初始化点
i = np.arange(0, int(2e4) + 1)
x = np.mod(i, 100)
y = np.floor(i / 100)
k = x / 4 - 12.5
e = y / 9 + 5
o = np.linalg.norm(np.vstack([k, e]), axis=0) / 9

scat = ax.scatter([], [], s=2, c='w', marker='o', edgecolors='none', alpha=0.4)

t = [0]  # 用列表以便在 update 中修改

def update(frame):
    t[0] += np.pi / 90
    q = x + 99 + np.tan(1. / (k + 1e-8)) + o * k * (np.cos(e * 9) / 4 + np.cos(y / 2)) * np.sin(o * 4 - t[0])
    c = o * e / 30 - t[0] / 8
    px = (q * 0.7 * np.sin(c)) + 9 * np.cos(y / 19 + t[0]) + 200
    py = 200 + (q / 2 * np.cos(c))
    scat.set_offsets(np.c_[px, py])
    return scat,

ani = animation.FuncAnimation(
    fig, update, interval=16, blit=True
)

plt.show() 