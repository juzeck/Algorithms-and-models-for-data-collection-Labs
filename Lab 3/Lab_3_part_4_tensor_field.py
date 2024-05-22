import numpy as np
import matplotlib.pyplot as plt
import glyph_visualization_lib as gvl


def main():
    x = np.linspace(-2, 2, 8, dtype=float, endpoint=True)
    y = np.linspace(-2, 2, 8, dtype=float, endpoint=True)
    z = np.linspace(-2, 2, 8, dtype=float, endpoint=True)

    X, Y, Z = np.meshgrid(x, y, z)

    stress_tensor = np.array([
        [np.exp(-X ** 2), np.sin(X + Y), np.sin(X + Z)],
        [np.sin(X + Y), np.exp(-Y ** 2), np.sin(Y + Z)],
        [np.sin(X + Z), np.sin(Y + Z), np.exp(-Z ** 2)]
    ])

    print(stress_tensor.shape)

    vm_stress = gvl.get_von_Mises_stress(stress_tensor)

    glyph_radius = 0.25
    limits = [np.min(vm_stress), np.max(vm_stress)]
    colormap = plt.get_cmap('rainbow', 120)

    fig2 = plt.figure()
    ax = fig2.add_subplot(111, projection='3d')

    for i in range(x.size):
        for j in range(y.size):
            for k in range(z.size):
                center = [x[i], y[j], z[k]]
                data = stress_tensor[:, :, i, j, k]
                color = colormap(gvl.get_colormap_ratio_on_stress(vm_stress[i, j, k], limits))[:3]

                """
                glyph_type = {0: 'cuboid', 1: 'cylinder', 2: 'ellipsoid', 3: 'superquadric'}

                if glyph_type == 3 (superquadric) 
                there are glyph shape type
                0 - superquadrics, 
                1 - Kindlmann_glyph, 
                2 - Kindlmann_modified_glyph
                """

                x_g, y_g, z_g = gvl.get_glyph_data(center, data, limits, glyph_points=12, glyph_radius=glyph_radius,
                                                   glyph_type=3,
                                                   superquadrics_option=1)

                surf = ax.plot_surface(x_g, y_g, z_g, linewidth=0, antialiased=True, color=color)
                surf = ax.plot_wireframe(x_g, y_g, z_g, linewidth=1, antialiased=True, color=color)

    plt.show()

    pass


if __name__ == '__main__':
    main()
