from conway import Celda, TipoCelda
from conway.rejilla import Rejilla
from conway.constantes import Constantes
from shared import Motor


class Juego(Motor):
    def __init__(self):
        super().__init__()
        self.rejilla = Rejilla()
        self.rejilla.__set_grid__()
        self.rejilla.__set_alive__()

    def __start__(self) -> None:
        print(self.rejilla.__str__())
        self.next_turn_grid()

    def next_turn_grid(self)-> None:
        for turno in range(Constantes.DEFAULT_GAME_TURNS):
            for fila in range(Constantes.DEFAULT_GRID_HEIGHT):
                for columna in range(Constantes.DEFAULT_GRID_WIDTH):
                    celda: Celda = next(filter(lambda item: item.fila == fila and item.columna == columna, self.rejilla.celdas),
                                       None)
                    self.get_cell_living_neighbors(celda)

            print(f"TURNO {turno}")
            print(self.rejilla.__str__())

    def get_cell_living_neighbors(self, celda:Celda):
        vecinos: list[Celda] = []

        arriba_izq = next(filter(lambda item: item.fila == celda.fila - 1 and item.columna == celda.columna - 1 and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
                                   None)

        if arriba_izq is not None:
            vecinos.append(arriba_izq)

        arriba_cen = next(
            filter(lambda item: item.fila == celda.fila - 1 and item.columna == celda.columna and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
            None)

        if arriba_cen is not None:
            vecinos.append(arriba_cen)

        arriba_der = next(
            filter(lambda item: item.fila == celda.fila - 1 and item.columna == celda.columna + 1 and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
            None)

        if arriba_der is not None:
            vecinos.append(arriba_der)

        izq = next(filter(lambda item: item.fila == celda.fila and item.columna == celda.columna - 1 and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
                                   None)

        if izq is not None:
            vecinos.append(izq)

        der = next(
            filter(lambda item: item.fila == celda.fila and item.columna == celda.columna + 1 and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
            None)

        if der is not None:
            vecinos.append(der)

        abajo_izq = next(
            filter(lambda item: item.fila == celda.fila + 1 and item.columna == celda.columna - 1 and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
            None)

        if abajo_izq is not None:
            vecinos.append(abajo_izq)

        abajo_cen = next(
            filter(lambda item: item.fila == celda.fila + 1 and item.columna == celda.columna and item.tipocelda == TipoCelda.Viva, self.rejilla.celdas),
            None)

        if abajo_cen is not None:
            vecinos.append(abajo_cen)

        abajo_der = next(
            filter(lambda item: item.fila == celda.fila + 1 and item.columna == celda.columna + 1, self.rejilla.celdas),
            None)

        if abajo_der is not None:
            vecinos.append(abajo_der)

        count:int = vecinos.__len__()

        if celda.tipocelda == TipoCelda.Viva:
            if count < Constantes.TWO_TO_DEAD_NEIGHBOURS:
                celda.tipocelda = TipoCelda.Muerta
            elif count in Constantes.TO_DEAD_NEIGHBOURS:
                celda.tipocelda = TipoCelda.Viva
            else:
                celda.tipocelda = TipoCelda.Muerta

        elif celda.tipocelda == TipoCelda.Muerta and count in Constantes.TO_ALIVE_NEIGHBOURS:
            celda.tipocelda = TipoCelda.Viva

        idx = list(map(lambda item: item.fila == celda.fila and item.columna == celda.columna, self.rejilla.celdas)).index(True)

        self.rejilla.celdas[idx].tipocelda = celda.tipocelda
