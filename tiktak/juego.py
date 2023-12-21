from random import randrange

from shared import Motor
from tiktak import (Rejilla, Constantes, Jugador,Celda)
from shared.tinta import  Tinta


class Juego(Motor):
    def __init__(self):
        super().__init__()
        self.rejilla = Rejilla()

    def __start__(self) -> None:
        print(self.rejilla.__str__())

        human_win, computer_win, filled_in = self.__current_satus__()

        while not human_win or not computer_win or not filled_in:
            self.__activate_human__()
            print(self.rejilla.__str__())
            self.__restart__()
            self.__activate_computer__()
            print(self.rejilla.__str__())
            self.__restart__()

    def __restart__(self) -> None:

        human_win, computer_win, filled_in = self.__current_satus__()

        if human_win or computer_win or filled_in:
            movimiento: str = ""

            while movimiento not in ["Y", "S", "N", "Q"]:
                movimiento = (input("\n" +
                                    "************************************** \n" +
                                    "******** ¿COMENZAR DE NUEVO? ********* \n" +
                                    "1. Y \n" +
                                    "2. S \n" +
                                    "3. N \n" +
                                    "4. Q \n" +
                                    "************************************** \n")).upper()

                match movimiento:
                    case "Y":
                        self.__init__()
                        self.__start__()
                    case "S":
                        self.__init__()
                        self.__start__()
                    case "N":
                        self.stop()
                    case "Q":
                        self.stop()

    def __current_satus__(self) -> tuple[bool, bool, bool]:
        human_win: bool = self.__win__(Jugador.HUMANO)
        computer_win: bool = self.__win__(Jugador.COMPUTADORA)
        filled_in: bool = self.__filled__()

        if human_win:
            print(f"******* JUGADOR {Tinta.GREEN} 0 {Tinta.BLACK} HAS GANADO **********  \n")

        if computer_win:
            print(f"******* JUGADOR {Tinta.GREEN} 0 {Tinta.BLACK} HAS PERDIDO **********  \n")

        return human_win, computer_win, filled_in

    def __activate_human__(self) -> None:
        columna, fila = self.__intro_human__()

        while not self.__check_cell__(columna, fila):
            columna, fila = self.__intro_human__()

        self.__activate_cell__(columna, fila, Jugador.HUMANO)

    def __intro_human__(self) -> tuple[int, int]:
        columna: str = ""

        fila: str = ""

        while not columna.isnumeric() and columna not in range(Constantes.TAMAÑO):
            columna = input(f"******* JUGADOR {Tinta.GREEN} 0 {Tinta.BLACK} INTRODUCE TU COLUMNA **********  \n")

        while not fila.isnumeric() and fila not in range(Constantes.TAMAÑO):
            fila = input(f"******* JUGADOR {Tinta.GREEN} 0 {Tinta.BLACK} INTRODUCE TU FILA **********  \n")

        return int(columna), int(fila)

    def __activate_computer__(self) -> None:
        columna, fila = self.__intro_computer__()

        while not self.__check_cell__(columna, fila):
            columna, fila = self.__intro_computer__()

        self.__activate_cell__(columna, fila, Jugador.COMPUTADORA)

    def __intro_computer__(self) -> tuple[int, int]:
        return randrange(Constantes.TAMAÑO), randrange(Constantes.TAMAÑO)

    def __activate_cell__(self, columna: int, fila: int, jugador: Jugador) -> None:
        idx = list(map(lambda item: item.columna == columna and item.fila == fila, self.rejilla.celdas)).index(True)

        self.rejilla.celdas[idx].jugador = jugador
        self.rejilla.celdas[idx].activada = True

    def __check_cell__(self, columna: int, fila: int) -> bool:
        obj = next(
            filter(lambda item: not (not (item.columna == columna) or not (item.fila == fila) or item.activada),
                   self.rejilla.celdas), None)
        return obj is not None

    def __filled__(self) -> bool:
        return list(filter(lambda item: item.activada, self.rejilla.celdas)).__len__() == (
                Constantes.TAMAÑO ** Constantes.TAMAÑO)

    def __win__(self, jugador: Jugador) -> bool:
        vertical: bool = self.__vertical__(jugador)
        horizontal: bool = self.__horizontal__(jugador)
        izq_diagonal: bool = self.__left_diagonal__(jugador)
        der_diagonal: bool = self.__right_diagonal__(jugador)

        return vertical | horizontal | izq_diagonal | der_diagonal

    def __vertical__(self, jugador: Jugador) -> bool:
        count: int = list(
            filter(lambda item: item.activada and item.jugador == jugador and item.columna in range(Constantes.TAMAÑO),
                   self.rejilla.celdas)).__len__()

        return count == Constantes.TAMAÑO

    def __horizontal__(self, jugador: Jugador) -> bool:
        count: int = list(
            filter(lambda item: item.activada and item.jugador == jugador and item.fila in range(Constantes.TAMAÑO),
                   self.rejilla.celdas)).__len__()

        return count == Constantes.TAMAÑO

    def __left_diagonal__(self, jugador: Jugador) -> bool:
        count: int = list(filter(lambda item: item.activada and item.jugador == jugador and item.fila == item.columna,
                                 self.rejilla.celdas)).__len__()

        return count == Constantes.TAMAÑO

    def __right_diagonal__(self, jugador: Jugador) -> bool:
        diag: list[Celda] = []

        for fila in range(Constantes.TAMAÑO):
            for columna in reversed(range(Constantes.TAMAÑO)):
                obj = next(filter(lambda item: item.columna == columna and item.fila == fila and item.activada and item.jugador == jugador, self.rejilla.celdas), None)
                if obj is not None:
                    diag.append(obj)

        count: int = diag.__len__()

        return count == Constantes.TAMAÑO

    def stop(self) -> None:
        quit()
