class Cadena():
    def __init__(self,cadena):
        self.cadena=cadena

#___________________________________________________________________________________________________________   
    def  recorrerCadena(self):
        print(':::::::::::::::::::::::::::::::::::::::::::::')
        print("Recorrer y presentar los datos de una cadena")
        print(':::::::::::::::::::::::::::::::::::::::::::::')
        for x in self.cadena:
            print(x,'',end='')
        
#___________________________________________________________________________________________________________  
    def  buscarCaracter(self,buscado):
        print(':::::::::::::::::::::::::::::::::::::')
        print("Buscar un carácter en una cadena")
        print(':::::::::::::::::::::::::::::::::::::')
        acum=0
        for x,i in enumerate(self.cadena):
            if i== buscado:
                acum=acum+1
        print("Su caracter se encuentra {} veces, dentro de la cadena".format(acum))
        print()
        
#___________________________________________________________________________________________________________  
    def  listaPosiciones(self,caracter):
        pass
#___________________________________________________________________________________________________________  
    def listaPalabras(self):
        pass
#___________________________________________________________________________________________________________  
    def cadenaLista(self):
        pass
#___________________________________________________________________________________________________________  
    def insertarDato(self,buscado,posicion):
        pass
#___________________________________________________________________________________________________________  
    def eliminarOcurrencias(buscado):
        pass
#___________________________________________________________________________________________________________  
    def retornaValor(posicion):
        pass
#___________________________________________________________________________________________________________  
    def concatenarCadena(dato):
        pass
#___________________________________________________________________________________________________________         

cadena='hola como esta me miro y acercandose no lo podia creer'
cad= Cadena(cadena)
# cad.recorrerCadena()
cad.buscarCaracter('b')