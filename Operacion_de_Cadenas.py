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
        print('::::::::::::::::::::::::::::::::::')
        print("Buscar un carácter en una cadena")
        print('::::::::::::::::::::::::::::::::::')
        acum=0
        for x,i in enumerate(self.cadena):
            if i== buscado:
                acum=acum+1
        print("Su caracter se encuentra {} vez(veces), dentro de la cadena".format(acum))
        print()
#___________________________________________________________________________________________________________  
    def  listaPosiciones(self,caracter):
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print("Retornar una lista con la posiciones dado un carácter de la cadena")
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        acum=0
        aux=[]
        for x,i in enumerate(self.cadena):
            acum=acum+1
            if i == caracter:
                aux.append(acum)
                lista=aux
        print(lista)        
                
#___________________________________________________________________________________________________________  
    def listaPalabras(self):
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print("Retornar una lista con todas las palabras de una cadena")
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::')  
        print(self.cadena.split())
#___________________________________________________________________________________________________________  
    def cadenaLista(self):
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print("       Retornar una cadena a partir de una lista")
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print(" ".join(self.cadena))
#___________________________________________________________________________________________________________  
    def insertarDato(self,insertar,posicion):
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print("   Insertar un dato en una cadena dada lo Posición")
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        if posicion <= len(self.cadena):
            izquierda = self.cadena[:posicion]
            derecha =self.cadena[posicion+1:]
            
            print("{} {} {}".format(izquierda, insertar, derecha))
        else:
            print("La posicion no existe")
        
#___________________________________________________________________________________________________________  
    def eliminarOcurrencias(self,buscado):
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print("    Eliminar todas las ocurrencias en una cadena")
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

        print("El elemento buscado se encontro {} veces en la cadena".format(self.cadena.count(buscado)))
#___________________________________________________________________________________________________________  
    def retornaValor(self,posicion):
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print(" Retornar cualquier valor de una cadena eliminándolo ")
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

        lista = []
        lista2 = []
        for pos, ele in enumerate (self.cadena):
            if pos == posicion:
                lista.append(self.cadena[pos])      
            else:
                lista2.append(self.cadena[pos])
        print("Se retorna la cadena de esta forma:")
        print(" ".join(lista2))     
        print("Letra de la posicion removido:")           
        print(" ".join(lista))
#___________________________________________________________________________________________________________  
    def concatenarCadena(self,nombre):
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print("                       Concatenar Cadena")
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        dato = "Hola, señor(a)"
        final= "Usted a usado nuestro programa cadena."
        frase= dato+" "+nombre+" "+final
        print(frase)
#___________________________________________________________________________________________________________         

# cadena='hola como esta me miro y acercandose no lo podia creer'
# cad= Cadena(cadena)
# # cad.recorrerCadena()
# #cad.buscarCaracter('b')
# cad.listaPosiciones('p')
