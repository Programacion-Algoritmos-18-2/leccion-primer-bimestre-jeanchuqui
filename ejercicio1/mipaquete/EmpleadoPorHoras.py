class EmpleadoPorHoras(Empleado)

    def __init__(self):
        super(EmpleadoPorHoras,self).__init__()
        self numero_horas = 0
        self valor_hora = 0

    def agregar_numero_horas(self, numeros):
        self.numero_horas = numeros

    def obtener_numero_horas(self):
        return self.numero_horas

    def agregar_valor_hora(self, valores):
        self.valor_hora = valores

    def obtener_valor_hora(self):
        return self.valor_hora

    def presentar_datos(self):
        cadena = "%s \n Numero horas: %s \nValor hora: %s \nSueldo final: %s" %
        (super(EmpleadoPorHoras,self).presentar_datos(), self.obtener_numero_horas(), self.obtener_valor_hora(),
         self.calcular_valor_sueldo())

    def calcular_valor_sueldo(self):
        print(self.numero_horas)
        print(self.valor_hora)
        print(self.comision_fija)