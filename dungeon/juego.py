from random import randrange
from dungeon import Rejilla, TipoCelda, Monstruo, Jugador, Movimiento, Salida, Celda
from shared import Motor


class Juego(Motor):

    def __init__(self):
        super().__init__()
        self.rejilla = Rejilla()
        self.rejilla.__set_grid__()
        self.rejilla.__set_walls__()

        self.monstruo = Monstruo()
        self.jugador = Jugador()
        self.salida = Salida()

        self._set_player__()
        self._set_monster__()
        self._set_exit__()

    def _set_monster__(self) -> None:

        rand_fila: int = randrange(self.rejilla.filas)
        rand_col: int = randrange(self.rejilla.columnas)

        self.monstruo = Monstruo(rand_fila, rand_col)
        self.rejilla.__set_cell_type__(rand_fila, rand_col, TipoCelda.Monstruo)

    def _set_player__(self) -> None:
        self.jugador = Jugador(0, 0)
        self.rejilla.__set_cell_type__(0, 0, TipoCelda.Jugador)

    def _set_exit__(self) -> None:
        self.salida = Salida(self.rejilla.filas - 1, self.rejilla.columnas - 1)
        self.rejilla.__set_cell_type__(self.rejilla.filas - 1, self.rejilla.columnas - 1, TipoCelda.Salida)

    def __start__(self) -> None:
        print(self.rejilla.__str__())

        movimiento: str = ""

        if self.__die__():
            self.__restart__()

        while movimiento not in ["W", "A", "S", "D", "Q"]:

            movimiento = (input("\n" +
                                "******************************************\n" +
                                "******* INTRODUCE TU movimiento **********\n" +
                                "1. W \n" +
                                "2. A \n" +
                                "3. S \n" +
                                "4. D \n" +
                                "5. Q \n" +
                                "******************************************\n")).upper()

            match movimiento:
                case "W":
                    self.__move_player__(Movimiento.Arriba)
                    self.__move_monster__(Movimiento.Abajo)
                case "A":
                    self.__move_player__(Movimiento.Izquierda)
                    self.__move_monster__(Movimiento.Derecha)
                case "S":
                    self.__move_player__(Movimiento.Abajo)
                    self.__move_monster__(Movimiento.Arriba)
                case "D":
                    self.__move_player__(Movimiento.Derecha)
                    self.__move_monster__(Movimiento.Izquierda)
                case "Q":
                    self.__stop__()

            if self.__die__() or self.__win__():
                self.__restart__()

            movimiento = ""
            print(self.rejilla.__str__())

    def __restart__(self) -> None:

        movimiento: str = ""

        while movimiento not in ["Y", "S", "N", "Q"]:
            movimiento = (input("\n" +
                                "******************************************\n"
                                "********* ¿COMENZAR DE NUEVO? ************\n" +
                                "1. Y \n" +
                                "2. S \n" +
                                "3. N \n" +
                                "4. Q \n" +
                                "******************************************\n")).upper()

            match movimiento:
                case "Y":
                    self.__init__()
                    self.__start__()
                case "S":
                    self.__init__()
                    self.__start__()
                case "N":
                    self.__stop__()
                case "Q":
                    self.__stop__()

    def __stop__(self) -> None:
        quit()

    def __win__(self) -> bool:
        bandera: bool = self.jugador.fila == self.salida.fila and self.jugador.columna == self.salida.columna

        if bandera:
            print("¡CONSEGUIDO! ¡HAS LLEGADO A SALVO!")

        return bandera

    def __die__(self) -> bool:
        bandera: bool = self.jugador.fila == self.monstruo.fila and self.jugador.columna == self.monstruo.columna

        if bandera:
            print("¡LO SIENTO! ¡HAS MUERTO!")

        return bandera

    def __collide__(self, fila: int = 0, columna: int = 0) -> bool:
        celda: Celda = next(filter(lambda item: item.fila == fila and item.columna == columna, self.rejilla.celdas), None)

        bandera:bool = celda.tipo_celda == TipoCelda.Muro

        return bandera

    def __move_player__(self, movimiento: Movimiento) -> None:
        match movimiento:
            case Movimiento.Arriba:
                if not self.jugador.fila - 1 <= self.rejilla.filas and not self.__collide__(self.jugador.fila - 1, self.jugador.columna):
                    self.rejilla.__set_cell_type__(self.jugador.fila, self.jugador.columna, TipoCelda.Standard)
                    self.rejilla.__set_cell_type__(self.jugador.fila - 1, self.jugador.columna, TipoCelda.Jugador)
                    self.jugador.__arriba__()

            case Movimiento.Izquierda:
                if not self.jugador.columna - 1 <= self.rejilla.columnas and  not self.__collide__(self.jugador.fila, self.jugador.columna-1):
                    self.rejilla.__set_cell_type__(self.jugador.fila, self.jugador.columna, TipoCelda.Standard)
                    self.rejilla.__set_cell_type__(self.jugador.fila, self.jugador.columna - 1, TipoCelda.Jugador)
                    self.jugador.__izquierda__()

            case Movimiento.Abajo:
                if not self.jugador.fila + 1 >= self.rejilla.filas and  not self.__collide__(self.jugador.fila + 1, self.jugador.columna):
                    self.rejilla.__set_cell_type__(self.jugador.fila, self.jugador.columna, TipoCelda.Standard)
                    self.rejilla.__set_cell_type__(self.jugador.fila+1, self.jugador.columna, TipoCelda.Jugador)
                    self.jugador.__abajo__()

            case Movimiento.Derecha:
                if not self.jugador.columna + 1 >= self.rejilla.columnas and  not self.__collide__(self.jugador.fila, self.jugador.columna+1):
                    self.rejilla.__set_cell_type__(self.jugador.fila, self.jugador.columna, TipoCelda.Standard)
                    self.rejilla.__set_cell_type__(self.jugador.fila, self.jugador.columna+1, TipoCelda.Jugador)
                    self.jugador.__derecha__()

    def __move_monster__(self, movimiento: Movimiento) -> None:
        match movimiento:
            case Movimiento.Arriba:
                if not self.monstruo.fila - 1 <= self.rejilla.filas:
                    self.rejilla.__set_cell_type__(self.monstruo.fila, self.monstruo.columna, TipoCelda.Standard)
                    self.rejilla.__set_cell_type__(self.monstruo.fila - 1, self.monstruo.columna, TipoCelda.Monstruo)
                    self.monstruo.__arriba__()

            case Movimiento.Izquierda:
                if not self.monstruo.columna - 1 <= self.rejilla.columnas:
                    self.rejilla.__set_cell_type__(self.monstruo.fila, self.monstruo.columna, TipoCelda.Standard)
                    self.rejilla.__set_cell_type__(self.monstruo.fila, self.monstruo.columna - 1, TipoCelda.Monstruo)
                    self.monstruo.__izquierda__()

            case Movimiento.Abajo:
                if not self.monstruo.fila + 1 >= self.rejilla.filas:
                    self.rejilla.__set_cell_type__(self.monstruo.fila, self.monstruo.columna, TipoCelda.Standard)
                    self.rejilla.__set_cell_type__(self.monstruo.fila + 1, self.monstruo.columna, TipoCelda.Monstruo)
                    self.monstruo.__abajo__()

            case Movimiento.Derecha:
                if not self.monstruo.columna + 1 >= self.rejilla.columnas:
                    self.rejilla.__set_cell_type__(self.monstruo.fila, self.monstruo.columna, TipoCelda.Standard)
                    self.rejilla.__set_cell_type__(self.monstruo.fila, self.monstruo.columna + 1, TipoCelda.Monstruo)
                    self.monstruo.__derecha__()
