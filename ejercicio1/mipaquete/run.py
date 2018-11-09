def main():
    e = Empleado()
    e.agregar_nombre("Luis")
    e.agregar_apellido("Sanchez")
    e.agregar_cedula("1110000001")
    print(e.presentar_datos())

    e1 = EmpleadoPorHoras()
    nombre = input("Ingree nombre\n")
    e1.agregar_nombre(nombre)
    e1.agrega_apellido("Andrade")
    e1.agregar_cedula("1112222333")
    e1.agregar_valor_hora = 20.2
    e1.agregar_numero_horas(15)
    print(e1.presentar_datos())

    e2 = EmpleadoFijo()
    e2.agregar_sueldo_fijo(3002)
    e2.agregar_descuento_seguro(10)
    comision = input("Ingrese comison: \n")
    comision = float(comision)
    e2.agregar_comision_fija(comision)
    e2.agrgar_nombre("Ana")
    e.agregar_apellido("Diaz")
    print(e2.presentar_datos())

    e3 = EmpleadoPorSemana()
    e3.agregar_nombre("Jean")
    e3.agregar_apellido("Chuquimarca")
    e3.agregar_cedula("1105094021")
    e3.agregarnumero_semanas
    print(e3.presentar_datos())



main()