from .libs import *
from .constants import *
from .lambdas import *


class Example:
    def __init__(self, varmin, varmax):
        self.x = np.linspace(varmin, varmax, 1000)

    def pltshow(self, xlim, ylim):
        plt.xlim(*xlim)
        plt.ylim(*ylim)
        plt.grid()
        plt.legend()
        plt.show()

    def fill_between(self):
        #x = np.linspace(0.3, 4, 1000)
        y1 = np.log(self.x)
        y2 = y1**2

        plt.plot(self.x, y1, label='ln(x)', color='r')
        plt.plot(self.x, y2, label='ln(x^2)', color='g')
        plt.plot(1, 0, 'o', label='(1,0)', color='m')
        plt.plot(np.e, 1, 'o', label='(e,1)', color='c')

        where = np.logical_and((self.x > 1), (self.x < np.e))
        plt.fill_between(self.x, y1, y2,
                         where=where,
                         hatch='--',
                         linestyle=':',
                         alpha=.4,
                         color='k',
                         fc='y')
        self.pltshow((.5, 3), (-.5, 1.2))

    def simple_vecadd_polar(self):
        plt.polar([0, np.pi/2], [0, 2], '-')
        plt.polar([0, np.pi*1/3], [0, 1], '-')
        plt.polar([np.pi/2, np.pi*1/3], [2, 1], '--', alpha=.4)
        plt.show()

    def laplacePlot():
        t = np.linspace(0, 12, 1000)
        y = 3*(t-3)*step(t-3)-6*(t-6)*step(t-6)+3*(t-9)*step(t-9)
        plt.plot(t, y)
        plt.show()

    def exp_laplace(self):
        fig, (ax1, ax2) = plt.subplots(1, 2, sharey=False)

        exp = 4
        def f(x, a): return (x-a)**exp

        rangemin = -30000*np.pi
        rangemax = -(30000+20)*np.pi
        t = np.linspace(rangemin, rangemax, 10000)

        ax1.plot(t, f(t, 0))
        ax1.plot(t, f(t, 3))
        ax1.plot(t, f(t, 15))

        rangemin = -10*np.pi
        rangemax = 10*np.pi
        t = np.linspace(rangemin, rangemax, 10000)

        ax2.plot(t, f(t, 0))
        ax2.plot(t, f(t, 3))
        ax2.plot(t, f(t, 15))

        ax2.plot(3, 0, 'rx')
        ax2.plot(0, 0, 'rx')
        ax2.plot(15, 0, 'rx')

        plt.show()

    def sinosuids(self):
        fig, (ax1, ax2) = plt.subplots(1, 2, sharey=False)
        t = np.linspace(1, 5*np.pi, 1000)
        y = np.sin(5*t)*(t[::-1]*(np.sin(.5*t)+1))**1.5

        ax1.plot(t, y)
        ax1.plot(t, 0*t, 'r', alpha=.2)
        ax1.plot(t, (0*t)+y.max(), 'r--', alpha=.2)
        ax1.plot(t, (0*t)+y.min(), 'r--', alpha=.2)

        y2 = (t[::-1]*(np.sin(.5*t)+1))**1.5
        ax2.plot(t, y2)
        ax2.plot(t, 0*t, 'r', alpha=.4)
        ax2.plot(t, (0*t)+y2.max(), 'r--', alpha=.2)
        plt.show()

    def simplesquare(self):
        t = np.linspace(-2*np.pi, 2*np.pi, 1000)
        f = step(abs(t)-np.pi/2)-step(abs(t)-np.pi)
        plt.plot(t, f)
        plt.plot([0, 0], [f.min(), f.max()], alpha=.2)
        plt.show()

    def multipolar():
        fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
        t = np.linspace(0, pi, 1000)
        f = np.sin(t)
        axs[0, 0].plot(t, f)
        axs[1, 1].scatter(t, f)
        axs[0, 1].plot([0, pi/3, pi/2, 3/2*pi], (1, 1, 1, 1), 'r-')

        plt.show()

    def polarElkrets():
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(
            2, 2, subplot_kw=dict(projection="polar"))
        #ax1.plot(t, f)
        #ax1.scatter(t, f)
        ax1.plot([0, pi/3, pi/2, 3/2*pi], (1, 1, 1, 1), 'r--')
        ax1.set_title('current')
        ax2.plot([0, pi/3, pi/2, 3/2*pi], (1, 1, 1, 1), 'b--')
        ax2.set_title('voltage')

        current = polar2cart(230/5, 0)
        voltage = polar2cart(230, pi/2)
        power = current*voltage

        I = cart2polar(current)
        V = cart2polar(voltage)
        P = cart2polar(power)

        thetha, r = zip(I, V, P)
        ax3.plot((0, I[1]), (0, I[0]), 'b--', alpha=.5)
        ax3.plot((0, V[1]), (0, V[0]), 'r--', alpha=.5)
        #ax3.plot((0,P[1]),(0,P[0]),'g--', alpha=.2)
        print(I)
        plt.show()
