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
x = i
y = i / 235.0
e = y / 8.0 - 13.0

scat = ax.scatter([], [], s=2, c='w', marker='o', edgecolors='none', alpha=0.4)

t = [0]  # 用列表以便在 update 中修改

def update(frame):
    t[0] += np.pi / 240
    k = (4 + np.sin(y * 2 - t[0]) * 3) * np.cos(x / 29)
    d = np.sqrt(k ** 2 + e ** 2)
    q = 3 * np.sin(k * 2) + 0.3 / (k + 1e-8) + np.sin(y / 25) * k * (9 + 4 * np.sin(e * 9 - d * 3 + t[0] * 2))
    px = q + 30 * np.cos(d - t[0]) + 200
    py = 620 - q * np.sin(d - t[0]) - d * 39
    scat.set_offsets(np.c_[px, py])
    return scat,

ani = animation.FuncAnimation(
    fig, update, interval=16, blit=True
)

plt.show() 