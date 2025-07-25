import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 初始化全局时间变量
t = 0.0

def calculate_points(t_val):
    """向量化计算所有点的坐标"""
    # 生成i的向量化数组（40000到1的倒序）
    i = np.arange(40000, 0, -1, dtype=np.float64)
    
    # 计算基础参数
    x = i % 200
    y = i / 400.0
    
    # 计算k分量（x/8 - 12.5）
    k = x / 8.0 - 12.5
    
    # 计算d分量（cos(k/2) + sin(y/3) - 0.5）
    d = np.cos(k / 2.0) + np.sin(y / 3.0) - 0.5
    
    # 计算q分量（核心公式）
    q = (x / 4.0) + 60.0 + d * k * (1.0 + np.cos(4.0 * d - 2.0 * t_val + y / 14.0))
    
    # 计算c中间变量（y*d/169 - t/8 + d/9）
    c = (y * d) / 169.0 - t_val / 8.0 + d / 9.0
    
    # 计算最终坐标
    px = q * 0.7 * np.cos(c) + 200.0 + 60.0 * np.sin( (3.0 * t_val)/32.0 + c/4.0 )
    py = (q + 59.0) * 0.7 * np.sin(c) + 200.0
    
    return px, py

def update(frame):
    global t
    # 时间递增（t += PI/30）
    t += np.pi / 20
    
    # 清空画布并设置参数
    ax.clear()
    ax.set_facecolor((0, 0, 0))  # 黑色背景
    ax.set_xlim(0, 400)          # 400x400画布
    ax.set_ylim(0, 400)
    ax.set_aspect('equal')
    ax.invert_yaxis()            
    
    # 计算并绘制点（白色，透明度≈0.14）
    px, py = calculate_points(t)
    ax.scatter(px, py, s=1, c='white', alpha=36/255, edgecolors='none')

# 初始化图形
fig, ax = plt.subplots(figsize=(4, 4))
fig.patch.set_facecolor((0, 0, 0))  # 窗口背景黑色
ax.set_facecolor((0, 0, 0))         # 坐标轴背景黑色

# 创建动画（约60帧/秒）
ani = animation.FuncAnimation(
    fig, update,
    interval=16,  # 16ms间隔≈60fps
    blit=False,
    frames=300
)

ani.save(
    '3.gif',
    writer='pillow',
    fps=45,                   # 帧率（决定每秒钟显示多少帧）
    dpi=72
)

plt.show()
