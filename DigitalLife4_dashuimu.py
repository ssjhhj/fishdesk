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
i = np.arange(0, int(4e4) + 1)
x = np.mod(i, 200)
y = i / 200.0
k = x / 8.0 - 12.5
e = y / 8.0 - 12.5
o = (k ** 2 + e ** 2) / 169.0
d = 0.5 + 5.0 * np.cos(o)

scat = ax.scatter([], [], s=1, c='w', marker='o', edgecolors='none', alpha=0.4)

t = [0]  # 用列表以便在 update 中修改

def update(frame):
    t[0] += np.pi / 120
    px = x + d * k * np.sin(d * 2 + o + t[0]) + e * np.cos(e + t[0]) + 100
    py = y / 4 - o * 135 + d * 6 * np.cos(d * 3 + o * 9 + t[0]) + 275
    color = ((d * np.sin(k) * np.sin(t[0] * 4 + e)) ** 2)
    rgb = np.stack([color, color, color], axis=1)
    rgb = np.clip(rgb, 0, 1)  # 保证颜色在0~1范围
    scat.set_offsets(np.c_[px, py])
    scat.set_facecolor(rgb)
    return scat,

ani = animation.FuncAnimation(
    fig, update, interval=16, blit=True
)

plt.show() 