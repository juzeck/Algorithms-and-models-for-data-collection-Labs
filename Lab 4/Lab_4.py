import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


def equilateral_triangle_vertices(side_length):
    height = np.sqrt(3) / 2 * side_length
    return np.array([
        [0, 0],
        [side_length, 0],
        [side_length / 2, height],
        [0, 0]
    ])


def v_shape(center, size):
    return np.array([
        [center[0] - size / 2, center[1] - size / 2],
        [center[0], center[1]],
        [center[0] + size / 2, center[1] - size / 2]
    ])


def interpolate_point(p1, p2, t):
    return p1 + (p2 - p1) * t


def create_animation_frames(triangle, v_size, num_frames):
    frames = []
    num_sides = len(triangle) - 1
    for i in range(num_sides):
        p1 = triangle[i]
        p2 = triangle[(i + 1) % num_sides]
        for t in np.linspace(0, 1, num_frames // num_sides):
            center = interpolate_point(p1, p2, t)
            v_points = v_shape(center, v_size)
            frames.append(v_points)
    return frames


def animate_and_save_gif(frames, triangle, filename, side_length):
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, side_length + 0.5)
    ax.set_ylim(-0.5, np.sqrt(3) / 2 * side_length + 0.5)
    line, = ax.plot([], [], lw=2)
    triangle_line, = ax.plot(triangle[:, 0], triangle[:, 1], 'b-')

    def init():
        line.set_data([], [])
        return line, triangle_line

    def animate(i):
        x = frames[i][:, 0]
        y = frames[i][:, 1]
        line.set_data(x, y)
        return line, triangle_line

    ani = animation.FuncAnimation(fig, animate, init_func=init,
                                  frames=len(frames), interval=50, blit=True)

    ani.save(filename, writer='pillow')


def main():
    side_length = 5
    v_size = 1
    num_frames = 150
    triangle = equilateral_triangle_vertices(side_length)
    frames = create_animation_frames(triangle, v_size, num_frames)
    animate_and_save_gif(frames, triangle, 'animation_v.gif', side_length)


if __name__ == '__main__':
    main()
