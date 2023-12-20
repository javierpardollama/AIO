from tiktak.jugador import Jugador
from common.tinta import Tinta

class Celda:
    def __init__(self, columna: int = 0, fila: int = 0, jugador: Jugador = Jugador.VACIO,
                 activada: bool = False) -> None:
        self.columna = columna
        self.fila = fila
        self.jugador = jugador
        self.activada = activada

    def __str__(self) -> str:
        if self.jugador == Jugador.HUMANO:
            return Tinta.GREEN + " O " + Tinta.BLACK
        elif self.jugador == Jugador.COMPUTADORA:
            return Tinta.RED + " X" + Tinta.BLACK
        else:
            return Tinta.BLACK + " . " + Tinta.BLACK
