"""
=====================================
Vector calculations:
- 2D and 3D vectors
- Components and magnitudes
- Addition, substraction, dot
    and cross product of vectors
- Rectangular and polar notations
- ¿¿¿ Derivatives and integration 
    (equations) of vectors ???
=====================================
"""

from input_eng import Input

from math import radians, degrees, cos, sin, asin, acos, atan, sqrt, pow
from matplotlib import use, font_manager
import matplotlib.pyplot as plt
import numpy as np

# Propiedades de la gráfica
plt.rcParams["figure.facecolor"] = "#30333521"
plt.rcParams["figure.figsize"] = (8.55, 7)

# Propiedades de los ejes de la gráfica
plt.rcParams["axes.facecolor"] = "#181E20"
plt.rcParams["xtick.color"] = "#81D4FA"
plt.rcParams["ytick.color"] = "#81D4FA"

# Propiedades del texto en la gráfica
plt.rcParams["text.color"] = "#81D4FA"
plt.rcParams["font.family"] = "Roboto Serif"
plt.rcParams["font.size"] = 16
plt.rcParams["mathtext.fontset"] = "cm"

# Propiedades de la leyenda en la gráfica
plt.rcParams["legend.facecolor"] = "#181E20"
plt.rcParams["legend.fancybox"] = True
plt.rcParams["legend.fontsize"] = 12

# Propiedades del texto en los ejes de la gráfica
estilo_ejes: dict[str, str] = {
    'family': 'CMU Serif',
    'color': '#B0E6F0',
    'size': 20
}

# Propiedades del texto de la representación matemática del vector
estilo_vector: dict[str, str] = {
    'color': '#72EAC6C8',
    'size': 14
}

# Propiedades del cuadro de la representación matemática del vector
estilo_cuadro_vector: dict[str, str] = {
    'facecolor': '#181E20',
    'edgecolor': '#FFFFFFBB',
    'boxstyle': 'round'
}

font_dirs = ["D:\\OneDrive\\PrepaTec\\CalcPhysics\\fonts"]
font_files = font_manager.findSystemFonts(fontpaths = font_dirs)

for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

use("svg")

