import misfunciones  as m

while True:
    m.limpiar()
    m.printA("sistema gestion agentes")
    m.printA("__________________________")
    print("1) agregar agentes")
    print("2) listas agentes" )
    print("0) salir")
    m.printA("_____________________")
    opcion = input("seleccione : ")
    if opcion=="0":
        break
    elif opcion=="1":
        m.printA("agregar agente")
        nombre = input("ingrese nombre agente : ").title()
        rol = input("ingrese rol agente : ").title()
        genero = input("ingrese genero agente  (F/M/R): ").title()[0] #para solo sacar primera letra
        ulti = input("ingrese ulti del agente : ").title()
        m.guardar(nombre,rol,genero,ulti)
    elif opcion=="2":
        m.printA("lista agentes")
        m.listar()
    else:
        m.printR("opcion no valida")

