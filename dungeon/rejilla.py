import os
from random import randrange
from dungeon.tipocelda import TipoCelda
from dungeon.celda import Celda


class Rejilla:
    def __init__(self, columnas: int = 15, filas: int = 7, porcentage: int = 30) -> None:
        self.celdas: list[Celda] = []
        self.columnas = columnas
        self.filas = filas
        self.porcentage = porcentage

    def __str__(self) -> str:
        rst: str = ""

        for fila in range(self.filas):
            for columna in range(self.columnas):

                cell: Celda = next(filter(lambda item: item.fila == fila and item.columna == columna, self.celdas), None)

                rst = rst + cell.__str__()

                if columna == range(self.columnas)[-1]:
                    rst = f"{rst}{os.linesep}"

        return rst

    def __set_grid__(self) -> None:
        for fila in range(self.filas):
            for columna in range(self.columnas):
                self.celdas.append(Celda(columna, fila, TipoCelda.Standard))

    def __set_walls__(self) -> None:
        muros: int = round(self.columnas * self.filas * (self.porcentage / 100) / 2)

        rand_col: int = randrange(self.columnas)
        rand_fila: int = randrange(self.filas)

        for muro in range(muros):
            rand_col: int = randrange(self.columnas)
            rand_fila: int = randrange(self.filas)

            idx = list(map(lambda item: item.fila == rand_fila and item.columna == rand_col, self.celdas)).index(True)

            self.celdas[idx].tipo_celda = TipoCelda.Muro

    def __set_cell_type__(self, fila: int = 0, columna: int = 0, tipo_celda:TipoCelda= TipoCelda.Standard):
        idx = list(map(lambda item: item.fila == fila and item.columna == columna, self.celdas)).index(True)
        self.celdas[idx].tipo_celda = tipo_celda
