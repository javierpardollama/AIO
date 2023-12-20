from dungeon.tipocelda import TipoCelda
from common.tinta import Tinta


class Celda:

    def __init__(self, columna: int, fila: int, tipo_celda: TipoCelda = TipoCelda.Standard) -> None:
        self.columna = columna
        self.fila = fila
        self.tipo_celda = tipo_celda

    def __str__(self) -> str:
        match self.tipo_celda:
            case TipoCelda.Muro:
                return Tinta.ORANGE + " X " + Tinta.BLACK
            case TipoCelda.Salida:
                return Tinta.BLUE + " > " + Tinta.BLACK
            case TipoCelda.Jugador:
                return Tinta.GREEN + " @ " + Tinta.BLACK
            case TipoCelda.Monstruo:
                return Tinta.RED + " $ " + Tinta.BLACK
            case TipoCelda.Standard:
                return Tinta.BLACK + " . " + Tinta.BLACK
