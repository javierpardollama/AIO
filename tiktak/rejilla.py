from tiktak.celda import Celda
from tiktak.jugador import Jugador
from tiktak.constantes import Constantes
import os


class Rejilla:

    def __init__(self) -> None:
        self.celdas: list[Celda] = []

        for i in range(Constantes.TAMAÑO):
            for j in range(Constantes.TAMAÑO):
                self.celdas.append(Celda(i, j, Jugador.VACIO, False))

    def __str__(self) -> str:
        rst: str = ""

        for fila in range(Constantes.TAMAÑO):
            for columna in range(Constantes.TAMAÑO):
                cell: Celda = next(filter(lambda item: item.fila == fila and item.columna == columna, self.celdas),
                                   None)

                rst = rst + cell.__str__()

                if columna == range(Constantes.TAMAÑO)[-1]:
                    rst = f"{rst}{os.linesep}"

        return rst
