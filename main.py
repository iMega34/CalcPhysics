
from gui_struct import GUI

import flet as ft


def page(page: ft.Page):
    # Propiedades de la ventana de la GUI
    page.title = "CalcPhysics"
    page.bgcolor = "#1F2129"
    page.window_full_screen = True

    # Pestañas de la GUI
    secciones: ft.Tabs = GUI.build_secciones()

    page.add(
        secciones
    )

    # print(f"Ancho: {page.window_width} px\nLargo: {page.window_height} px")

ft.app(target = page)
