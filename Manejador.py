class Listaiviajero():
    __lista = None

    def __init__ (self):
        self.__lista = []

    def LeerArchivo(self):
        import csv
        from Clase_ViajeroFrecuente import ViajeroFrecuente
        archivo = open("Viajeros.csv")
        reader = csv.reader(archivo,delimiter = ';')

        for viajero in reader:
            self.__lista.append(ViajeroFrecuente(viajero[0],viajero[1],viajero[2],viajero[3],viajero[4]))

        archivo.close()

    def Buscar(self,Nv):
        i = 0
        while ((i<len(self.__lista)) and (int(Nv) != int(self.__lista[i].getnum()))):
            i += 1
        
        if(i<len(self.__lista)):
            return i
        else:
            return -1

    def MuestraCantidad(self,Nv):
        posicion = self.Buscar(Nv)
        print(posicion)
        if posicion != -1:
            print("La cantidad total de millas acumuladas en de ",self.__lista[posicion].getMillas())
        else:
            print("No existe el Viajero")
    def GetTamañodeLista(self):
        return len(self.__lista)
    def AcumulaCantidad(self,Nv):
        posicion = self.Buscar(Nv)
        if posicion != -1:
            Milla = input("Ingrese cantidad de millas recorridas en el ultimo viaje ")
            self.__lista[posicion].AcumularMillas(Milla)
            print("Millas añadidas sastifactoriamete")
        else:
            print("El viajero no existe ")
    def CanjearMilla(self,Nv,canje):
        posicion = self.Buscar(Nv)
        if posicion != -1:
            if canje <= int(self.__lista[posicion].getMillas()):
                self.__lista[posicion].CanjearMillas(canje)
                print("La cantidad de millas restantes es: {}".format(self.__lista[posicion].getMillas()))
            else:
                print("Error,la cantidad solicitada es mayor que la que tiene el viajero")
        else:
            print("No se encontro numero de viajero")


