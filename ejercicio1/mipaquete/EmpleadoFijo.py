class EmpleadoFijo(Empleado)

    def __init__(self):
        super(EmpleadoFijo,self).__init__()
        self sueldo_fijo = 0
        self descuento_seguro = 0

    def agregar_sueldo_fijo(self, sueldos):
        self.sueldo_fijo = sueldos

    def obtener_sueldo_fijo(self):
        return self.sueldo_fijo

    def agregar_descuento_seguro(self, descuentos):
        self.descuento_seguro = descuentos

    def obtener_descuento_seguro(self):
        return self.descuento_seguro

    def presentar_datos(self):
        cadena = "%s \nSueldo Fijo: %s \nDescuento seguro: %s \nSueldo final: %s" %
        (super(EmpleadoFijo,self).presentar_datos(), self.obtener_sueldo_fijo(), self.obtener_descuento_seguro(),
         self.calcular_valor_sueldo())

    def calcular_valor_sueldo(self):
        print(self.sueldo_fijo)
        print(self.descuento_seguro)
        print(self.comision_fija)
