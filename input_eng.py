
class Input:
    """
    Motor de extracción y procesamiento de datos de la GUI dividido por
    las secciones correspondientes a cada pestaña que la compone
    """

    class PropiedadesVectores:
        """
        Módulo de extracción y procesamiento de datos de la pestaña de
        propiedades de vectores
        """

        def __init_subclass__(cls) -> None:
            cls._datos: dict = {}


        @property
        def get_datos(cls) -> None:
            return cls._datos


        @get_datos.setter
        def set_datos(cls, datos: dict) -> None:
            cls._datos = datos


        def proc_input_vectores(cls, *args) -> None:
            """
            Procesamiento y guardado de datos importados como atributo de
            la subclase

            Los datos son guardados como un objeto de tipo :type:`dict`
            """

            claves: tuple = (
                "comp_x", "comp_y", "comp_z",
                "ang_x", "ang_y", "ang_z",
                "mag", "rad", "not", "id_op"
            )

            cls.set_datos = dict(zip(claves, args))

import matplotlib.pyplot as plt
from matplotlib import font_manager
from mpl_toolkits.mplot3d import Axes3D

font_dirs = ["D:\\OneDrive\\PrepaTec\\CalcPhysics\\fonts"]
font_files = font_manager.findSystemFonts(fontpaths = font_dirs)

for font_file in font_files:
    font_manager.fontManager.addfont(font_file)


""" plt.rcParams["figure.facecolor"] = "#303335"
plt.rcParams["figure.figsize"] = (8.55, 7)

plt.rcParams["axes.facecolor"] = "#181E20"
plt.rcParams["xtick.color"] = "#81D4FA"
plt.rcParams["ytick.color"] = "#81D4FA"

plt.rcParams["font.family"] = "Roboto Serif"
plt.rcParams["text.color"] = "#81D4FA"
plt.rcParams["font.size"] = 16

plt.rcParams["legend.facecolor"] = "#181E20"
plt.rcParams["legend.fancybox"] = True
plt.rcParams["legend.fontsize"] = 12

estilo_ejes: dict[str, str] = {
            'family': 'CMU Serif',
            'color': '#B0E6F0',
            'size': 20
        }

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d', proj_type = 'ortho')
ax.set_title("Vector 3D")
ax.set_xlabel("x", fontdict = estilo_ejes)
ax.set_ylabel("y", fontdict = estilo_ejes)
ax.set_zlabel("z", fontdict = estilo_ejes)
axs = plt.gca(); ax.axis("equal"); ax.margins(0.5, 0.5, 0.5)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.quiver(0, 0, 0, 1, 2, 1, color = ['#12C521'],
          label = "Magnitud", arrow_length_ratio = 0.1)
ax.set_xlim([-1, 4])
ax.set_ylim([-1, 4])
ax.set_zlim([-1, 4])

plt.grid(); plt.draw(); plt.legend(loc = "upper right")

plt.show() """