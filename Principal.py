if __name__ == "__main__":
    from Manejador import Listaiviajero
    Lista = Listaiviajero()
    Lista.LeerArchivo()
    def op1():
        
        Lista.MuestraCantidad(numero)
    def op2():
        Lista.AcumulaCantidad(numero)
    def op3():
        Lista.CanjearMilla()
        pass
    numero = input("Ingrese numero del viajero a consultar ")
    diccionario = {1:op1,2:op2,3:op3}

    while int(numero) < int(Lista.GetTamañodeLista()) and numero != -1:    
        opcion = None
        while opcion != 4:
            print("Ingrese 1 para Consultar cantidad de millas ")
            print("Ingrese 2 para Acumular millas ")
            print("Ingres 3 para canjear millas ")
            print("Ingrese 4 para salir")
            opcion = int(input("Ingrese opcion "))
            op = diccionario.get(opcion,lambda: print("Se ingreso una opcion incarrecta"))
            op()
        numero = input("Ingrese numero del viajero a consultar ")
        
