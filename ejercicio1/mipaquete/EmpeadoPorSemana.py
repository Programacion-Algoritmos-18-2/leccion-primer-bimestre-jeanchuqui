class EmpleadoPorSemana(Empleado)

    def __init__(self):
        super(EmpleadoPorSemana,self).__init__()
        self numero_semanas = 0
        self valor_semanal = 0

    def agregar_numero_semanas(self, numeros):
        self.numero_semanas = numeros

    def obtener_numero_semanas(self):
        return self.numero_semanas

    def agregar_valor_semanal(self, valores):
        self.valor_semanal = valores

    def obtener_valor_semanal(self):
        return self.valor_semanal

    def presentar_datos(self):
        cadena = "%s \n Numero semanas: %s \nValor semanal: %s \nSueldo final: %s" %
        (super(EmpleadoPorSemana,self).presentar_datos(), self.obtener_numero_semanas(), self.obtener_valor_semanal(),
         self.calcular_valor_sueldo())

    def calcular_valor_sueldo(self):
        print(self.numero_semanas)
        print(self.valor_semanal)
        print(self.comision_fija)