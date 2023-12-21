from conway.tipocelda import TipoCelda
from shared.tinta import Tinta
from conway.constantes import  Constantes

class Celda:
    def __init__(self, columna:int, fila:int, tipocelda:TipoCelda = TipoCelda.Muerta):
        self.columna= columna
        self.fila= fila
        self.tipocelda=tipocelda

    def __str__(self) -> str:
        if self.tipocelda == TipoCelda.Muerta:
            return Tinta.RED + Constantes.DEAD + Tinta.BLACK
        else:
            return Tinta.GREEN + Constantes.ALIVE + Tinta.BLACK