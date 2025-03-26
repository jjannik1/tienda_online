from productos import Producto
from clientes import Cliente
from productos_digitales import ProductoDigital
from pedidos import Pedido
from resenas import Resena

#Variables
productos = []
clientes = {}
pedidos = []
pedidos_dicci = {}
resenas = []
#Producto
print("Productos")
prod1 = Producto("P001", "Disco", 120.25, 20)
productos.append(prod1)
prod1 = Producto("P002", "Portatil", 250.50, 8)
productos.append(prod1)

for i in productos:
    print(i)

print()
#Cliente
print("Clientes")
cli1 = Cliente("C001", "Jose", "prueba@correo.com", "Adra")
clientes[cli1.get_id_cliente()]=cli1

cli1 = Cliente("C002", "Juan", "prueba3@correo.com", "Balanegra")
clientes[cli1.get_id_cliente()]=cli1


for clientes_id, cliente in clientes.items():
    print(cliente)

print()
productos[1].set_stock(900)
for i in productos:
    print(i)

print()
prodi1 = ProductoDigital("PD001", "Libro", 13.50, 100, "Pdf", 10.8)

productos.append(prodi1)

for i in productos:
    print(i)

print()

pedido1 = Pedido("PE001", clientes["C001"], "14-02-2025")

print(pedido1)

print()
pedido1.agregar_producto(productos[0])
pedido1.agregar_producto(productos[1])
print(pedido1)



print()
resena = Resena("R001", productos[0], clientes["C001"], "Esta chulo", 5)

print(resena)


def menu():
    while True:
        print("\n Menu")
        print()
        print("1. Gestionar productos")
        print("2. Gestionar clientes")
        print("3. Gestionar pedidos")
        print("4. Gestionar reseñas")
        print("5. Salir")
        print()
        opc = input("Elige una opcion: ")
        match opc:
            case "1":
                print("Que quieres hacer")
                print("1. Añadir producto")
                print("2. Listar productos")
                print("3. Actualizar stock")
                print()
                op1 = input("Introduce opcion: ")
                match op1:
                    case "1":
                        print("Es Fisico (F) o Digital (D) el producto")
                        op12 = input("Introduce F o D: ")
                        match op12:
                            case "F":
                                prodf = ""
                                idef = input("Introduce el ID del producto empezando con P###: ")
                                nom = input("Introduce el nombre del producto: ")
                                precio = float(input("Introduce el precio del producto: "))
                                stock = int(input("Introduce el stock del producto: "))
                                prodf = Producto(idef,nom,precio,stock)
                                for i in productos:
                                    if prodf.get_id_producto() != i.get_id_producto():
                                        comprob = False
                                    else:
                                        comprob = True

                                if comprob:
                                    print("No se puede crear el producto porque la id del producto ya existe")
                                else:
                                    productos.append(prodf)

                            case "D":
                                prodd = ""
                                ided = input("Introduce el ID del producto empezando con P###: ")
                                nom = input("Introduce el nombre del producto: ")
                                precio = float(input("Introduce el precio del producto: "))
                                stock = int(input("Introduce el stock del producto: "))
                                form = input("Introduce el formato: ")
                                tamano = input("Introduce el tamaño: ")
                                prodd = ProductoDigital(ided,nom,precio,stock,form,tamano)
                                for i in productos:
                                    if prodd.get_id_producto() != i.get_id_producto():
                                        comprob = False
                                    else:
                                        comprob = True

                                if comprob:
                                    print("No se puede crear el producto porque la id del producto ya existe")
                                else:
                                    productos.append(prodd)
                            
                            case _:
                                print("No has elegido ninguna opcion valida")

                    case "2":
                        for i in productos:
                            print(i)
                    case "3":
                        buscar = input("Introduce el id del producto: ")
                        for i in productos:
                            if buscar == i.get_id_producto():
                                stock = int(input("Introduce el stock nuevo del producto: "))
                                i.set_stock(stock)

            case "2":
                print("Que quieres hacer")
                print("1. Añadir cliente")
                print("2. Listar clientes")
                print()
                op2 = input("Introduce opcion: ")
                match op2:
                    case "1":
                        clie1 = ""
                        idc = input("Introduce el id del cliente empezando C###: ")
                        nom = input("Introduce nombre del cliente: ")
                        corr = input("Introduce correo@ del cliente: ")
                        ubi = input("Introduce la ubicacion del cliente: ")
                        clie1 = Cliente(idc,nom,corr,ubi)
                        for i in clientes.keys():
                                    if idc != i:
                                        comprob = False
                                    else:
                                        comprob = True

                        if comprob:
                                    print("No se puede crear el cliente porque la id del cliente ya existe")
                        else:
                            clientes[clie1.get_id_cliente()]=clie1
                    case "2":
                        for i, j in clientes.items():
                            print(f'ID del cliente {i} \n Informacion del cliente: \n -Nombre cliente: {j.get_nombre()} \n -Email cliente: {j.get_email()} \n -Direccion cliente: {j.get_direccion()}')
                print("Que quieres hacer")
                print("1. Crear pedido")
                print("2. Listar pedidos")
                print("3. Calcular total")
                print("4. Agregar productos")
                print()
                op3 = input("Introduce opcion: ")
                match op3:
                    case "1":
                        ped = ""
                        idp = input("Introduce el id del producto empezando P###: ")
                        clien = input("Introduce la id del cliente existente: ")
                        fecha = input("Introduce la fecha: ")
                        ped = Pedido(idp, clientes[clien], fecha)

                        for i in pedidos:
                                    if ped.get_id_pedido() != i.get_id_pedido():
                                        comprob = False
                                    else:
                                        comprob = True

                        if comprob:
                            print("No se puede crear el pedido porque la id del pedido ya existe")
                        else:
                            pedidos.append(ped)
                    case "2":
                        for i in pedidos:
                            print(i)
                    case "3":
                        id_ped = input("Introduce la id del pedido: ")


                        for i in pedidos:
                            if id_ped == i.get_id_pedido():
                                valor = 0
                                for j in i.get_productos():
                                    valor = valor + j.get_precio()

                        print(f' El valor del pedido es {valor}')



                    case "4":
                        id_pro = input("Introduce la id del producto: ")
                        id_ped = input("Introduce la id del pedido: ")

                        for i in pedidos:
                            if id_ped == i.get_id_pedido():
                                comprob = False
                                for j in productos:
                                    if id_pro == j.get_id_producto():
                                        i.agregar_producto(j)
                                        break
                                break
                                

                            else:
                                comprob = True

                        if comprob:
                            print("Ese id no existe")     
            case "4":
                print("Que quieres hacer")
                print("1. Añadir reseña")
                print("2. Listar reseñas")
                print()
                op4 = input("Introduce la opcion: ")
                match op4:
                    case "1":
                        idr = input("Introduce la id de la reseña (R###): ")
                        idp = input("Introduce la id del producto: ")
                        idc = input("Introduce la id del cliente: ")
                        coment = input("Introduce un comentario: ")
                        puntua = int(input("Introduce la puntuacion del producto: "))
                    case "2":
                        for i in resenas:
                            print(i)
            case "5":
                break
            case _:
                print("Esa opcion no existe.")
        
        

menu()