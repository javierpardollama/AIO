from conway.juego import Juego as Conway
from tiktak.juego import Juego as TikTak
from dungeon.juego import Juego as Dungeon

class Nucleo:

    def __init__(self):
        self.conway = Conway()
        self.tiktak = TikTak()
        self.dungeon = Dungeon()

    def __start__(self):
        opcion: str = ""

        while opcion not in ["1", "2", "3", "4"]:
            opcion = (input("\n" +
                            "************************************** \n" +
                            "************* ¿QUE JUEGO? ************ \n" +
                            "1. TRES EN RAYA \n" +
                            "2. MAZMORRAS & DRAGONES \n" +
                            "3. JUEGO DE LA VIDA \n" +
                            "4. SALIR \n" +
                            "************************************** \n")).upper()

            match opcion:
                case "1":
                    self.tiktak.__start__()
                    self.__start__()
                case "2":
                  self.dungeon.__start__()
                  self.__start__()
                case "3":
                    self.conway.__start__()
                    self.__start__()
                case "4":
                    self.stop()

    def stop(self) -> None:
        quit()