class Vector:
    """
    Clase con subclases para el cálculo de propiedades y operaciones 
    vectoriales hasta en R3
    """

    class Propiedades:
        """
        Funciones para calcular y analizar propiedades de vectores hasta en R3
        """

        @staticmethod
        def magnitud(vector_rect: list[float]) -> float:
            """
            Cálculo de la magnitud del vector `v` a partir de sus componentes

            Regresa un número de tipo :type:`float` con el valor de la magnitud
            """

            vector_rect: dict[str, float] = dict(zip(("i", "j", "k"), vector_rect))

            if len(vector_rect) == 1:
                mag: float = vector_rect["i"]
            elif len(vector_rect) == 2:
                mag: float = sqrt(pow(vector_rect["i"], 2) + pow(vector_rect["j"], 2))
            else:
                mag: float = sqrt(pow(vector_rect["i"], 2) + pow(vector_rect["j"], 2) + pow(vector_rect["k"], 2))

            return mag


        @staticmethod
        def vector_unitario(vector_rect: list[float]) -> dict[str, float]:
            """
            Cálculo del vector unitario en la dirección del vector `v`

            Regresa un objeto de tipo :type:`dict` con los valores de 
            las componentes del vector unitario
            """

            mag: float = Vector.Propiedades.magnitud(vector_rect)
            vector_unit: list[float] = [comp / mag for comp in vector_rect]

            vector_unit: dict[str, float] = dict(zip(("i", "j", "k"), vector_unit))

            return vector_unit


        @staticmethod
        def componentes_2D(mag: float, angulo: float) -> dict[str, float]:
            """
            Cálculo de las componentes del vector `v` en forma rectangular

            Regresa un objeto de tipo :type:`dict` con los valores de 
            las componentes del vector en dos dimensiones
            """

            x_comp: float = mag * cos(radians(angulo))
            y_comp: float = mag * sin(radians(angulo))

            comptes: dict[str, float] = dict(zip(("i", "j"), (x_comp, y_comp)))

            return comptes


        @staticmethod
        def componentes_2D_rad(mag: float, angulo:float) -> dict[str, float]:
            """
            Cálculo de las componentes del vector `v` en forma rectangular
            
            Se usan radianes como unidad de ángulo

            Regresa un objeto de tipo :type:`dict` con los valores de 
            las componentes del vector en dos dimensiones
            """

            x_comp: float = mag * cos(angulo)
            y_comp: float = mag * sin(angulo)

            comptes: dict[str, float] = dict(zip(("i", "j"), (x_comp, y_comp)))

            return comptes


        @staticmethod
        def componentes_3D(mag: float, angulos: list[float]) -> dict[str, float]:
            """
            Cálculo de las componentes del vector `v` en forma rectangular

            Regresa un objeto de tipo :type:`dict` con los valores de 
            las componentes del vector en tres dimensiones
            """

            angulos: dict[str, float] = dict(zip(("x", "y", "z"), angulos))

            x_comp: float = mag * cos(radians(angulos["x"]))
            y_comp: float = mag * cos(radians(angulos["y"]))
            z_comp: float = mag * cos(radians(angulos["z"]))

            vector: dict[str, float] = dict(zip(("i", "j", "k"), (x_comp, y_comp, z_comp)))

            return vector


        @staticmethod
        def componentes_3D_rad(mag: float, angulos: list[float]) -> dict[str, float]:
            """
            Cálculo de las componentes del vector `v` en forma rectangular
            
            Se usan radianes como unidad de ángulo

            Regresa un objeto de tipo :type:`dict` con los valores de 
            las componentes del vector en tres dimensiones
            """

            angulos: dict[str, float] = dict(zip(("x", "y", "z"), angulos))

            x_comp: float = mag * cos(angulos["x"])
            y_comp: float = mag * cos(angulos["y"])
            z_comp: float = mag * cos(angulos["z"])

            vector: dict[str, float] = dict(zip(("i", "j", "k"), (x_comp, y_comp, z_comp)))

            return vector


        @staticmethod
        def cosenos_directores(vector_rect: list[float]) -> dict[str, float]:
            """
            Cálculo de los cosenos o ángulos directores del vector `v`

            Regresa un objeto de tipo :type:`dict` con los valores de
            los ángulos del vector en tres dimensiones
            """

            mag: float = Vector.Propiedades.magnitud(vector_rect)
            vector_rect: dict[str, float] = dict(zip(("i", "j", "k"), vector_rect))

            x_cos: float = degrees(acos(vector_rect["i"] / mag))
            y_cos: float = degrees(acos(vector_rect["j"] / mag))
            z_cos: float = degrees(acos(vector_rect["k"] / mag))

            cos_directores: dict[str, float] = dict(zip(("x", "y", "z"), (x_cos, y_cos, z_cos)))

            return cos_directores


        @staticmethod
        def cosenos_directores_rad(vector_rect: list) -> dict[str, float]:
            """
            Cálculo de los cosenos o ángulos directores del vector `v`

            Regresa un objeto de tipo :type:`dict` con los valores de
            los ángulos en radianes del vector en tres dimensiones
            """

            mag: float = Vector.Propiedades.magnitud(vector_rect)
            vector_rect: dict[str, float] = dict(zip(("i", "j", "k"), vector_rect))

            x_cos: float = acos(vector_rect["i"] / mag)
            y_cos: float = acos(vector_rect["j"] / mag)
            z_cos: float = acos(vector_rect["k"] / mag)

            cos_directores: dict[str, float] = dict(zip(("x", "y", "z"), (x_cos, y_cos, z_cos)))

            return cos_directores


        """ Deprecated """
        @staticmethod
        def cuadrant_components(mag, angle, cuad):
            if cuad == 'ii':
                return -mag * cos(radians(angle)), mag * sin(radians(angle))
            elif cuad in ['iii', '-']:
                return -mag * cos(radians(angle)), -mag * sin(radians(angle))
            elif cuad == 'iv':
                return mag * cos(radians(angle)), -mag * sin(radians(angle))

            return mag * cos(radians(angle)), mag * sin(radians(angle))

        """ Deprecated """
        @staticmethod
        def vector_components(vector):
            if vector[3] in ['II', 'ii']:
                return -vector[1] * cos(radians(vector[2])), vector[1] * sin(radians(vector[2]))
            elif vector[3] in ['III', 'iii', '-']:
                return -vector[1] * cos(radians(vector[2])), -vector[1] * sin(radians(vector[2]))
            elif vector[3] in ['IV', 'iv']:
                return vector[1] * cos(radians(vector[2])), -vector[1] * sin(radians(vector[2]))

            return vector[1] * cos(radians(vector[2])), vector[1] * sin(radians(vector[2]))

        """ Deprecated """
        @staticmethod
        def result_angle(rect_vector):
            reference_angle = degrees(atan(rect_vector[1] / rect_vector[0]))
            if rect_vector[0] > 0 and rect_vector[1] > 0:
                return reference_angle
            elif rect_vector[0] < 0 and (rect_vector[1] > 0 or rect_vector[1] < 0):
                total_angle = reference_angle + 180
            else:
                total_angle = reference_angle + 360

            return total_angle

        """ Deprecated """
        @staticmethod
        def rect_vector(component_list):
            if component_list[0] < 0:
                i_comp = f"- {abs(component_list[0]):.3f}î "
            else:
                i_comp = f"{component_list[0]:.3f}î "

            if component_list[1] < 0:
                j_comp = f"- {abs(component_list[1]):.3f}ĵ "
            else:
                j_comp = f"+ {component_list[1]:.3f}ĵ "

            if component_list[2] < 0:
                k_comp = f"- {abs(component_list[2]):.3f}k"
            else:
                k_comp = f"+ {component_list[2]:.3f}k"

            vector = f"{i_comp}{j_comp}{k_comp}"

            return vector


    class VectorOperations:
        """
        Funciones para realizar operaciones con vectores hasta en R3
        """

        @staticmethod
        def mult_by_scalar(factor, rect_vector):
            
            return factor * rect_vector

        @staticmethod
        def dot_prod(rect_vector_1, rect_vector_2):
            dot_prod = np.dot(rect_vector_1, rect_vector_2)

            return dot_prod

        @staticmethod
        def dot_prod_angle(rect_vector_1, rect_vector_2):
            dot_prod = Vector.VectorOperations.dot_prod(rect_vector_1, rect_vector_2)
            mag_1 = Vector.magnitud(rect_vector_1); mag_2 = Vector.magnitud(rect_vector_2)
            angle = degrees(acos(dot_prod / (mag_1 * mag_2)))

            return angle

        @staticmethod
        def cross_prod(rect_vector_1, rect_vector_2):
            cross_prod = np.cross(rect_vector_1, rect_vector_2)

            return tuple(map(float, cross_prod))

        @staticmethod
        def cross_prod_angle(rect_vector_1, rect_vector_2):
            cross_prod = Vector.VectorOperations.cross_prod(rect_vector_1, rect_vector_2)
            cross_prod_mag = Vector.magnitud(cross_prod)
            mag_1 = Vector.magnitud(rect_vector_1); mag_2 = Vector.magnitud(rect_vector_2)
            angle = degrees(asin(cross_prod_mag / (mag_1 * mag_2)))

            return angle


    class Visualizador:
        """
        Motor de interpretación y visualización de datos de la GUI
        en las pestañas de propiedades de vectores y operaciones con
        vectores.
        """

        def __init__(self) -> None:
            self._grafica = ""


        @property
        def get_grafica(self) -> None:
            return self._grafica


        class PropiedadesVectores:
            """
            Módulo de procesamiento de datos para la pestaña
            propiedades de vectores.

            Trabaja con la subclase :subclass:`Input.PropiedadesVectores`
            """

            def generador(Input: Input.PropiedadesVectores):
                """
                Generación de la figura con :library:`Matplotlib`
                """

                datos: dict[str] = Input.get_datos

                if datos["id_op"] == "comptes":

                    if datos["ang_z"] != "":

                        # Propiedades específicas de la gráfica
                        fig = plt.figure()
                        ax = fig.add_subplot(projection = '3d', proj_type = 'ortho')
                        ax.set_title("Componentes del vector")
                        ax.set_xlabel("x", fontdict = estilo_ejes)
                        ax.set_ylabel("y", fontdict = estilo_ejes)
                        ax.set_zlabel("z", fontdict = estilo_ejes)
                        ax.xaxis.pane.fill, ax.yaxis.pane.fill, ax.zaxis.pane.fill = False, False, False
                        axs = plt.gca(); ax.set_aspect("equalxy"); ax.margins(0.5, 0.5, 0.5)
                        ax.autoscale(enable = True, axis = "both", tight = True)

                        # Procesamiento de datos
                        ang_x = float(datos["ang_x"]); ang_y = float(datos["ang_y"]); ang_z = float(datos["ang_z"])
                        magnitud = float(datos["mag"]);
                        if datos["rad"] == True:
                            comp_vector: dict[str, float] = Vector.Propiedades.componentes_3D_rad(
                                magnitud, [ang_x, ang_y, ang_z]
                            )
                        else:
                            comp_vector: dict[str, float] = Vector.Propiedades.componentes_3D(
                                magnitud, [ang_x, ang_y, ang_z]
                            )
                        comp_x: float = comp_vector["i"]; comp_y: float = comp_vector["j"]; comp_z: float = comp_vector["k"]
                        plt.scatter(comp_x, comp_y, comp_z, c = '#FFFFFF00')
                        print(comp_x, comp_y, comp_z)

                        # Trazo del vector
                        ax.quiver(
                            0, 0, 0, comp_x, comp_y, comp_z,
                            color = ['#C8C823'], arrow_length_ratio = 0.1,
                            label = rf"$ |v| = {magnitud:.4f} $"
                        )
                        # Trazo de la componente en x
                        ax.quiver(
                            0, 0, 0, comp_x, 0, 0,
                            arrow_length_ratio = 0.1,
                            color = ['#D71A40'],
                            label = rf"$ {comp_x:.4f} i $"
                        )
                        # Trazo de la componente en y
                        ax.quiver(
                            0, 0, 0, 0, comp_y, 0,
                            arrow_length_ratio = 0.1,
                            color = ['#1BC4E6'],
                            label = rf"$ {comp_y:.4f} j $"
                        )
                        # Trazo de la componente en z
                        ax.quiver(
                            0, 0, 0, 0, 0, comp_z,
                            arrow_length_ratio = 0.1,
                            color = ['#29E782'],
                            label = rf"$ {comp_z:.4f} k $"
                        )
                        # Etiquetado de la magnitud del vector
                        ax.text(
                            comp_x / 2, comp_y / 2, comp_z / 2,
                            rf"$ |v| = {magnitud:.4f} $"
                        )
                        # Etiquetado de la componente en la dirección i (eje x)
                        ax.text(
                            comp_x * 1.03, 0, 0,
                            rf"$ {comp_x:.4f} i $"
                        )
                        # Etiquetado de la componente en la dirección j (eje y)
                        ax.text(
                            0, comp_y * 1.03, 0,
                            rf"$ {comp_y:.4f} j $"
                        )
                        # Etiquetado de la componente en la dirección jk(eje z)
                        ax.text(
                            0, 0, comp_z * 1.03,
                            rf"$ {comp_z:.4f} k $"
                        )

                        # Representación matemática del vector
                        if datos["not"] == True:
                            ax.text(
                                5, 5, 0.5,
                                r"$ \vec{v} $" + rf"$ = \langle {comp_x:.4f}, {comp_y:.4f}, {comp_z:.4f} \rangle $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )
                        else:
                            ax.text(
                                5, 5, 0.5,
                                r"$ \vec{v} $" + rf"$ = ({comp_x:.4f}) i + ({comp_y:.4f}) j + ({comp_z:.4f}) k $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )

                        # Visualización de los elementos en la gráfica
                        plt.grid(); plt.draw(); plt.legend(ncol = 4, bbox_to_anchor = (0.5, -0.02), loc = "best")

                        return fig

                    else:

                        # Propiedades específicas de la gráfica
                        fig, ax = plt.subplots()
                        ax.set_title("Componentes del vector")
                        ax.set_xlabel("x", fontdict = estilo_ejes)
                        ax.set_ylabel("y", fontdict = estilo_ejes)
                        axs = plt.gca(); ax.axis("equal"); ax.margins(0.5, 0.5)

                        # Procesamiento de datos
                        magnitud = float(datos["mag"]); ang_x = float(datos["ang_x"])
                        if datos["rad"] == True:
                            comp_vector: dict[str, float] = Vector.Propiedades.componentes_2D_rad(
                                magnitud, ang_x
                            )
                        else:
                            comp_vector: dict[str, float] = Vector.Propiedades.componentes_2D(
                                magnitud, ang_x
                            )
                        plt.scatter(comp_vector["i"], comp_vector["j"], c = '#FFFFFF00')

                        # Trazo del vector
                        ax.quiver(
                            0, 0, comp_vector['i'], comp_vector["j"], angles = 'xy',
                            scale_units = 'xy', color = ['#29E782'], scale = 1,
                            label = "Magnitud"
                        )
                        # Trazo de la componente en x
                        ax.quiver(
                            0, 0, comp_vector['i'], 0, angles = 'xy', scale = 1,
                            scale_units = 'xy', color = ['#D71A40'],
                            label = "Comp. en x"
                        )
                        # Trazo de la componente en y
                        ax.quiver(
                            0, 0, 0, comp_vector["j"], angles = 'xy', scale = 1,
                            scale_units = 'xy', color = ['#1BC4E6'],
                            label = "Comp. en y"
                        )
                        # Etiquetado de la magnitud del vector
                        ax.text(
                            comp_vector['i'] / 2, comp_vector["j"] / 2,
                            rf"$ |v| = {magnitud:.4f} $"
                        )
                        # Etiquetado de la componente en la dirección i (eje x)
                        ax.text(
                            comp_vector["i"] * 1.03, 0,
                            rf"$ {comp_vector['i']:.4f} i $",
                        )
                        # Etiquetado de la componente en la dirección j (eje y)
                        ax.text(
                            0, comp_vector["j"] * 1.03,
                            rf"$ {comp_vector['j']:.4f} j $",
                        )

                        # Representación matemática del vector
                        if datos["not"] == True:
                            ax.text(
                                0.02, 0.93,
                                r"$ \vec{v} $" + rf"$ = \langle {comp_vector['i']:.4f}, {comp_vector['j']:.4f} \rangle $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )
                        else:
                            ax.text(
                                0.02, 0.94,
                                r"$ \vec{v} $" + rf"$ = ({comp_vector['i']:.4f}) i + ({comp_vector['j']:.4f}) j $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )

                        # Visualización de los elementos en la gráfica
                        plt.grid(); plt.draw(); plt.legend(loc = "upper right")

                        return fig

                elif datos["id_op"] == "mag":

                    if datos["comp_z"] != "":

                        # Propiedades específicas de la gráfica
                        fig = plt.figure()
                        ax = fig.add_subplot(projection = '3d', proj_type = 'ortho')
                        ax.set_title("Magnitud del vector")
                        ax.set_xlabel("x", fontdict = estilo_ejes)
                        ax.set_ylabel("y", fontdict = estilo_ejes)
                        ax.set_zlabel("z", fontdict = estilo_ejes)
                        ax.xaxis.pane.fill, ax.yaxis.pane.fill, ax.zaxis.pane.fill = False, False, False
                        axs = plt.gca(); ax.set_aspect("equalxy"); ax.margins(0.5, 0.5, 0.5)
                        ax.autoscale(enable = True, axis = 'both')

                        # Procesamiento de datos
                        comp_x = float(datos["comp_x"]); comp_y = float(datos["comp_y"]); comp_z = float(datos["comp_z"])
                        magnitud: float = Vector.Propiedades.magnitud([comp_x, comp_y, comp_z])
                        ax.scatter(comp_x, comp_y, comp_z, c = '#FFFFFF00')

                        # Trazo del vector
                        ax.quiver(
                            0, 0, 0, comp_x, comp_y, comp_z,
                            color = ['#C8C823'], arrow_length_ratio = 0.1,
                            label = rf"$ |v| = {magnitud:.4f} $"
                        )
                        # Trazo de la componente en x
                        ax.quiver(
                            0, 0, 0, comp_x, 0, 0,
                            arrow_length_ratio = 0.1,
                            color = ['#D71A40'],
                            label = rf"$ {comp_x:.4f} i $"
                        )
                        # Trazo de la componente en y
                        ax.quiver(
                            0, 0, 0, 0, comp_y, 0,
                            arrow_length_ratio = 0.1,
                            color = ['#1BC4E6'],
                            label = rf"$ {comp_y:.4f} j $"
                        )
                        # Trazo de la componente en z
                        ax.quiver(
                            0, 0, 0, 0, 0, comp_z,
                            arrow_length_ratio = 0.1,
                            color = ['#29E782'],
                            label = rf"$ {comp_z:.4f} k $"
                        )
                        # Etiquetado de la magnitud del vector
                        ax.text(
                            comp_x / 2, comp_y / 2, comp_z / 2,
                            rf"$ |v| = {magnitud:.4f} $"
                        )
                        # Etiquetado de la componente en la dirección i (eje x)
                        ax.text(
                            comp_x * 1.03, 0, 0,
                            rf"$ {comp_x:.4f} i $"
                        )
                        # Etiquetado de la componente en la dirección j (eje y)
                        ax.text(
                            0, comp_y * 1.03, 0,
                            rf"$ {comp_y:.4f} j $"
                        )
                        # Etiquetado de la componente en la dirección jk(eje z)
                        ax.text(
                            0, 0, comp_z * 1.03,
                            rf"$ {comp_z:.4f} k $"
                        )

                        # Representación matemática del vector
                        if datos["not"] == True:
                            ax.text(
                                5, 5, 0.5,
                                r"$ \vec{v} $" + rf"$ = \langle {comp_x:.4f}, {comp_y:.4f}, {comp_z:.4f} \rangle $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )
                        else:
                            ax.text(
                                5, 5, 0.5,
                                r"$ \vec{v} $" + rf"$ = ({comp_x:.4f}) i + ({comp_y:.4f}) j + ({comp_z:.4f}) k $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )

                        # Visualización de los elementos en la gráfica
                        plt.grid(); plt.draw(); plt.legend(ncol = 4, bbox_to_anchor = (0.5, -0.02), loc = "upper center")

                        return fig

                    else:

                        # Propiedades específicas de la gráfica
                        fig, ax = plt.subplots()
                        ax.set_title("Magnitud del vector")
                        ax.set_xlabel("x", fontdict = estilo_ejes)
                        ax.set_ylabel("y", fontdict = estilo_ejes)
                        axs = plt.gca(); ax.axis("equal"); ax.margins(0.5, 0.5)

                        # Procesamiento de datos
                        comp_x = float(datos["comp_x"]); comp_y = float(datos["comp_y"])
                        magnitud: float = Vector.Propiedades.magnitud([comp_x, comp_y])
                        plt.scatter(comp_x, comp_y, c = '#FFFFFF00')

                        # Trazo del vector
                        ax.quiver(
                            0, 0, comp_x, comp_y, angles = 'xy', scale = 1,
                            scale_units = 'xy', color = ['#29E782'],
                            label = "Magnitud"
                        )
                        # Trazo de la componente en x
                        ax.quiver(
                            0, 0, comp_x, 0, angles = 'xy', scale = 1,
                            scale_units = 'xy', color = ['#D71A40'],
                            label = "Comp. en x"
                        )
                        # Trazo de la componente en y
                        ax.quiver(
                            0, 0, 0, comp_y, angles = 'xy', scale = 1,
                            scale_units = 'xy', color = ['#1BC4E6'],
                            label = "Comp. en y"
                        )
                        # Etiquetado de la magnitud del vector
                        ax.text(
                            comp_x / 2, comp_y / 2,
                            rf"$ |v| = {magnitud:.4f} $"
                        )
                        # Etiquetado de la componente en la dirección i (eje x)
                        ax.text(
                            comp_x * 1.03, 0,
                            rf"$ {comp_x:.4f} i $"
                        )
                        # Etiquetado de la componente en la dirección j (eje y)
                        ax.text(
                            0, comp_y * 1.03,
                            rf"$ {comp_y:.4f} j $"
                        )

                        # Representación matemática del vector
                        if datos["not"] == True:
                            ax.text(
                                0.02, 0.92, r"$ \vec{v} $" + rf"$ = \langle {comp_x:.4f}, {comp_y:.4f} \rangle $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )
                        else:
                            ax.text(
                                0.02, 0.93, r"$ \vec{v} $" + rf"$ = ({comp_x:.4f}) i + ({comp_y:.4f}) j $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )

                        # Visualización de los elementos en la gráfica
                        plt.grid(); plt.draw(); plt.legend(loc = "upper right")

                        return fig

                elif datos["id_op"] == "unit":

                    if datos["comp_z"] != "":

                        # Propiedades específicas de la gráfica
                        fig = plt.figure()
                        ax = fig.add_subplot(projection = '3d', proj_type = 'ortho')
                        ax.set_title("Vector unitario")
                        ax.set_xlabel("x", fontdict = estilo_ejes)
                        ax.set_ylabel("y", fontdict = estilo_ejes)
                        ax.set_zlabel("z", fontdict = estilo_ejes)
                        ax.xaxis.pane.fill, ax.yaxis.pane.fill, ax.zaxis.pane.fill = False, False, False
                        axs = plt.gca(); ax.set_aspect("equalxy"); ax.margins(0.5, 0.5, 0.5)
                        ax.autoscale(enable = True, axis = 'both')

                        # Procesamiento de datos
                        comp_x = float(datos["comp_x"]); comp_y = float(datos["comp_y"]); comp_z = float(datos["comp_z"])
                        vctr_unit: dict[str, float] = Vector.Propiedades.vector_unitario([comp_x, comp_y, comp_z])
                        comp_x_unit: float = vctr_unit["i"]; comp_y_unit: float = vctr_unit["j"]; comp_z_unit: float = vctr_unit["k"]
                        magnitud_unit: float = Vector.Propiedades.magnitud([comp_x_unit, comp_y_unit, comp_z_unit])
                        ax.scatter(comp_x_unit, comp_y_unit, comp_z_unit, c = '#FFFFFF00')

                        # Trazo del vector
                        ax.quiver(
                            0, 0, 0, comp_x_unit, comp_y_unit, comp_z_unit,
                            color = ['#C89423'], arrow_length_ratio = 0.1,
                            label = rf"$ |v| = {magnitud_unit:.4f} $"
                        )
                        # Trazo de la componente en x
                        ax.quiver(
                            0, 0, 0, comp_x_unit, 0, 0,
                            arrow_length_ratio = 0.1,
                            color = ['#D71ABB'],
                            label = rf"$ {comp_x_unit:.4f} i $"
                        )
                        # Trazo de la componente en y
                        ax.quiver(
                            0, 0, 0, 0, comp_y_unit, 0,
                            arrow_length_ratio = 0.1,
                            color = ['#1B91E6'],
                            label = rf"$ {comp_y_unit:.4f} j $"
                        )
                        # Trazo de la componente en z
                        ax.quiver(
                            0, 0, 0, 0, 0, comp_z_unit,
                            arrow_length_ratio = 0.1,
                            color = ['#29E73C'],
                            label = rf"$ {comp_z_unit:.4f} k $"
                        )
                        # Etiquetado de la magnitud del vector
                        ax.text(
                            comp_x_unit / 2, comp_y_unit / 2, comp_z_unit / 2,
                            rf"$ |v| = {magnitud_unit:.4f} $"
                        )
                        # Etiquetado de la componente en la dirección i (eje x)
                        ax.text(
                            comp_x_unit * 1.03, 0, 0,
                            rf"$ {comp_x_unit:.4f} i $"
                        )
                        # Etiquetado de la componente en la dirección j (eje y)
                        ax.text(
                            0, comp_y_unit * 1.03, 0,
                            rf"$ {comp_y_unit:.4f} j $"
                        )
                        # Etiquetado de la componente en la dirección jk(eje z)
                        ax.text(
                            0, 0, comp_z_unit * 1.03,
                            rf"$ {comp_z_unit:.4f} k $"
                        )

                        # Representación matemática del vector
                        if datos["not"] == True:
                            ax.text(
                                5, 5, 0.5,
                                r"$ \vec{v} $" + rf"$ = \langle {comp_x_unit:.4f}, {comp_y_unit:.4f}, {comp_z_unit:.4f} \rangle $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )
                        else:
                            ax.text(
                                5, 5, 0.5,
                                r"$ \vec{v} $" + rf"$ = ({comp_x_unit:.4f}) i + ({comp_y_unit:.4f}) j + ({comp_z_unit:.4f}) k $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )

                        # Visualización de los elementos en la gráfica
                        plt.grid(); plt.draw(); plt.legend(ncol = 4, bbox_to_anchor = (0.5, -0.02), loc = "upper center")

                        return fig

                    else:

                        # Propiedades específicas de la gráfica
                        fig, ax = plt.subplots()
                        ax.set_title("Vector unitario")
                        ax.set_xlabel("x", fontdict = estilo_ejes)
                        ax.set_ylabel("y", fontdict = estilo_ejes)
                        axs = plt.gca(); ax.axis("equal"); ax.margins(0.5, 0.5)

                        # Procesamiento de datos
                        comp_x = float(datos["comp_x"]); comp_y = float(datos["comp_y"])
                        vctr_unit: dict[str, float] = Vector.Propiedades.vector_unitario([comp_x, comp_y])
                        comp_x_unit: float = vctr_unit['i']; comp_y_unit: float = vctr_unit['j'];
                        magnitud_unit: float = Vector.Propiedades.magnitud([comp_x_unit, comp_y_unit])
                        plt.scatter(comp_x_unit, comp_y_unit, c = '#FFFFFF00')

                        # Trazo del vector unitario
                        ax.quiver(
                            0, 0, comp_x_unit, comp_y_unit, angles = 'xy', scale = 1,
                            scale_units = 'xy', color = ['#12C521'],
                            label = "Mag. unit"
                        )
                        # Trazo de la componente unitaria en x
                        ax.quiver(
                            0, 0, comp_x_unit, 0, angles = 'xy', scale = 1,
                            scale_units = 'xy', color = ['#D41AD7'],
                            label = "Unit. en x"
                        )
                        # Trazo de la componente unitaria en y
                        ax.quiver(
                            0, 0, 0, comp_y_unit, angles = 'xy', scale = 1,
                            scale_units = 'xy', color = ['#1B45DC'],
                            label = "Unit. en y"
                        )
                        # Etiquetado de la magnitud del vector unitario
                        ax.text(
                            comp_x_unit / 2, comp_y_unit / 2,
                            rf"$ |v| = {magnitud_unit:.4f} $"
                        )
                        # Etiquetado de la componente unitaria en la dirección i (eje x)
                        ax.text(
                            comp_x_unit * 1.03, 0,
                            rf"$ {comp_x_unit:.4f} i $",
                        )
                        # Etiquetado de la componente unitaria en la dirección j (eje y)
                        ax.text(
                            0, comp_y_unit * 1.03,
                            rf"$ {comp_y_unit:.4f} j $",
                        )

                        # Representación matemática del vector
                        if datos["not"] == True:
                            ax.text(
                                0.02, 0.92, r"$ \hat{v} $" + rf"$ = \langle {comp_x_unit:.4f}, {comp_y_unit:.4f} \rangle $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )
                        else:
                            ax.text(
                                0.02, 0.93, r"$ \hat{v} $" + rf" $ = ({comp_x_unit:.4f}) i + ({comp_y_unit:.4f}) j $",
                                fontdict = estilo_vector,
                                bbox = estilo_cuadro_vector,
                                transform = axs.transAxes
                            )

                        # Visualización de los elementos en la gráfica
                        plt.grid(); plt.draw(); plt.legend(loc = "upper right")

                        return fig

                elif datos["id_op"] == "cos":

                    # Propiedades específicas de la gráfica
                    fig = plt.figure()
                    ax = fig.add_subplot(projection = '3d', proj_type = 'ortho')
                    ax.set_title("Cosenos directores del vector")
                    ax.set_xlabel("x", fontdict = estilo_ejes)
                    ax.set_ylabel("y", fontdict = estilo_ejes)
                    ax.set_zlabel("z", fontdict = estilo_ejes)
                    ax.xaxis.pane.fill, ax.yaxis.pane.fill, ax.zaxis.pane.fill = False, False, False
                    axs = plt.gca(); ax.set_aspect("equalxy"); ax.margins(0.5, 0.5, 0.5)
                    ax.autoscale(enable = True, axis = 'both')

                    # Procesamiento de datos
                    comp_x = float(datos["comp_x"]); comp_y = float(datos["comp_y"]); comp_z = float(datos["comp_z"])
                    magnitud: float = Vector.Propiedades.magnitud([comp_x, comp_y, comp_z])
                    cos_directores: dict[str, float] = Vector.Propiedades.cosenos_directores([comp_x, comp_y, comp_z])
                    cos_x: float = cos_directores["x"]; cos_y: float = cos_directores["y"]; cos_z: float = cos_directores["z"]
                    ax.scatter(comp_x, comp_y, comp_z, c = '#FFFFFF00')

                    # Trazo del vector
                    ax.quiver(
                        0, 0, 0, comp_x, comp_y, comp_z,
                        color = ['#C8C823'], arrow_length_ratio = 0.1,
                        label = rf"$ |v| = {magnitud:.4f} $"
                    )
                    # Trazo de la componente en x
                    ax.quiver(
                        0, 0, 0, comp_x, 0, 0,
                        arrow_length_ratio = 0.1,
                        color = ['#D71A40'],
                        label = rf"$ \alpha = {cos_x:.4f} $" + r"$ ^{\circ} $"
                    )
                    # Trazo de la componente en y
                    ax.quiver(
                        0, 0, 0, 0, comp_y, 0,
                        arrow_length_ratio = 0.1,
                        color = ['#1BC4E6'],
                        label = rf"$ \beta = {cos_y:.4f} $" + r"$ ^{\circ} $"
                    )
                    # Trazo de la componente en z
                    ax.quiver(
                        0, 0, 0, 0, 0, comp_z,
                        arrow_length_ratio = 0.1,
                        color = ['#29E782'],
                        label = rf"$ \gamma = {cos_z:.4f} $" + r"$ ^{\circ} $"
                    )
                    # Etiquetado de la magnitud del vector
                    ax.text(
                        comp_x / 2, comp_y / 2, comp_z / 2,
                        rf"$ |v| = {magnitud:.4f} $"
                    )
                    # Etiquetado del ángulo con respecto al eje x
                    ax.text(
                        comp_x * 1.03, 0, 0,
                        rf"$ {cos_x:.4f} $"
                    )
                    # Etiquetado del ángulo con respecto al eje y
                    ax.text(
                        0, comp_y * 1.03, 0,
                        rf"$ {cos_y:.4f} $"
                    )
                    # Etiquetado del ángulo con respecto al eje z
                    ax.text(
                        0, 0, comp_z * 1.03,
                        rf"$ {cos_z:.4f} $"
                    )

                    # Representación matemática del vector
                    if datos["not"] == True:
                        ax.text(
                            5, 5, 0.5,
                            r"$ \vec{v} $" + rf"$ = \langle {comp_x:.4f}, {comp_y:.4f}, {comp_z:.4f} \rangle $",
                            fontdict = estilo_vector,
                            bbox = estilo_cuadro_vector,
                            transform = axs.transAxes
                        )
                    else:
                        ax.text(
                            5, 5, 0.5,
                            r"$ \vec{v} $" + rf"$ = ({comp_x:.4f}) i + ({comp_y:.4f}) j + ({comp_z:.4f}) k $",
                            fontdict = estilo_vector,
                            bbox = estilo_cuadro_vector,
                            transform = axs.transAxes
                        )

                    # Visualización de los elementos en la gráfica
                    plt.grid(); plt.draw(); plt.legend(ncol = 4, bbox_to_anchor = (0.5, -0.02), loc = "upper center")

                    return fig
