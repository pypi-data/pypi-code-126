import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FixedLocator, MultipleLocator
from mpl_toolkits.mplot3d import Axes3D


def plot_3D_scene(room_size, mic_position, T60, SNR, trajectory_points, name=""):
    """Plots the source trajectory and the microphones within the room."""
    fig = plt.figure()

    ax = Axes3D(fig)

    ax.set_xlim3d(0, room_size[0])
    ax.set_ylim3d(0, room_size[1])
    ax.set_zlim3d(0, room_size[2])

    ax.scatter(trajectory_points[:, 0], trajectory_points[:, 1], trajectory_points[:, 2])
    ax.scatter(mic_position[:, 0], mic_position[:, 1], mic_position[:, 2])
    ax.text(
        trajectory_points[0, 0],
        trajectory_points[0, 1],
        trajectory_points[0, 2],
        "Start",
    )

    ax.set_title("$T_{60}$" + " = {:.3f}s, SNR = {:.1f}dB".format(T60, SNR))
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.set_zlabel("z [m]")

    plt.savefig(name, dpi=None)


def plot_2D_scene(
    room_size,
    valid_region,
    mic_position,
    T60,
    SNR,
    trajectory,
    backup_trajectory,
    name="",
):
    """Plots the source trajectory and the microphones within the room."""
    width = room_size[0]
    depth = room_size[1]

    fig, ax = plt.subplots()
    ax.set_title(f"T60={T60:.1f}s, SNR={SNR:.1f}dB")
    ax.set_xlabel("Width (m)")
    ax.set_ylabel("Depth (m)")
    ax.set_xlim(0, width)
    ax.set_ylim(0, depth)

    # Change major ticks
    ax.xaxis.set_major_locator(FixedLocator([0, *np.linspace(valid_region[0][0], valid_region[1][0], 4), width]))
    ax.yaxis.set_major_locator(FixedLocator([0, *np.linspace(valid_region[0][1], valid_region[1][1], 4), depth]))

    # Change minor ticks
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))

    ax.grid(which="major", linestyle="--", alpha=0.8)
    ax.grid(which="minor", linestyle="-.", alpha=0.1)

    ax.plot(
        backup_trajectory[:, 0],
        backup_trajectory[:, 1],
        linewidth=10.0,
        alpha=0.2,
        color="#4477AA",
    )
    ax.quiver(
        trajectory[-1, 0],
        trajectory[-1, 1],
        trajectory[-1, 0] - trajectory[-2, 0],
        trajectory[-1, 1] - trajectory[-2, 1],
        scale_units="xy",
        headwidth=7,
        color="#4477AA",
    )
    ax.plot(
        trajectory[:, 0],
        trajectory[:, 1],
        c="#4477AA",
        linewidth=2,
    )
    ax.scatter(trajectory[:, 0], trajectory[:, 1], marker=".", color="#4477AA", alpha=0.6)  # type: ignore
    ax.scatter(trajectory[0, 0], trajectory[0, 1], marker="o", color="#4477AA", alpha=1)  # type: ignore
    ax.scatter(mic_position[:, 0], mic_position[:, 1])

    plt.savefig(name, dpi=None)
    plt.close(fig)
