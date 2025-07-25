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
i = np.arange(0, int(1e4) + 1)
x = np.mod(i, 200)
y = i / 55.0
k = 9.0 * np.cos(x / 8.0)
e = y / 8.0 - 12.5

scat = ax.scatter([], [], s=1, c='w', marker='o', edgecolors='none', alpha=0.4)

t = [0]  # 用列表以便在 update 中修改

def update(frame):
    t[0] += np.pi / 120
    d = (k ** 2 + e ** 2) / 99.0 + np.sin(t[0]) / 6.0 + 0.5
    q = 99 - e * np.sin(np.arctan2(k, e) * 7) / d + k * (3 + np.cos(d ** 2 - t[0]) * 2)
    c = d / 2.0 + e / 69.0 - t[0] / 16.0
    px = q * np.sin(c) + 200
    py = (q + 19 * d) * np.cos(c) + 200
    scat.set_offsets(np.c_[px, py])
    return scat,

ani = animation.FuncAnimation(
    fig, update, interval=16, blit=True
)

plt.show() 