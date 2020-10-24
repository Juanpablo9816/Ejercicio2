class ViajeroFrecuente():
    __NViajero = 0
    __DNI = 0
    __Nombre = ""
    __Apellido = ""
    __Millas = 0.0

    def __init__(self,NV,DNI,Nom,Apell,Mill):
        self.__NViajero = NV
        self.__DNI = DNI
        self.__Nombre = Nom
        self.__Apellido = Apell
        self.__Millas = Mill

    def AcumularMillas(self,Mill):
        self.__Millas =self.__Millas+Mill
    def CanjearMillas (self, cantidad):
        self.__Millas -= cantidad
    def getnum(self):
        return self.__NViajero
    def getMillas(self):
        return self.__Millas
    
