import random
import os
import csv
rojo = True
sectores = tuple(["San Bernardo","Calera De Tango","Buin"])
pedidos = [["Nro. Pedido","Cliente","Dirección","Sector","Saco 5kg","Saco 10kg","Saco 20kg"]]

def registro_pedido(pedidos):
   saco_5kg = 0
   saco_10kg = 0
   saco_20kg= 0
   verde = True
   numero = 0
   numero = random.randint(1,1000)
   numero+=1
   name = input("Ingrese Nombre y apellido cliente: ")
   direccion = input("\nIngrese su dirección: ")
   while verde ==True:
      print("Comunas disponibles:\n")
      for i in sectores:
         print(i)
      comuna = input("\nIngrese sector disponible: ").title()
      if comuna in sectores:
         verde = False
         blue = True
             
      else:
         print("Ingrese comuna correcta.\n")
         verde = True 
      while blue ==True:
          cincokg= int(input("¿Cuantos sacos de 5kg desea?: "))
          diezkg= int(input("¿Cuantos sacos de 10kg desea?: "))
          veintekg= int(input("¿Cuantos sacos de 20kg desea?: "))
          saco_5kg+=cincokg
          saco_10kg+=diezkg
          saco_20kg+=veintekg
          break
           

   pedidos.append([numero,name,direccion,comuna,saco_5kg,saco_10kg,saco_20kg])   

def volver():
   amarillo = True
   while amarillo==True:
      print("no se encuentra ningun registro.")
      m = input("Ingrese (M) Para volver al menu: ").upper()
      if m == "M":
         amarillo = False
         break
      else:
         amarillo = True  

def listar_pedidos(pedidos):
 for x in pedidos:
      for a in x:
         print(a,end="\t")
      print()

def hoja_ruta(pedidos):
   seleccion_zona = input("Seleccione Sector: ").title()
   if seleccion_zona in sectores:
      with open ("Lista Zona.txt",'w') as archivo:
       archivo.write(f"ID\tNombre Cliente\tdireccion\tSector\tSaco 5kg\tSaco 10kg\tSaco 20kg")
      for a in pedidos[4:]:
       if seleccion_zona == pedidos[4:]:
         archivo.write(f"{a[0]}\t")#no me acuerdo como se hacia
   else:
      ("ingrese un sector valido") 

   with open("Listado.csv",'w',newline=' ') as archivo_csv:
    archivo_csv.writerow(pedidos)
    for x in pedidos:
       archivo_csv.writerow([x])
          
          
while rojo == True:
    menu = ("\n1.Registrar Pedido","2.Listar pedidos","3.Imprimir Hoja de ruta","4.Salir del Programa")
    for a in menu:
     print(a)
    try:
       opt = int(input("\nIngrese su opción: "))
       
       if opt==1:
         registro_pedido(pedidos)
        
       elif opt==2:
          if len(pedidos) ==1:
             volver()
          else:
             listar_pedidos(pedidos)   

       elif opt==3:
           if len(pedidos) ==1:
             volver()
           else:
             hoja_ruta(pedidos) 

       elif opt==4:
          print("Usted ha salido del programa correctamente.")
          rojo = False

       else:
            print("\nSeleccione la opción correcta:")

    except ValueError:
        print("\nSelecione la opcion con el numero correcto.")
        rojo = True
               
       
            




    
    