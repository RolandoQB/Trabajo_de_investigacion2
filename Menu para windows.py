import os
from typing import Text
from Calculadora import CalEstandar, calCientifica
from Operacion_Numeros import Basico, Intermedio
from Tratamiento_lista import TratamientoListas
from Operacion_de_Cadenas import Cadena

class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo=titulo
        self.opciones= opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija la opción [1...{}]:".format(len(self.opciones)))
        return opc
opc = ""
while opc != "5":
    os.system("cls")
    men = Menu("Menu Principal",["1)Calculadora", "2)Operación Numeros", "3)Tratamiento de Listas","4)Operacion de Cadenas", "5)Salir" ])
    opc = men.menu()

    if opc == "1":
        opc1 = ""
        while opc1 != "10":
            os.system("cls")
            men1 = Menu("Menu Calculadora",["1)Suma", "2)Resta", "3)Multiplicación","4)División", "5)Exponente", "6)Valor Absoluto", "7)Circunferencia", "8)Area del Circulo", "9)Area del Cuadrado", "10)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("<----Ingrese los numeros para la respectiva suma---->")
                n1 = int(input("Ingrese el primer valor:"))
                n2 = int(input("Ingrese el segundo valor:"))
                cal = CalEstandar(n1,n2)
                cal.suma()
                input("Presione una tecla para continuar...")
                
            elif opc1 == "2":
                os.system("cls")
                print("<----Ingrese los numeros para la respectiva resta---->")
                n1 = int(input("Ingrese el primer valor:"))
                n2 = int(input("Ingrese el segundo valor:"))
                cal = CalEstandar(n1,n2)
                cal.resta()
                input("Presione una tecla para continuar...")
                
            elif opc1 == "3":
                os.system("cls")
                print("<----Ingrese los numeros para la respectiva multiplicacion---->")
                n1 = int(input("Ingrese el primer valor:"))
                n2 = int(input("Ingrese el segundo valor:"))
                cal = CalEstandar(n1,n2)
                print("La multiplicacin del numero {} y {} es:".format(n1,n2),cal.multiplicacion())
                input("Presione una tecla para continuar...")
             
            elif opc1 == "4":
                os.system("cls")
                print("<----Ingrese los numeros para la respectiva division---->")
                n1 = int(input("Ingrese el primer valor:"))
                n2 = int(input("Ingrese el segundo valor:"))
                cal = CalEstandar(n1,n2)
                cal.division()
                input("Presione una tecla para continuar...")   
                
            elif opc1 == "5":
                os.system("cls")
                print("<----Exponentes---->")
                n1 = int(input("Ingrese el primer valor como base:"))
                n2 = int(input("Ingrese el segundo valor como exponente:"))
                cal = CalEstandar(n1,n2)
                cal.exponente()
                input("Presione una tecla para continuar...")
                
            elif opc1 == "6":
                os.system("cls")
                print("<----Valor Absoluto---->")
                n1 = int(input("Ingrese el numero:"))
                cal = CalEstandar(0,0)
                print("El Valor Absoluto es: ",cal.valorAbsoluto(n1))
                input("Presione una tecla para continuar...") 
            
            elif opc1 == "7":
                os.system("cls")
                print("<----Circunferencia---->")
                n1 = int(input("Ingrese el valor del radio:"))
                cal = calCientifica(n1,0)
                print("El perimetro de la circunferencia es: ",cal.circunferencia())
                input("Presione una tecla para continuar...")
                
            elif opc1 == "8":
                os.system("cls")
                print("<----Area del Circulo---->")
                n1 = int(input("Ingrese el valor del radio:"))
                cal = calCientifica(n1,0)
                print("El area del Circulo es: ",cal.areaCirculo())
                input("Presione una tecla para continuar...")  
                
            elif opc1 == "9":
                os.system("cls")
                print("<----Area del Cuadrado---->")
                n2 = int(input("Ingrese el valor del lado:"))
                cal = calCientifica(0,n2)
                print("El area del cuadrado es: ",cal.areaCuadrado())
                input("Presione una tecla para continuar...")   

    elif opc == "2":
        opc2 = ""
        while opc2 != "10":
            os.system("cls")
            men2 = Menu("Menu Operación Numeros",["1)numerosN", "2)Multiplo", "3)Divisores Numero","4)Primo", "5)Perfecto", "6)factorial", "7)Fibonacci", "8)Primos Gemelos", "9)Amigos", "10)Salir"])
            opc2 = men2.menu()
            if opc2 == "1":
                os.system("cls")
                print("<----Presentar los números de 1 a n---->")
                n1 = int(input("Ingrese el numero hasta donde desea presentar:"))
                cal = Basico()
                cal.numerosN(n1)
                input("Presione una tecla para continuar...")
                
            elif opc2 == "2":
                os.system("cls")
                print("<----Múltiplo de cualquier numero---->")
                n1 = int(input("Ingrese el primer valor:"))
                n2 = int(input("Ingrese el segundo valor:"))
                cal = Basico()
                cal.multiplo(n1,n2)
                input("Presione una tecla para continuar...")
                
            elif opc2 == "3":
                os.system("cls")
                print("<----Presentar los divisores de un numero---->")
                n1 = int(input("Ingrese el primer valor:"))
                cal = Basico()
                print("La respuesta es: ",cal.divisoresNumero(n1))
                input("Presione una tecla para continuar...")
                
            elif opc2 == "4":
                os.system("cls")
                print("<----Numero Primo---->")
                n1 = int(input("Ingrese el valor:"))
                cal = Basico()
                cal.primo(n1)
                input("Presione una tecla para continuar...")
                
            elif opc2 == "5":
                os.system("cls")
                print("<----Perfecto--->")
                n1 = int(input("Ingrese el valor:"))
                cal = Basico()
                cal.perfecto(n1)
                input("Presione una tecla para continuar...")
                
            elif opc2 == "6":
                os.system("cls")
                print("<----Factorial--->")
                n1 = int(input("Ingrese el valor:"))
                cal = Intermedio()
                print(cal.factorial(n1))
                input("Presione una tecla para continuar...")
                
            elif opc2 == "7":
                os.system("cls")
                print("<----Fibonacci--->")
                n1 = int(input("Ingrese el valor:"))
                cal = Intermedio()
                print(cal.fibonacci(n1))
                input("Presione una tecla para continuar...")
                
            elif opc2 == "8":
                os.system("cls")
                print("<----Primos Gemelos--->")
                n1 = int(input("Ingrese el primer valor:"))
                n2 = int(input("Ingrese el segundo valor:"))
                cal = Intermedio()
                cal.primosGemelos(n1,n2)
                input("Presione una tecla para continuar...")
                
            elif opc2 == "9":
                os.system("cls")
                print("<----Numeros Amigos--->")
                n1 = int(input("Ingrese el primer valor:"))
                n2 = int(input("Ingrese el segundo valor:"))
                cal = Intermedio()
                cal.amigos(n1,n2)
                input("Presione una tecla para continuar...")       

    elif opc == "3":
        opc3 = ""
        while opc3 != "11":
            os.system("cls")
            men3 = Menu("Menu Tratamiento Listas",["1)Presentar Lista", "2)Buscar Lista", "3)Lista Factorial","4)Lista Primo", "5)Lista Notas", "6)Insertar Lista", "7)Eliminar Lista", "8)Retornar Valor Lista", "9)Copiar Tupla Lista", "10)Vuelto Lista", "11)Salir"])
            opc3 = men3.menu()   
            if opc3 == "1":
                os.system("cls")
                print("<----Presentar lista--->")      
                num = int(input("Cuantos elementos desea en la lista?: "))
                lista = []
                for x in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista    
                resultado = TratamientoListas(lista)
                resultado.PresentarLista() 
                input("Presione una tecla para continuar...") 
            
            elif opc3 == "2":
                os.system("cls")
                print("<----Buscar Lista--->")
                lista = []       
                num = int(input("Cuantos elementos desea en la lista?: "))
                for i in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista
                buscar = int(input("Ingrese el valor a buscar:"))                
                resultado = TratamientoListas(lista)
                resultado.buscarLista(buscar) 
                input("Presione una tecla para continuar...") 
                
            elif opc3 == "3":
                os.system("cls")
                print("<----Lista Factorial--->")
                lista = []       
                num = int(input("Cuantos elementos desea en la lista?: "))
                for i in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista
                resultado = TratamientoListas(lista)
                resultado.ListaFactorial()
                
            elif opc3 == "4":
                os.system("cls")
                print("<----Lista Numeros Primos--->")
                lista = []       
                num = int(input("Cuantos elementos desea en la lista?: "))
                for i in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista
                resultado = TratamientoListas(lista)
                resultado.listaPrimo()
                
            elif opc3 == "5":
                os.system("cls")
                print("<----Lista Notas--->")
                diccionario=[{'nombre':'Josue', 'nota':100},{'nombre':'Mario','nota':80},{'nombre':'Miguel','nota':90}]
                resultado = TratamientoListas(diccionario)
                resultado.listaNotas()
                
            elif opc3 == "6":
                os.system("cls")
                print("<----Insertar Lista--->")
                lista = []       
                num = int(input("Cuantos elementos desea en la lista?: "))
                for i in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista
                ele = int(input("Ingrese el elemento que desea colocar a la lista:"))
                val = int(input("Ingrese la posicion en la que se insertara el elemento:"))
                resultado = TratamientoListas(lista)
                resultado.insertarLista(ele,val-1)
                
            elif opc3 == "7":
                os.system("cls")
                print("<----Eliminar Lista--->")
                lista = []       
                num = int(input("Cuantos elementos desea en la lista?: "))
                for i in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista
                resultado = TratamientoListas(lista)
                resultado.eliminarLista()
                
            elif opc3 == "8":
                os.system("cls")
                print("<----Retornar valor lista--->")
                lista = []       
                num = int(input("Cuantos elementos desea en la lista?: "))
                for i in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista
                resultado = TratamientoListas(lista)
                resultado.retornaValorLista()
                
            elif opc3 == "9":
                os.system("cls")
                print("<----Copiar tupla--->")
                tupla = (2,2,3,4,5,6,7)
                resultado = TratamientoListas(tupla)
                print(resultado.copiarTuplaLista())
                
            elif opc3 == "10":
                os.system("cls")
                print("<----Vuelto lista--->")
                diccionario={}
                lista=[]
                num=int(input("ingrese cuantos diccionarios desea ingresar: "))
                for x in range(num):
                    clave=(input("ingrese su clave para el diccionario: ")).capitalize()
                    valor=int(input("ingrese el valor de la clave para el diccionario: "))

                    diccionario[clave]=valor
                    lista.append(diccionario)
                    diccionario={}
                resultado = TratamientoListas(diccionario)
                resultado.vueltoLista(lista)
                

    elif opc == "4":
        opc4 = ""
        while opc4 != "10":
            os.system("cls")
            men4 = Menu("Menu Operaciónes de Cadenas",["1)Recorrer Cadena", "2)Buscar Caracter", "3)Lista Posiciones","4)Lista Palabras", "5)cadena Lista", "6)Insertar Dato", "7)Eliminar Ocurrencias", "8)Retornar Valor", "9)Concatenar cadena", "10)Salir"])
            opc4 = men4.menu()
            if opc4 == "1":
                os.system("cls")
                print("<---Recorrer Cadena---->")
                Texto = input("Ingrese la Cadena:")
                resultado = Cadena(Texto)
                resultado.recorrerCadena()
                input("Presione una tecla para continuar...")
                
            elif opc4 == "2":
                os.system("cls")
                print("<---Buscar Caracter---->")
                Texto = input("Ingrese la Cadena:")
                buscar = input("Ingrese el caracter que desea buscar:")
                resultado = Cadena(Texto)
                resultado.buscarCaracter(buscar)
                input("Presione una tecla para continuar...")
                
            elif opc4 == "3":
                os.system("cls")
                print("<---Lista Posiciones---->")
                Texto = input("Ingrese la Cadena:")
                buscar = input("Ingrese el caracter:")
                resultado = Cadena(Texto)
                resultado.listaPosiciones(buscar)
                input("Presione una tecla para continuar...")
                
            elif opc4 == "4":
                os.system("cls")
                print("<---Lista Palabras---->")
                Texto = input("Ingrese la Cadena:")
                resultado = Cadena(Texto)
                resultado.listaPalabras()
                input("Presione una tecla para continuar...")
                
            elif opc4 == "5":
                os.system("cls")
                print("<---Lista Palabras---->")
                lista=[]
                num = int(input("Cuantos elementos desea en la lista?: "))
                lista = []
                for x in range(num):
                    frase = (input("Ingrese el elemento:")) 
                    lista.append(frase)
                aux=lista 
                print("La lista se creada es la siguuente:")
                print(lista)   
                resultado = Cadena(lista)
                print("Transformacion a cadena:")
                resultado.cadenaLista()
                input("Presione una tecla para continuar...")
                
            elif opc4 == "6":
                os.system("cls")
                print("<---Insertar Dato---->")
                Texto = input("Ingrese la Cadena:")
                texto_insertar = input("Ingrese el texto a insertar:")
                posicion_insertar = int(input("Ingrese en que posicion desea insertar el texto:"))
                resultado = Cadena(Texto)
                resultado.insertarDato(texto_insertar,posicion_insertar)
                input("Presione una tecla para continuar...")   
            
            elif opc4 == "7":
                os.system("cls")
                print("<---Eliminar Ocurrencias---->")
                Texto = input("Ingrese la Cadena:")
                Buscado = input("Ingrese el elemento a buscar:")
                resultado = Cadena(Texto)
                resultado.eliminarOcurrencias(Buscado)
                input("Presione una tecla para continuar...")
        
            elif opc4 == "8":
                os.system("cls")
                print("<---Retornar Valor---->")
                texto = input("Ingrese el texto:")        
                res = Cadena(texto)
                pos = int(input("Ingrese posicion:"))
                res.retornaValor(pos)  
                input("Presione una tecla para continuar...")
                
            elif opc4 == "9":
                os.system("cls")
                print("<---Retornar Valor---->")
                texto = input("Ingrese su nombre:")        
                res = Cadena(texto)
                res.concatenarCadena(texto)  
                input("Presione una tecla para continuar...")
                  
    elif opc == "5":
        print("Gracias por usar el sistema")
    else:
        print("Opcion no valida")

print("Lo espermos en una proxima ocasión")
