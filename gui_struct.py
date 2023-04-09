
from input_eng import Input
from vectors import Vector

from flet.matplotlib_chart import MatplotlibChart
import flet as ft


class GUI():
    """
    Propiedades de la estructura y creación de la GUI
    """

    def build_secciones() -> ft.Tabs:
        """
        Instancias de las clases correspondientes a cada pestaña en la GUI y
        construcción de la estructura de la GUI.

        Cada pestaña es una instancia de la clase :class:`ft.Tab`

        Regresa un objeto de la clase :class:`ft.Tabs`
        """
        tab1_vectores: ft.Tab = GUI.Vectores.build()
        tab2_op_vectores: ft.Tab = GUI.OperacionesVectores.build()
        tab3_conversiones: ft.Tab = GUI.Conversiones.build()

        secciones = ft.Tabs(
            animation_duration = 300,
            tabs = [
                tab1_vectores, tab2_op_vectores, tab3_conversiones
            ],
            expand = True
        )

        return secciones


    class Vectores():
        """
        Contiene el constructor de la pestaña correspondiente a propiedades de vectores
        """

        def build() -> ft.Tab:
            """
            Construye la pestaña correspondiente a propiedades de vectores

            Contiene los elementos que componen a la pestaña

            Regresa un objeto de la clase :class:`ft.Tab`
            """

            datos: Input.PropiedadesVectores = Input.PropiedadesVectores()

            grafico: Vector.Visualizador = Vector.Visualizador()

            def calcula_comptes(self) -> None:
                """
                Recupera los datos de cada entrada en la pestaña y los exporta
                al objeto de la subclase :subclass:`Input.PropiedadesVectores`.

                Se realizan las operaciones para el cálculo de componentes
                """

                datos.proc_input_vectores(
                    txt_comp_x.value, txt_comp_y.value, txt_comp_z.value,
                    txt_ang_x.value, txt_ang_y.value, txt_ang_z.value,
                    txt_magnitud.value, switch_angulo.value, switch_notacion.value,
                    "comptes"
                )

                grafica_vectores = grafico.PropiedadesVectores.generador(datos)

                cont_grafica.content = MatplotlibChart(grafica_vectores)

                self.page.update()

            def calcula_mag(self) -> None:
                """
                Recupera los datos de cada entrada en la pestaña y los exporta
                al objeto de la subclase :subclass:`Input.PropiedadesVectores`.

                Se realizan las operaciones para el cálculo de la magnitud
                """

                datos.proc_input_vectores(
                    txt_comp_x.value, txt_comp_y.value, txt_comp_z.value,
                    txt_ang_x.value, txt_ang_y.value, txt_ang_z.value,
                    txt_magnitud.value, switch_angulo.value, switch_notacion.value,
                    "mag"
                )

                grafica_vectores = grafico.PropiedadesVectores.generador(datos)

                cont_grafica.content = MatplotlibChart(grafica_vectores)

                self.page.update()

            def calcula_unitario(self) -> None:
                """
                Recupera los datos de cada entrada en la pestaña y los exporta
                al objeto de la subclase :subclass:`Input.PropiedadesVectores`.

                Se realizan las operaciones para el cálculo del vector unitario
                """

                datos.proc_input_vectores(
                    txt_comp_x.value, txt_comp_y.value, txt_comp_z.value,
                    txt_ang_x.value, txt_ang_y.value, txt_ang_z.value,
                    txt_magnitud.value, switch_angulo.value, switch_notacion.value,
                    "unit"
                )

                grafica_vectores = grafico.PropiedadesVectores.generador(datos)

                cont_grafica.content = MatplotlibChart(grafica_vectores)

                self.page.update()

            def calcula_cosenos(self) -> None:
                """
                Recupera los datos de cada entrada en la pestaña y los exporta
                al objeto de la subclase :subclass:`Input.PropiedadesVectores`.

                Se realizan las operaciones para el cálculo de los cosenos directores
                """

                datos.proc_input_vectores(
                    txt_comp_x.value, txt_comp_y.value, txt_comp_z.value,
                    txt_ang_x.value, txt_ang_y.value, txt_ang_z.value,
                    txt_magnitud.value, switch_angulo.value, switch_notacion.value,
                    "cos"
                )

                grafica_vectores = grafico.PropiedadesVectores.generador(datos)

                cont_grafica.content = MatplotlibChart(grafica_vectores)

                self.page.update()

            medidas: dict = {
                "columna1": {
                    "alto": 750,
                    "ancho": 550
                },
                "columna2": {
                    "alto": 750,
                    "ancho": 905
                },
                "titulo": {
                    "alto": 90,
                    "ancho": 510,
                },
                "subtitulo": {
                    "alto": 40,
                    "ancho": 510
                },
                "filas": {
                    "ancho": 510
                },
                "divisiones": {
                    "ancho": 510
                },
                "cuadros_txt": {
                    "alto": 80,
                    "ancho": 250,
                    "ancho_mag": 510,
                },
                "botones": {
                    "alto": 45,
                    "ancho": 245
                },
                "switch": {
                    "alto": 43,
                    "ancho": 127,
                    "alto_cnt": 45,
                    "ancho_cnt": 155,
                    "ancho_opc": 170,
                }
            }

            titulo_panel_prcp: ft.Text = ft.Text(
                            "Propiedades de vectores",
                            size = 36,
                            font_family = "Bahnschrift",
                            color = ft.colors.LIGHT_BLUE_300,
                            weight = ft.FontWeight.BOLD,
                            text_align = ft.TextAlign.CENTER,
                        )

            subtitulo_op: ft.Text = ft.Text(
                                "Operaciones",
                                size = 24,
                                font_family = "Tahoma",
                                color = ft.colors.LIGHT_BLUE_200,
                                weight = ft.FontWeight.BOLD,
                                text_align = ft.TextAlign.CENTER
                            )

            txt_magnitud: ft.TextField = ft.TextField(
                                label = "Magnitud",
                                label_style = ft.TextStyle(color = "#90A5B6"),
                                text_style = ft.TextStyle(font_family = "Verdana"),
                                prefix_style = ft.TextStyle(font_family = "CMU Serif",
                                                            size = 20),
                                prefix_text = "|v| = ",
                                border_radius = ft.border_radius.all(10),
                                filled = True,
                                bgcolor = "#111317",
                                border_color = "#111317"
                            )

            txt_comp_x: ft.TextField = ft.TextField(
                                label = "Componente en x",
                                label_style = ft.TextStyle(color = "#90A5B6"),
                                text_style = ft.TextStyle(font_family = "Verdana"),
                                prefix_style = ft.TextStyle(font_family = "CMU Serif",
                                                            size = 20),
                                prefix_text = "x = ",
                                border_radius = ft.border_radius.all(10),
                                filled = True,
                                bgcolor = "#111317",
                                border_color = "#111317"
                            )

            txt_comp_y: ft.TextField = ft.TextField(
                                label = "Componente en y",
                                label_style = ft.TextStyle(color = "#90A5B6"),
                                text_style = ft.TextStyle(font_family = "Verdana"),
                                prefix_style = ft.TextStyle(font_family = "CMU Serif",
                                                            size = 20),
                                prefix_text = "y = ",
                                border_radius = ft.border_radius.all(10),
                                filled = True,
                                bgcolor = "#111317",
                                border_color = "#111317"
                            )

            txt_comp_z: ft.TextField = ft.TextField(
                                label = "Componente en z",
                                label_style = ft.TextStyle(color = "#90A5B6"),
                                text_style = ft.TextStyle(font_family = "Verdana"),
                                prefix_style = ft.TextStyle(font_family = "CMU Serif",
                                                            size = 20),
                                prefix_text = "z = ",
                                border_radius = ft.border_radius.all(10),
                                filled = True,
                                bgcolor = "#111317",
                                border_color = "#111317"
                            )

            txt_ang_x: ft.TextField = ft.TextField(
                                label = "Ángulo en x",
                                label_style = ft.TextStyle(color = "#90A5B6"),
                                text_style = ft.TextStyle(font_family = "Verdana"),
                                prefix_style = ft.TextStyle(font_family = "CMU Serif",
                                                            size = 20),
                                suffix_style = ft.TextStyle(font_family = "Verdana",
                                                            size = 16),
                                prefix_text = "α = ",
                                suffix_text = "°",
                                border_radius = ft.border_radius.all(10),
                                filled = True,
                                bgcolor = "#111317",
                                border_color = "#111317"
                            )

            txt_ang_y: ft.TextField = ft.TextField(
                                label = "Ángulo en y",
                                label_style = ft.TextStyle(color = "#90A5B6"),
                                text_style = ft.TextStyle(font_family = "Verdana"),
                                prefix_style = ft.TextStyle(font_family = "CMU Serif",
                                                            size = 20),
                                suffix_style = ft.TextStyle(font_family = "Verdana",
                                                            size = 16),
                                prefix_text = "β = ",
                                suffix_text = "°",
                                border_radius = ft.border_radius.all(10),
                                filled = True,
                                bgcolor = "#111317",
                                border_color = "#111317"
                            )

            txt_ang_z: ft.TextField = ft.TextField(
                                label = "Ángulo en z",
                                label_style = ft.TextStyle(color = "#90A5B6"),
                                text_style = ft.TextStyle(font_family = "Verdana"),
                                prefix_style = ft.TextStyle(font_family = "CMU Serif",
                                                            size = 20),
                                suffix_style = ft.TextStyle(font_family = "Verdana",
                                                            size = 16),
                                prefix_text = "γ = ",
                                suffix_text = "°",
                                border_radius = ft.border_radius.all(10),
                                filled = True,
                                bgcolor = "#111317",
                                border_color = "#111317"
                            )

            def cambio_angulo(self) -> None:
                txt_ang_x.suffix_text = (
                    "°" if switch_angulo.value == False
                    else "rad"
                )

                txt_ang_y.suffix_text = (
                    "°" if switch_angulo.value == False
                    else "rad"
                )

                txt_ang_z.suffix_text = (
                    "°" if switch_angulo.value == False
                    else "rad"
                )

                cont_switch_ang.bgcolor = (
                    "#1F2028" if switch_angulo.value == False
                    else "#65AFB8"
                )

                switch_angulo.label = (
                    "Grados" if switch_angulo.value == False
                    else "Radianes"
                )

                self.page.update()

            switch_angulo: ft.Switch = ft.Switch(
                                label = "Grados",
                                on_change = cambio_angulo,
                            )

            cont_switch_ang: ft.Container = ft.Container(
                                width = medidas["switch"]["ancho_cnt"],
                                height = medidas["switch"]["alto_cnt"],
                                alignment = ft.alignment.center,
                                border_radius = ft.border_radius.all(10),
                                bgcolor = "#1F2028",
                                animate = 200,
                                content = ft.Container(
                                    width = medidas["switch"]["ancho"],
                                    height = medidas["switch"]["alto"],
                                    alignment = ft.alignment.center,
                                    content = switch_angulo,
                                )
                            )

            def cambio_notacion(self) -> None:
                switch_notacion.label = (
                    "Vct. unit." if switch_notacion.value == False
                    else "Conjunto"
                )

                cont_switch_notacion.bgcolor = (
                    "#1F2028" if switch_notacion.value == False
                    else "#65AFB8"
                )

                self.page.update()

            switch_notacion: ft.Switch = ft.Switch(
                                label = "Vctr. unit.",
                                on_change = cambio_notacion,
                            )

            cont_switch_notacion: ft.Container = ft.Container(
                                width = medidas["switch"]["ancho_cnt"],
                                height = medidas["switch"]["alto_cnt"],
                                alignment = ft.alignment.center,
                                border_radius = ft.border_radius.all(10),
                                bgcolor = "#1F2028",
                                animate = 200,
                                content = ft.Container(
                                    width = medidas["switch"]["ancho"],
                                    height = medidas["switch"]["alto"],
                                    alignment = ft.alignment.center,
                                    content = switch_notacion,
                                )
                            )

            # Datos de ejemplo
            # datos.proc_input_vectores('', '', '', '0.785398', '', '', '8', True, False, 'comptes')
            # datos.proc_input_vectores('15', '40', '', '', '', '', '', False, False, 'mag')
            datos.proc_input_vectores('5', '4', '3', '', '', '', '', False, False, 'mag')
            grafica_vectores = grafico.PropiedadesVectores.generador(datos)

            cont_grafica: ft.Container = ft.Container(
                                alignment = ft.alignment.center,
                                content = MatplotlibChart(
                                    grafica_vectores
                                )
                            )

            tab: ft.Tab = ft.Tab(
                text = "Vectores",
                content = 
                ft.Container(
                    border_radius = ft.border_radius.vertical(0, 20),
                    bgcolor = "#0F1115",
                    padding = 25,
                    content =
                    ft.Row(
                        controls = [
                            # Panel princpal de la pestaña (550w x 750h)
                            ft.Container(
                                border_radius = ft.border_radius.all(20),
                                width = medidas["columna1"]["ancho"],
                                height = medidas["columna1"]["alto"],
                                bgcolor = "#3530333D",
                                padding = 20,
                                content =
                                # Columna del panel principal (510w x 650h) - (25 padding lateral)
                                # Total = (510w x 650h) + 10 x (10 espaciado vertical) = (510w x 750h)
                                ft.Column(
                                    spacing = 10,
                                    controls = [
                                        # Título del panel principal (510w x 90h)
                                        ft.Container(
                                            height = medidas["titulo"]["alto"],
                                            width = medidas["titulo"]["ancho"],
                                            alignment = ft.alignment.center,
                                            content = titulo_panel_prcp,
                                            border_radius = ft.border_radius.vertical(20, 0),
                                        ),

                                        # Línea divisora (510w x 2h)
                                        ft.Container(
                                            width = medidas["divisiones"]["ancho"],
                                            height = 2,
                                            bgcolor = "#2F374C"
                                        ),

                                        # Cuadro de texto para magnitud (510w x 80h)
                                        ft.Container(
                                            height = medidas["cuadros_txt"]["alto"],
                                            width = medidas["cuadros_txt"]["ancho_mag"],
                                            alignment = ft.alignment.center,
                                            content = txt_magnitud,
                                        ),

                                        # Cuadros de texto para componente y ángulo en x
                                        # Total = 2 x (250w x 80h) + (10 espaciado) = (510w x 80h)
                                        ft.Row(
                                            width = medidas["filas"]["ancho"],
                                            spacing = 10,
                                            controls = [
                                                ft.Container(
                                                    width = medidas["cuadros_txt"]["ancho"],
                                                    height = medidas["cuadros_txt"]["alto"],
                                                    alignment = ft.alignment.center,
                                                    content = txt_comp_x,
                                                ),
                                                ft.Container(
                                                    width = medidas["cuadros_txt"]["ancho"],
                                                    height = medidas["cuadros_txt"]["alto"],
                                                    alignment = ft.alignment.center,
                                                    content = txt_ang_x,
                                                )
                                            ]
                                        ),

                                        # Cuadros de texto para componente y ángulo en y
                                        # Total = 2 x (250w x 80h) + (10 espaciado) = (510w x 80h)
                                        ft.Row(
                                            width = medidas["filas"]["ancho"],
                                            spacing = 10,
                                            controls = [
                                                ft.Container(
                                                    width = medidas["cuadros_txt"]["ancho"],
                                                    height = medidas["cuadros_txt"]["alto"],
                                                    alignment = ft.alignment.center,
                                                    content = txt_comp_y,
                                                ),
                                                ft.Container(
                                                    width = medidas["cuadros_txt"]["ancho"],
                                                    height = medidas["cuadros_txt"]["alto"],
                                                    alignment = ft.alignment.center,
                                                    content = txt_ang_y,
                                                )
                                            ]
                                        ),

                                        # Cuadros de texto para componente y ángulo en z
                                        # Total = 2 x (250w x 80h) + (10 espaciado) = (510w x 80h)
                                        ft.Row(
                                            width = medidas["filas"]["ancho"],
                                            spacing = 10,
                                            controls = [
                                                ft.Container(
                                                    width = medidas["cuadros_txt"]["ancho"],
                                                    height = medidas["cuadros_txt"]["alto"],
                                                    alignment = ft.alignment.center,
                                                    content = txt_comp_z,
                                                ),
                                                ft.Container(
                                                    width = medidas["cuadros_txt"]["ancho"],
                                                    height = medidas["cuadros_txt"]["alto"],
                                                    alignment = ft.alignment.center,
                                                    content = txt_ang_z,
                                                )
                                            ]
                                        ),

                                        # Texto informativo de sección (170w x 45h) y
                                        # switches de cambio de propiedades 2 x (155w x 45h).
                                        # Total = (480w x 80h) + 2 x (15 espaciado) = (510w x 80h)
                                        ft.Row(
                                            width = medidas["filas"]["ancho"],
                                            spacing = 15,
                                            controls = [
                                                # Texto informativo de la sección
                                                ft.Container(
                                                    width = medidas["switch"]["ancho_opc"],
                                                    height = medidas["switch"]["alto_cnt"],
                                                    alignment = ft.alignment.center,
                                                    content = ft.Text(
                                                        "Opciones adicionales",
                                                        size = 14,
                                                        font_family = "Verdana",
                                                        color = ft.colors.LIGHT_BLUE_200,
                                                        text_align = ft.TextAlign.CENTER
                                                    )
                                                ),
                                                # Switch para cambio de unidad de ángulo
                                                cont_switch_ang,
                                                # Switch para cambio de tipo de componente
                                                cont_switch_notacion
                                            ]
                                        ),

                                        # Línea divisora (510w x 2h)
                                        ft.Container(
                                            width = medidas["divisiones"]["ancho"],
                                            height = 2,
                                            bgcolor = "#2F374C"
                                        ),

                                        # Subtítulo del panel principal (510w x 40h)
                                        ft.Container(
                                            height = medidas["subtitulo"]["alto"],
                                            width = medidas["subtitulo"]["ancho"],
                                            alignment = ft.alignment.center,
                                            content = subtitulo_op
                                        ),

                                        # Línea divisora (510w x 2h)
                                        ft.Container(
                                            width = medidas["divisiones"]["ancho"],
                                            height = 2,
                                            bgcolor = "#2F374C"
                                        ),

                                        # Botones de operaciones 2 x (245w x 45h).
                                        # Total = (490w x 45h) + 2 x (20 espaciado) = (510w x 45h)
                                        ft.Row(
                                            width = medidas["filas"]["ancho"],
                                            spacing = 20,
                                            controls = [
                                                # Botón de cálculo de componentes
                                                ft.ElevatedButton(
                                                    width = medidas["botones"]["ancho"],
                                                    height = medidas["botones"]["alto"],
                                                    bgcolor = "#EFCC57",
                                                    content = ft.Text("Componentes",
                                                                        font_family = "Verdana",
                                                                        color = "#05204A"),
                                                    on_click = calcula_comptes
                                                ),
                                                # Botón de cálculo de magnitud
                                                ft.ElevatedButton(
                                                    width = medidas["botones"]["ancho"],
                                                    height = medidas["botones"]["alto"],
                                                    bgcolor = "#EFCC57",
                                                    content = ft.Text("Magnitud",
                                                                        font_family = "Verdana",
                                                                        color = "#05204A"),
                                                    on_click = calcula_mag
                                                )
                                            ]
                                        ),

                                        # Botones de operaciones 2 x (245w x 45h).
                                        # Total = (490w x 45h) + 2 x (20 espaciado) = (510w x 45h)
                                        ft.Row(
                                            width = medidas["filas"]["ancho"],
                                            spacing = 20,
                                            controls = [
                                                # Botón de cálculo de vector unitario
                                                ft.ElevatedButton(
                                                    width = medidas["botones"]["ancho"],
                                                    height = medidas["botones"]["alto"],
                                                    bgcolor = "#EFCC57",
                                                    content = ft.Text("Vector unitario",
                                                                        font_family = "Verdana",
                                                                        color = "#05204A"),
                                                    on_click = calcula_unitario
                                                ),
                                                # Botón de cálculo de cosenos directores
                                                ft.ElevatedButton(
                                                    width = medidas["botones"]["ancho"],
                                                    height = medidas["botones"]["alto"],
                                                    bgcolor = "#EFCC57",
                                                    content = ft.Text("Cosenos directores",
                                                                        font_family = "Verdana",
                                                                        color = "#05204A"),
                                                    on_click = calcula_cosenos
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ),

                            # Visualizador de propiedades de vector (905w x 750h)
                            ft.Container(
                                border_radius = ft.border_radius.all(20),
                                width = medidas["columna2"]["ancho"],
                                height = medidas["columna2"]["alto"],
                                bgcolor = "#3530333D",
                                padding = 25,
                                alignment = ft.alignment.center,
                                content = cont_grafica
                            )
                        ]
                    )
                )
            )

            return tab


    class OperacionesVectores:
        """
        Contiene el constructor de la pestaña correspondiente a operaciones con vectores
        """

        def build() -> ft.Tab:
            """
            Construye la pestaña correspondiente a operaciones con vectores

            Contiene los elementos que componen a la pestaña

            Regresa un objeto de la clase :class:`ft.Tab`
            """
            tab: ft.Tab = ft.Tab(
                text = "Operaciones con vectores",
                content = ft.Container(
                    content = ft.Text("Esta es la pestaña de operaciones con vectores"),
                    alignment = ft.alignment.center
                )
            )

            return tab


    class Conversiones:
        """
        Contiene el constructor de la pestaña correspondiente a conversiones de unidades
        """

        def build() -> ft.Tab:
            """
            Construye la pestaña correspondiente a conversiones de unidades

            Contiene los elementos que componen a la pestaña

            Regresa un objeto de la clase :class:`ft.Tab`
            """

            tab: ft.Tab = ft.Tab(
                text = "Conversiones",
                content = ft.Container(
                    content = ft.Text("Esta es la pestaña de conversiones de unidades"),
                    alignment = ft.alignment.center
                )
            )

            return tab