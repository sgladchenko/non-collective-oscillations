from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import ticker

from constants import *

from mesh import Mesh
import numpy as np
import weak
import vacuum
import akhmedov

weak_mesh = Mesh()
vacuum_mesh = Mesh()
akhmedov_mesh = Mesh()

length = 70 # km

for x in np.arange(0, length*1e3*1e2, 0.5e4):
	weak_mesh.add_on_mesh(x, abs(weak.rho_flavours(x)[0][1]))
	vacuum_mesh.add_on_mesh(x, abs(vacuum.rho_flavours(x)[0][1]))
	akhmedov_mesh.add_on_mesh(x, abs(akhmedov.rho_flavours(x)[0][1]))

fig = Figure()
FigureCanvas(fig)

axs1 = fig.add_subplot(2, 1, 1)
axs2 = fig.add_subplot(2, 1, 2)


l1, = axs1.plot(weak_mesh.x(1e-5), weak_mesh.y(1e3), '-', markersize=1, color='#000000')
axs1.set_title("Oscillations in vacuum and normal matter")
axs1.set_ylabel("rho(e, μ) x 1e-3")
axs1.grid(True)
axs1.get_yaxis().get_major_formatter().set_useOffset(1e-3)
axs1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))

axs1.legend([l1, ], ["Normal matter, V = {} eV".format(Ve/eV_2_erg),])

"""
l1, = axs1.plot(akhmedov_mesh.x(1e-5), akhmedov_mesh.y(), '-', markersize=1, color='#255F3E')
axs1.set_title("Oscillations in vacuum (corrected and not corrected)")
axs1.set_ylabel("rho(e, μ)")
axs1.grid(True)
axs1.get_yaxis().get_major_formatter().set_useOffset(1e-3)
axs1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))

axs1.legend([l1, ], ["Linear dispersion relation",])
"""

l2, = axs2.plot(weak_mesh.x(1e-5), vacuum_mesh.y(), '-', markersize=1, color='#29506D')
axs2.set_ylabel("rho(e, μ)")
axs2.set_xlabel("Length, km")
axs2.grid(True)
axs2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))

#axs2.legend([l2, ], ["Vacuum",])
axs2.legend([l2, ], ["Vacuum",])

fig.savefig("plots/plot_matter.png", fmt="png")
