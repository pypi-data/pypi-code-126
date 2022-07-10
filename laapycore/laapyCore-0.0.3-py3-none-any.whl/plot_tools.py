from .libs import *


def splane(TF, ax, poles=None, zeros=None, smin=-10, smax=10, heightlim=2):
    '''
    splane(tansferFunction,ax,poles=None,zeros=None,smin=-10,smax=10,heightlim=2) => ax
    '''
    o = np.linspace(smin, smax, 2000)
    w = o.copy()
    O, W = np.meshgrid(o, w)
    s = O+1j*W
    Y = TF(s)
    G = Y.copy()
    G = abs(G)
    G[G > heightlim] = heightlim
    while poles:
        pole = poles.pop()
        ax.plot(pole.real, pole.imag, 'rx', label=f'pole {pole}')
    while zeros:
        zero = zeros.pop()
        ax.plot(zero.real, zero.imag, 'ro', label=f'zero {zero}')

    ax.contour(O, W, G, 12)
    ax.set_xlabel(r'$\sigma$')
    ax.set_ylabel(r'$j\omega$')
    ax.grid()
    return ax


def splane_slice(TF, ax, smin=-10, smax=10, sigmas=None, heightlim=2):
    x = np.linspace(smin, smax, 1000)
    assert type(sigmas) in (list, tuple), 'sigmas must be list or tuple'
    for i in sigmas:
        s = x*1j+i
        ax.plot(x, abs(TF(s)), label=fr'$\sigma={i}$')
    ax.set_ylim(0, heightlim)
    ax.set_xlabel(r'$j \omega$')
    ax.set_ylabel('amplitude')
    ax.legend()
    return


def splane3d(TF, ax, smin=-10, smax=10, heightlim=2):
    o = np.linspace(smin, smax, 2000)
    w = o.copy()
    O, W = np.meshgrid(o, w)
    s = O+1j*W
    Y = TF(s)
    G = Y.copy()
    G = abs(G)
    G[G > heightlim] = heightlim

    surf = ax.plot_surface(O, W, G, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    ax.set_xlabel('real')
    ax.set_ylabel('imag')
    ax.set_zlabel('amplitude')
    ax.set_zlim(0, heightlim)
    return ax


def setBodeInfo(ax1, ax2):
    ax1.set_ylabel('Gain (dB)')
    ax2.set_ylabel('Phase Angle (deg)')
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_xscale('log')
    ticks = (0, -45, -90, -180)
    ax2.set_yticks(ticks)
    ax2.set_yticklabels([rf'${i}\degree$' for i in ticks])
    return ax1, ax2


def plotOnBode(TF, ax1, ax2, wlogmin=-10, wlogmax=10, label=None, fmt='', is_zero=False):
    w = np.logspace(wlogmin, wlogmax, 3000)
    tfresp = TF(1j*w)
    inv = -1 if is_zero else 1
    dB = np.log10(abs(tfresp))*20*inv
    phase = np.angle(tfresp)*180/np.pi*inv
    ax1.plot(w, dB, fmt, label=label)
    ax2.plot(w, phase, fmt)


def dxdyMark(ax, x1, x2, y1, y2, comment='', xytext=None, below=True):
    x = (x1, x1 if below else x2, x2)
    y = (y1, y2 if below else y1, y2)
    ax.plot(x, y, 'g--')
    xy = (x1, y2) if below else (x2, y1)
    if xytext:
        ax.annotate(comment, xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="->"))
