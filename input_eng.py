
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
