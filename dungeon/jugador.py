class Jugador:
    def __init__(self, fila: int = 0, columna: int = 0) -> None:
        self.fila = fila
        self.columna = columna

    def __arriba__(self) -> None:
        self.fila = self.fila - 1

    def __abajo__(self) -> None:
        self.fila = self.fila + 1

    def __derecha__(self) -> None:
        self.columna = self.columna + 1

    def __izquierda__(self) -> None:
        self.columna= self.columna - 1
