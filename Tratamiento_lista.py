class TratamientoListas():
    
    def __init__(self,lista):
        self.lista=lista
        
#_____________________________________________________________________________________________

    def PresentarLista(self):
        print("Recorrer y presentar los datos de una lista")
        for list in self.lista:
            print(list,end='   ')
        print() 

#_____________________________________________________________________________________________        
    
    def buscarLista(self,buscado):
        print("Buscar un valor en una lista")
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                enc=True
                break
        if enc==True:
           print("Su valor si se encuentra en la lista, se encuentra en la posicion: {}".format(pos+1))
        else:
            print("Su valor no se encuentra en la lista")

#_____________________________________________________________________________________________  
    
    def ListaFactorial(self):
        print("Retornar una lista con los factoriales")
        for pos,i in enumerate(self.lista): 
            if i >= 0:
                acu=1
                for num in range(i,1,-1):
                    acu =acu*num
                print("numero:  {}  ,Factorial:  {} ".format(i,acu))
        print()           

#_____________________________________________________________________________________________  
    
    def listaPrimo(self):
        print("Retornar una lista de números primos")
        listaprimo=[]
        for pos,i in enumerate(self.lista): 
            if i >= 0:
                primo=True
                divisor=2
                while divisor < i and primo ==True :
                    Res= i%divisor
                    if Res == 0:
                        primo+=1
                    divisor+=1
                if primo ==True:
                    listaprimo.append(i)
            else:
                print("Su nmumero es negativo ")
        print()
        print("lista de numeros Primos: ")    
        print(listaprimo)
        
        

#_____________________________________________________________________________________________  
    
    def listaNotas(self,listaNotasDicccionario):
        print("Recorrer una lista de diccionario con notas de alumnos")
        for nom in listaNotasDicccionario:
            for clave,valor in nom.items():
                print(clave,":",valor,end="  ")
            print()

#_____________________________________________________________________________________________  
    
    def insertarLista(self,valor,posicion):
        print("Insertar un dato en una Lista dada la Posición")
        print()
        auxlista=[]        
        for pos,ele in enumerate(self.lista):
            if valor < ele:
                break
        for i in range(posicion):
            auxlista.append(self.lista[i])
        auxlista.append(valor)

        for j in range(posicion,len(self.lista)):
            auxlista.append(self.lista[j])
        self.lista=auxlista
        return self.lista

#_____________________________________________________________________________________________  
    
    def eliminarLista(self,lista):
        print("Eliminar todas las ocurrencias en una Lista")
        print()
        lista2 = {}
        for i in lista:
            if i in lista2:
                lista2[i] += 1
            else:
                lista2[i] = 1 
        print("Queda lo siguiente:",lista2)
        print("En total son {} elementos sin contar las repeticiones".format(len(lista2)))
        lista3 = []        
        for clave, valor in enumerate(lista2):
            lista3.append(valor)
        return (lista3)   

        
#_____________________________________________________________________________________________  
    
    def retornaValorLista(self,lista):
        print(" Retornar cualquier valor de una lista eliminándolo ")
        print()
        n=int(input("que valor quieres eliminar: "))      
        for x,i in enumerate(lista):
            if i == n:
                del lista[x]  
        return (lista)

#_____________________________________________________________________________________________  
    
    def copiarTuplaLista(self):
        print(" Copiar cada elemento de una tupla en una lista ")
        aux1=list(self.tupla)
        return aux1      

#_____________________________________________________________________________________________  
    
    def vueltoLista(self,listaClientesDiccionario):
        print(" Dar el vuelto a varios clientes ")
        for key in listaClientesDiccionario:
            print("------")
            print(key,':',listaClientesDiccionario[key])
        

       
        
        
#_____________________________________________________________________________________________  
 
pos=2
diccionario=[{'nombre':'Josue', 'nota':100},{'nombre':'Mario','nota':80},{'nombre':'Miguel','nota':90}]
lista=[0,-2,5,3,40,50]
tupla=(22,23,24,25)
listaClientesDiccionarios=[{'cliente':'Josue','deuda':100},{'cliente':'Maria','deuda':80},{'cliente':'Ruth','deuda':50}]
ord1= TratamientoListas(lista)
#ord1.PresentarLista()
#ord1.buscarLista(40)
# ord1.ListaFactorial()
ord1.listaPrimo()
# ord1.listaNotas(diccionario)
# print(ord1.insertarLista(600,5))
# print()
# lista1 = []       
# num = int(input("Cuantos elementos desea en la lista?: "))
# for x in range(num):
#     valor = int(input("Ingrese el elemento:")) 
#     lista1.append(valor)
# aux=lista1
# print(ord1.eliminarLista(aux))
# lista2 = []       
# num = int(input("Cuantos elementos desea en la lista?: "))
# for x in range(num):
#     valor = int(input("Ingrese el elemento:")) 
#     lista2.append(valor)
# aux=lista2
# print(ord1.retornaValorLista(aux))
#print(ord1.copiarTuplaLista())
#ord1.vueltoLista(listaClientesDiccionarios)

